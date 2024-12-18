-- Créer la base de données
CREATE DATABASE IF NOT EXISTS Gestion_Scolarite;

-- Créer les tables dans SQLite

-- Table Etudiant
CREATE TABLE IF NOT EXISTS Etudiant (
    num_apogee INTEGER NOT NULL PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    cin TEXT NOT NULL,
    date_naiss DATE NOT NULL
);

-- Table Enseignant
CREATE TABLE IF NOT EXISTS Enseignant (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    cin TEXT NOT NULL,
    departement TEXT NOT NULL
);

-- Table Module
CREATE TABLE IF NOT EXISTS Module (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Enseignant_id INTEGER NOT NULL,
    matiere TEXT NOT NULL,
    semestre TEXT NOT NULL,
    FOREIGN KEY (Enseignant_id) REFERENCES Enseignant(id)
);

-- Table Inscrire
CREATE TABLE IF NOT EXISTS Inscrire (
    module_id INTEGER NOT NULL,
    etudiant_apogee INTEGER NOT NULL,
    note REAL,
    valide TEXT,
    PRIMARY KEY (module_id, etudiant_apogee),
    FOREIGN KEY (module_id) REFERENCES Module(id),
    FOREIGN KEY (etudiant_apogee) REFERENCES Etudiant(num_apogee)
);
