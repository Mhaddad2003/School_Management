import sqlite3

conn = sqlite3.connect("C:/Users/hp/Downloads/Gestion_Scolarite.db")
curs = conn.cursor()
curs.execute("PRAGMA foreign_keys = ON;")

curs.execute('''CREATE TABLE IF NOT EXISTS Etudiant (
                num_apogee INTEGER NOT NULL PRIMARY KEY,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                cin TEXT NOT NULL,
                date_naiss date NOT NULL
                )''')
result = curs.fetchone()

curs.execute('''CREATE TABLE IF NOT EXISTS Enseignant (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                cin TEXT NOT NULL,
                departement TEXT NOT NULL
            )''')
result = curs.fetchone()

curs.execute('''CREATE TABLE IF NOT EXISTS Module (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Enseignant_id INTEGER NOT NULL,
                matiere TEXT NOT NULL,
                semestre TEXT NOT NULL,
                FOREIGN KEY (Enseignant_id) REFERENCES Enseignant(id) ON UPDATE CASCADE ON DELETE SET NULL
            )''')
result = curs.fetchone()
            
curs.execute('''CREATE TABLE IF NOT EXISTS Inscrire (
                module_id INTEGER NOT NULL,
                etudiant_apogee INTEGER NOT NULL,
                note REAL,
                valide TEXT,
                PRIMARY KEY (module_id, etudiant_apogee),
                FOREIGN KEY (module_id) REFERENCES Module(id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (etudiant_apogee) REFERENCES Etudiant(num_apogee) ON UPDATE CASCADE ON DELETE CASCADE
            )''')
result = curs.fetchone()

print(result)