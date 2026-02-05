# 📦 Itemize

Itemize is a simple home-lab inventory management web application built with Django. It allows you to store, organize, and manage all items you own in one place — including images, descriptions, purchase info, warranty, and location.

Designed to run efficiently on a Raspberry Pi and easily deployable using Docker.

---

## 🚀 Features

- Add, edit, view, and delete items (CRUD)
- Categories for organizing items
- Upload item images
- Quantity tracking
- Warranty expiry tracking
- Simple sketch-style UI
- SQLite database (lightweight and fast)
- Dockerized for easy deployment

---

## 🛠 Tech Stack

- Python 3.13
- Django 6.x
- SQLite
- HTML / CSS / Bootstrap
- Docker & Docker Compose

---

## 📂 Project Structure

```
Itemize2/
├── core/
├── items/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .gitignore
```

---

## ⚙️ Local Development Setup (Without Docker)

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
```
http://127.0.0.1:8000
```

---

## 🐳 Run With Docker (Recommended)

### Build & Start

```bash
docker compose build
docker compose up
```

### Run Migrations

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Open:
```
http://localhost:8000
```

---

## 🍓 Raspberry Pi Deployment

Itemize works on Raspberry Pi 4/5 (ARM64).

```bash
sudo apt update
sudo apt install docker.io docker-compose -y

git clone <your-repo-url>
cd Itemize2

docker compose build
docker compose up
```

---

## 🔐 Environment Variables (Optional)

Create `.env` file:

```
DEBUG=True
SECRET_KEY=change-me
```

---

## 🧭 Roadmap

- Search & filter items
- Pagination
- User authentication
- Soft delete / recycle bin
- Backup & restore system
- Nginx + Gunicorn production stack

---

## 👤 Author

Mohammed Alghamdi

---

## ⭐ Why Itemize?

Itemize is built as a learning-focused homelab project that demonstrates real-world Django architecture, Docker deployment, and clean UI design — while being genuinely useful for personal
