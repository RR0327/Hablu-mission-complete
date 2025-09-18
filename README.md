## <h1 align="center">Hablu’s Heartbreak API</h1>

A Django REST Framework project to help "Hablu" level up in life — academically, socially, mentally, and professionally.

---

## Features Implemented (All 11 Missions)

| Phase     | Feature        | Endpoint             |
| --------- | -------------- | -------------------- |
| Academic  | Save CGPA      | `/api/cgpa/`         |
| Academic  | Learn Skills   | `/api/skills/`       |
| Academic  | Mood Tracker   | `/api/mood-checks/`  |
| Lifestyle | Run Tracker    | `/api/marathon/`     |
| Lifestyle | Outfit Tips    | `/api/outfit-tips/`  |
| Lifestyle | Gym Finder     | `/api/gym-friends/`  |
| Career    | Job Listings   | `/api/jobs/`         |
| Career    | Random Movie   | `/api/movies/`       |
| Fun       | Fun Fact       | `/api/fun-fact/`     |
| Social    | Study Group    | `/api/study-groups/` |
| Final     | Hero Dashboard | `/api/dashboard/`    |

---

## Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- Simple JWT + Djoser (Auth)
- SQLite (Default)
- TMDB API (for movie suggestion)

---

## Project Structure

```
hablu_project/
├── core/ # Main features
├── templates/ # For HTML forms (optional)
├── db.sqlite3
├── .env
├── requirements.txt
└── manage.py
```

---

## Setup Instructions

```
git clone <repo-url>
cd hablu_project
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
Create .env and add your values.
```

Then run:

```
python manage.py migrate
python manage.py runserver
```

_Auth Endpoints_

```
Use djoser + JWT:

POST /auth/users/ → Register

POST /auth/jwt/create/ → Login (returns tokens)

Use token in header: Authorization: Bearer <access_token>
```

# Credits

Built with using Django by **Md Rakibul Hassan**

CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast

[LinkedIn](https://www.linkedin.com/in/md-rakibul-hassan-507b00308)
[GitHub](https://github.com/RR0327)

Designed to help users visualize complex data through customizable heatmaps and track real-time weather conditions interactively.

## Special thanks to **Md Tahsin Azad Shaikat** for assistance with this project.

[LinkedIn](https://www.linkedin.com/in/mdtahsinazad020)
[GitHub](https://github.com/shaikat020)

# License

This project is open source and available under the MIT License.
