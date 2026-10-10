CREATE DATABASE IF NOT EXISTS workshop_tracker_db;
USE workshop_tracker_db;

CREATE TABLE workshops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending'
);