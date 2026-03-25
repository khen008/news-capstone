# News Capstone Application

This project is a Django-based News Application developed as part of the bootcamp capstone task.

The application allows users to view news articles while administrators can create and manage articles through the Django admin panel.

The project demonstrates the use of:

- Git and GitHub for version control
- Sphinx for documentation
- Docker for containerization
- Django for the web framework

---

# Project Repository

GitHub Repository:
https://github.com/khen008/news-capstone

DockerHub Image:
https://hub.docker.com/r/khen008/news-capstone-app

---

# Running the Project Using Python Virtual Environment (venv)

## 1. Clone the repository

git clone https://github.com/khen008/news-capstone.git

cd news-capstone


## 2. Create a virtual environment

python -m venv venv


## 3. Activate the virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate


## 4. Install dependencies

pip install -r requirements.txt


## 5. Apply database migrations

python manage.py migrate


## 6. Run the development server

python manage.py runserver


## 7. Open the application

http://127.0.0.1:8000

---

# Running the Project Using Docker

## 1. Pull the Docker image

docker pull khen008/news-capstone-app


## 2. Run the container

docker run -p 8000:8000 khen008/news-capstone-app


## 3. Open the application

http://localhost:8000

---

# Admin Access

To create an admin user:

python manage.py createsuperuser

Then login at:

http://127.0.0.1:8000/admin

---

# Documentation

Sphinx documentation is included in the `docs` directory.

To build the documentation:

cd docs

make html

The generated documentation will be available in:

docs/build/html/index.html

---

# Technologies Used

- Python
- Django
- Docker
- Git
- GitHub
- Sphinx
