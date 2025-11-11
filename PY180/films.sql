DROP TABLE IF EXISTS public.films;
CREATE TABLE films (title varchar(255), "year" integer, genre varchar(100));

INSERT INTO films(title, "year", genre) VALUES ('Die Hard', 1988, 'action');  
-- The SQL file we used has the column name year in quotes. 
    -- While it's fine to use year without quotes in PostgreSQL, 
    -- it can cause issues in other RDBMSs when year is a reserved word.
INSERT INTO films(title, "year", genre) VALUES ('Casablanca', 1942, 'drama');  
INSERT INTO films(title, "year", genre) VALUES ('The Conversation', 1974, 'thriller');  