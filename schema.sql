DROP TABLE IF EXISTS swf;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS works;

CREATE TABLE swf (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    "desc" TEXT NOT NULL DEFAULT "No description.",
    filepath TEXT NOT NULL,
    filename TEXT NOT NULL,
    thumbnail TEXT
);
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL
);

CREATE TABLE works (
    work_id INTEGER PRIMARY KEY AUTOINCREMENT,
    swf_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (swf_id) REFERENCES swf (id),
    FOREIGN KEY (author_id) REFERENCES author (id)
);

/*Put the first one as an unknown author*/
INSERT INTO authors(author_name) VALUES("Unknown Author");

/*test records*/
/*
INSERT INTO authors(author_name) VALUES("Test Author 1");
INSERT INTO authors(author_name) VALUES("Test Author 2");
INSERT INTO authors(author_name) VALUES("Test Author 3");
INSERT INTO authors(author_name) VALUES("Test Author 4");

INSERT INTO swf(title, "desc", filepath) VALUES("Test Title 1", "Test Description.", "flash/test/test.swf");
INSERT INTO swf(title, "desc", filepath) VALUES("Test Title 2", "Test Description.", "flash/test/test.swf");
INSERT INTO swf(title, "desc", filepath) VALUES("Test Title 3", "Test Description.", "flash/test/test.swf");
INSERT INTO swf(title, "desc", filepath) VALUES("Test Title 4", "Test Description.", "flash/test/test.swf");

INSERT INTO works(swf_id,author_id) VALUES (1, 2);
INSERT INTO works(swf_id,author_id) VALUES (2, 3);
INSERT INTO works(swf_id,author_id) VALUES (3, 4);
INSERT INTO works(swf_id,author_id) VALUES (4, 5);

*/