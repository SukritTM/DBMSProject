DROP TABLE IF EXISTS recipie;
DROP TABLE IF EXISTS technique;
DROP TABLE IF EXISTS recipie_technique;

CREATE TABLE recipie(
    rid TEXT PRIMARY KEY,
    ingredients TEXT NOT NULL,
    serves INTEGER NOT NULL,
    cooktime INTEGER NOT NULL,
    body TEXT,
    veg TEXT NOT NULL,
    difficulty INTEGER(2),
    summary TEXT NOT NULL
);

CREATE TABLE technique(
    tid TEXT PRIMARY KEY,
    technique_name TEXT,
    ttype TEXT,
    difficulty INTEGER,
    utensils TEXT,
    body TEXT,
    theory TEXT,
    ingredients TEXT
);

CREATE TABLE recipie_technique(
    rid TEXT,
    tid TEXT,
    FOREIGN KEY (rid) REFERENCES reciepie(rid),
    FOREIGN KEY (tid) REFERENCES technique(tid),
);
