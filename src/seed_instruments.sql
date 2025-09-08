CREATE TABLE IF NOT EXISTS instruments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

INSERT INTO instruments (name, type) VALUES ('Guitarra', 'Cuerda');
INSERT INTO instruments (name, type) VALUES ('Bajo', 'Cuerda');
INSERT INTO instruments (name, type) VALUES ('Batería', 'Percusión');
INSERT INTO instruments (name, type) VALUES ('Teclado', 'Tecla');
INSERT INTO instruments (name, type) VALUES ('Saxofón', 'Viento');
INSERT INTO instruments (name, type) VALUES ('Flauta', 'Viento');
INSERT INTO instruments (name, type) VALUES ('Trompeta', 'Viento');
INSERT INTO instruments (name, type) VALUES ('Violín', 'Cuerda');
INSERT INTO instruments (name, type) VALUES ('Platillos', 'Percusión');
