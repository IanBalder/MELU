-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create bars table
CREATE TABLE IF NOT EXISTS bars (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255),
    number VARCHAR(20),
    description TEXT,
    image VARCHAR(255),
    open_hours VARCHAR(100)
);

-- Create items table
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    bar_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(5, 2) NOT NULL,
    category VARCHAR(50),
    FOREIGN KEY (bar_id) REFERENCES bars(id) ON DELETE CASCADE
);

-- Create comments table
CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    bar_id INT NOT NULL,
    user_id INT NOT NULL,
    comment VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bar_id) REFERENCES bars(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create favourites table
CREATE TABLE IF NOT EXISTS favourites (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    bar_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (bar_id) REFERENCES bars(id) ON DELETE CASCADE
);

-- Create ratings table
CREATE TABLE IF NOT EXISTS ratings (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    bar_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (bar_id) REFERENCES bars(id) ON DELETE CASCADE
);
