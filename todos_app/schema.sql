CREATE TABLE lists (
id serial PRIMARY KEY,
title text NOT NULL UNIQUE);

CREATE TABLE todos (
id serial PRIMARY KEY,
title text NOT NULL,
completed bool NOT NULL DEFAULT false,
list_id text NOT NULL REFERENCES lists(title) ON DELETE CASCADE
);