
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES 
    ('Abhi', 'abhi@example.com'),
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');

    