from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from src.db import get_db


bp = Blueprint('mainpages', __name__, url_prefix='/page')


@bp.route('/input', methods=('GET', 'POST'))
def dbinput():
    if request.method == 'GET':
        db = get_db()
        db.execute(
            'INSERT INTO recipie (serves, cooktime, body, veg, difficulty, summary) VALUES (?, ?, ?, ?, ?, ?)',
            (2, 2, 'body1', 'Veg', 2, 'summary1')
        )
        db.execute(
            'INSERT INTO ingredient (name) VALUES (?), (?)', ('genericingredient1', 'genericingredient2')
        )
        db.execute(
            'INSERT INTO recipie_ingredient (rid, iid, quantity) VALUES (?,?,?), (?,?,?)', 
            (1,1,'1 tsp',1,2,'1 tsp')
        )
        db.commit()
        data = db.execute('SELECT * FROM recipie').fetchone()
        return str(data[0])

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
            '''SELECT name FROM 
            recipie r INNER JOIN recipie_ingredient ri ON r.rid = ri.rid
            INNER JOIN ingredient i on ri.iid = i.iid
            WHERE r.rid = ?''', 
            (rid)
        ).fetchall()
        return render_template('recipiepage.html', recipie=recipie, ingredients=ingredients)

