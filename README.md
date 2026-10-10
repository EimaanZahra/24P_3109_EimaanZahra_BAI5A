Name: Eimaan Zahra
Roll No: 24P-3109
Section: BAI5A

GitHub Repository: https://github.com/EimaanZahra/24P_3109_EimaanZahra_BAI5A
Project Video: The demonstration video is included inside the submitted zip file.

--------------------------------------------------
Project: Workshop Tracker (Flask, MySQL, HTML/JS)
--------------------------------------------------

How to run the project:

1. Database Setup
- Open your MySQL command line.
- Create the database: CREATE DATABASE workshop_tracker_db;
- Use it: USE workshop_tracker_db;
- Create the table: CREATE TABLE workshops (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, status VARCHAR(50) DEFAULT 'Pending');

2. Backend Setup
- Open Git Bash and go to the backend folder: cd backend
- Activate the virtual environment: source venv/Scripts/activate
- Install the required files: pip install -r requirements.txt
- Open the .env file in the backend folder and put in your own MySQL password.
- Start the server: python app.py

3. Frontend Setup
- Open your regular Windows File Explorer.
- Go into the frontend folder.
- Double-click the index.html file to open the app in your browser.