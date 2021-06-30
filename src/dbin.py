from flask import Blueprint, render_template, request

from src.db import get_db

bp = Blueprint('dbin', __name__, url_prefix = '/dbin')

@bp.route('/techniques', methods=('GET', 'POST'))
def techniques():
    if request.method == 'POST':
        db = get_db()
        iids = request.form['Associated_Ingredients'].split(',')
        qtys = request.form['Quantities'].split(',')

        db.execute(
            'INSERT INTO technique (tid, technique_name, ttype, difficulty, body, theory) VALUES (?, ?, ?, ?, ?, ?)',
            (int(request.form['Technique_id']), request.form['Technique_name'], request.form["TType"], int(request.form["Difficulty"]), request.form["Body"], request.form['Theory'])
        )

        for i in range(len(iids)):
            if iids[i] != -1:
                db.execute(
                    'INSERT INTO ingredient_technique (iid, tid, quantity) VALUES (?, ?, ?)', 
                    (int(iids[i]), int(request.form['Technique_id']), qtys[i])
                )
        db.commit()

    return render_template('techniqueentrypage.html')

@bp.route('/ingredients', methods=('GET', 'POST'))
def ingredients():
    if request.method == 'POST':
        db = get_db()

        db.execute(
            'INSERT INTO ingredient (iid, name) VALUES (?, ?)',
            (request.form['Ingredient_id'], request.form['Ingredient_name'])
        )
        db.commit()
    
    return render_template('ingrediententrypage.html')

@bp.route('/recipies', methods=('GET', 'POST'))
def recipies():
    if request.method == 'POST':
        db = get_db()

        iids = request.form['Associated_Ingredients'].split(',')
        tids = request.form['Associated_Techniques'].split(',')

        db.execute(
            'INSERT INTO recipie (rid, recipie_name, serves, cooktime, body, veg, difficulty, summary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (int(request.form['Recipie_id']), request.form['Recipie_name'], request.form['Serves'], request.form['Cooktime'], request.form['Body'], request.form['Veg'], request.form['Difficulty'], request.form['Summary'])
        )

        for iidq in iids:
            db.execute(
                'INSERT INTO recipie_ingredient (rid, iid, quantity) VALUES (?, ?, ?)', 
                (int(request.form['Recipie_id']), int(iidq.split(';')[0]), iidq.split(';')[1])
            )
        
        for tid in tids:
            db.execute(
                'INSERT INTO recipie_technique (rid, tid) VALUES (?, ?)', 
                (int(request.form['Recipie_id']), int(tid))
            )
        db.commit()

    return render_template('recipieentrypage.html')