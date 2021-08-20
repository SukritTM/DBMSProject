import sqlite3
import sys

import click
from flask import current_app, g
from flask.cli import with_appcontext

import os

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    g.db.row_factory = sqlite3.Row

    return g.db

# get db, but do not use the app or modify the request context
def get_db_noapp():
    os.chdir('instance')
    print(os.getcwd())
    db = sqlite3.connect(
            'src.sqlite',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    db.row_factory = sqlite3.Row

    os.chdir('..')

    return db

def close_db(e=None):
    db = g.pop('db', None)
    
    if db:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    '''Clear the existing database and remake all tables'''
    init_db()
    click.echo('Database initialised')

@click.command('test')
@with_appcontext
def test_command():
    click.echo('Command executed')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(test_command)


# extremely simple interface to run database commands, bc I'm tired of doing it by hand

def executesql(commands, db):
    del commands[-1] # temp patch till I figure out what the hell is going on
    cur = db.cursor()
    statement = ' '.join(commands)
    # print(statement)
    if statement.split(' ')[0] == 'SELECT':
        try:
            msg = cur.execute(statement).fetchall()
        except sqlite3.OperationalError as error:
            msg = 'Error: '+str(error)
        
        longestlen = list()

        for row in msg:
            for attr in range(len(row)):
                print(len( str( row[attr])))

        for row in msg:
            for attr in range(len(row)):
                print(row[attr], end=' : ')
            print()
    
    del cur
        

def runcommand(line):
    if line == 'quit':
        sys.exit(0)

def ioloop():
    db = get_db_noapp()
    sqlcommand = []
    sqlstatement = False
    while True:
        if sqlstatement:
            print('...', end=' ', flush=True)
        else:
            print(">", end=' ', flush=True)
        line = input().replace('\n', '')

        if sqlstatement and (line != 'end' or line != 'END'):
            sqlcommand.append(line)
        else:
            runcommand(line)

        if line == 'sql' or line == 'SQL':
            sqlstatement = True
        if line == 'end' or line == 'END':
            sqlstatement = False
            executesql(sqlcommand, db)

# always run this from the parent directory, i.e. the directory above the one that contains your app factory
if __name__ == "__main__":
    ioloop()