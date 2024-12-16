CREATE DATABASE IF NOT EXISTS Gestion_Scolarite;

CREATE TABLE IF NOT EXISTS Etudiant (
    num_apogee INT NOT NULL PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    prenom VARCHAR(20) NOT NULL,
    cin VARCHAR(20) NOT NULL,
    date_naiss date NOT NULL,
);

CREATE TABLE IF NOT EXISTS Enseignant (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(20) NOT NULL,
    prenom VARCHAR(20) NOT NULL,
    cin VARCHAR(20) NOT NULL,
    departemet VARCHAR(20) NOT NULL,
);

CREATE TABLE IF NOT EXISTS Module (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Enseignant_id INT NOT NULL,
    matiere VARCHAR(20) NOT NULL,
    semestre VARCHAR(20) NOT NULL,
    FOREIGN KEY Enseignant_id REFERENCES Enseignant(id)
);

CREATE TABLE IF NOT EXISTS Inscrire (
    module_id INT NOT NULL,
    etudiant_apogee INT NOT NULL,
    PRIMARY KEY (module_id, etudiant_apogee),
    FOREIGN KEY module_id REFERENCES Module(id),
    FOREIGN KEY Etudiant_apogee REFERENCES Etudiant(num_apogee)
);