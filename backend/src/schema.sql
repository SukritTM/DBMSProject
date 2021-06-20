DROP TABLE IF EXISTS recipie;
DROP TABLE IF EXISTS technique;
DROP TABLE IF EXISTS recipie_technique;

CREATE TABLE recipie(
    rid INTEGER PRIMARY KEY AUTOINCREMENT,
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
    utensils TEXT,
    body TEXT,
    theory TEXT,
);

CREATE TABLE ingredient(
    iid INTEGER PRIMARY KEY AUTOINCREMENT
    name TEXT NOT NULL,
);

CREATE TABLE recipie_ingredient(
    iid INTEGER PRIMARY KEY,
    rid INTEGER PRIMARY KEY,
    quantity TEXT,
    FOREIGN KEY (rid) REFERENCES recipie(rid),
    FOREIGN KEY (iid) REFERENCES ingredient(iid)
);

CREATE TABLE recipie_technique(
    rid TEXT,
    tid TEXT,
    FOREIGN KEY (rid) REFERENCES recipie(rid),
    FOREIGN KEY (tid) REFERENCES technique(tid),
);
commit;