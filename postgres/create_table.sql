CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    avg_temp DOUBLE PRECISION,
);