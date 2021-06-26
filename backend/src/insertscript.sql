INSERT INTO recipie (recipie_name, serves, cooktime, body, veg, difficulty, summary) VALUES  ('recipie1', 2, 2, 'body1', 'Veg', 2, 'summary1'), ('recipie2', 2, 2, 'body2', 'non-veg', 2, 'summary2');
 
INSERT INTO ingredient (name) VALUES ('ingredient1'), ('ingredient2'), ('ingredient3');

INSERT INTO recipie_ingredient (rid, iid, quantity) VALUES (1, 1, '1tsp'), (1, 2, '1 pinch'), (2, 1, '2tsp'), (2, 3, '1 pinch');

INSERT INTO technique (technique_name, ttype, difficulty, body, theory) VALUES ('technique1', 'type1', 2, 'tbody1', 'theory1'), ('technique2', 'type2', 3, 'tbody2', 'theory2'), ('technique3', 'type3', 4, 'tbody3', 'theory3'), ('technique4', 'type4', 5, 'tbody4', 'theory4');

INSERT INTO recipie_technique (rid, tid) VALUES (1, 1), (1, 2), (2, 1), (2, 3);

INSERT INTO ingredient_technique (tid, iid, quantity) VALUES (1, 1, '1tsp'), (1, 2, '1 pinch'), (3, 1, '1tsp');

