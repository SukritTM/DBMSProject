from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
from src.db import get_db


bp = Blueprint('mainpages', __name__, url_prefix='/page')

@bp.route('/input', methods=('GET', 'POST'))
def dbinput():
    if request.method == 'GET':
        
        db = get_db()
        with current_app.open_resource('insertscript.sql') as f:
            db.executescript(f.read().decode('utf8'))
            db.commit()

        data = db.execute('SELECT * FROM recipie').fetchone()
        return str(data['recipie_name'])

@bp.route('/recipie', methods=('GET', 'POST'))
def recipiepage():
    rid = request.args.get('id', type=str)
    if request.method == 'GET':
        db = get_db()
        recipie = db.execute(
            'SELECT * FROM recipie WHERE rid = ?', 
            (rid)
        ).fetchone()
        ingredients = db.execute(
            '''SELECT name, quantity FROM 
            recipie r INNER JOIN recipie_ingredient ri ON r.rid = ri.rid
            INNER JOIN ingredient i on ri.iid = i.iid
            WHERE r.rid = ?''', 
            (rid)
        ).fetchall()
        techniques = db.execute(
            '''SELECT technique_name, t.tid FROM 
            recipie r INNER JOIN recipie_technique rt ON r.rid = rt.rid
            INNER JOIN technique t on rt.tid = t.tid
            WHERE r.rid = ?''', 
            (rid)
        ).fetchall()
        return render_template('recipiepage.html', recipie=recipie, ingredients=ingredients, techniques=techniques)

@bp.route('/technique', methods=('GET', 'POST'))
def techniquepage():
    tid = request.args.get('id', type=str)
    if request.method == 'GET':
        db = get_db()
        technique = db.execute(
            'SELECT technique_name, ttype, difficulty, body, theory FROM technique t WHERE t.tid = ?', (tid)
        ).fetchone()

        ingredients = db.execute(
            '''SELECT name, quantity, t.tid FROM 
            technique t INNER JOIN ingredient_technique it ON t.tid = it.tid
            INNER JOIN ingredient i on it.iid = i.iid
            WHERE t.tid = ?''', 
            (tid)
        ).fetchall()
        return render_template('techniquepage.html', technique = technique, ingredients=ingredients)

@bp.route('/recipies', methods=('GET', 'POST'))
def recipies():
    if request.method == 'GET':
        db = get_db()
        recipies = db.execute('SELECT recipie_name, rid FROM recipie').fetchall()
        return render_template('recipielist.html', recipies=recipies)

@bp.route('/techniques', methods=('GET', 'POST'))
def techniques():
    if request.method == 'GET':
        db = get_db()
        techniques = db.execute('SELECT technique_name, tid FROM technique').fetchall()
        return render_template('techniquelist.html', techniques=techniques)