DROP TABLE IF EXISTS recipie;
DROP TABLE IF EXISTS technique;
DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS recipie_ingredient;
DROP TABLE IF EXISTS recipie_technique;
DROP TABLE IF EXISTS ingredient_technique;

CREATE TABLE recipie(
    rid INTEGER PRIMARY KEY AUTOINCREMENT,
    recipie_name TEXT,
    serves INTEGER NOT NULL,
    cooktime INTEGER NOT NULL,
    body TEXT,
    veg TEXT NOT NULL,
    difficulty INTEGER(2),
    summary TEXT NOT NULL
);

CREATE TABLE technique(
    tid INTEGER PRIMARY KEY AUTOINCREMENT,
    technique_name TEXT,
    ttype TEXT,
    difficulty INTEGER,
    body TEXT,
    theory TEXT
);

CREATE TABLE ingredient(
    iid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE recipie_ingredient(
    iid INTEGER NOT NULL,
    rid INTEGER NOT NULL,
    quantity TEXT,
    FOREIGN KEY (rid) REFERENCES recipie(rid),
    FOREIGN KEY (iid) REFERENCES ingredient(iid)
);

CREATE TABLE recipie_technique(
    rid INTEGER NOT NULL,
    tid INTEGER NOT NULL,
    FOREIGN KEY (rid) REFERENCES recipie(rid),
    FOREIGN KEY (tid) REFERENCES technique(tid)
);

CREATE TABLE ingredient_technique(
    iid INTEGER NOT NULL,
    tid INTEGER NOT NULL,
    quantity TEXT,
    FOREIGN KEY (iid) REFERENCES recipie(iid),
    FOREIGN KEY (tid) REFERENCES technique(tid)
);