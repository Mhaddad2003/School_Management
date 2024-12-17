-- CREATE DATABASE IF NOT EXISTS Gestion_Scolarite;

CREATE TABLE IF NOT EXISTS Etudiant (
    num_apogee INTEGER NOT NULL PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    cin TEXT NOT NULL,
    date_naiss date NOT NULL,
);

CREATE TABLE IF NOT EXISTS Enseignant (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    cin TEXT NOT NULL,
    departemet TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS Module (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Enseignant_id INTEGER NOT NULL,
    matiere TEXT NOT NULL,
    semestre TEXT NOT NULL,
    FOREIGN KEY (Enseignant_id) REFERENCES Enseignant(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Inscrire (
    module_id INTEGER NOT NULL,
    etudiant_apogee INTEGER NOT NULL,
    note REAL NOT NULL,
    valide TEXT NOT NULL
    PRIMARY KEY (module_id, etudiant_apogee),
    FOREIGN KEY (module_id) REFERENCES Module(id),
    FOREIGN KEY (Etudiant_apogee) REFERENCES Etudiant(num_apogee)
);