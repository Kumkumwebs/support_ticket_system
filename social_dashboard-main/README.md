
# 📊 Social Media Dashboard (Django + DRF)

A feature-rich social media dashboard built with Django, Django REST Framework, Bootstrap, and JavaScript. Users can register, create text-based posts, comment, like, manage their profile and social media handles.

---

## 🚀 Features

- ✅ User Authentication (Login, Register, Logout)
- ✅ Post Creation (Text-based posts)
- ✅ Like & Comment System
- ✅ Profile Picture Upload
- ✅ Edit Profile & Social Media Links
- ✅ Responsive Bootstrap UI
- ✅ RESTful API (DRF)
- ✅ Admin Panel Access
- ✅ Secure with CSRF Protection

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, Bootstrap, JavaScript (Fetch API)
- **Database**: SQLite (default, can be changed)
- **Auth**: Django built-in authentication system
- **Media Storage**: Local media folder (for profile pictures)

---

## 📁 Project Structure

social_dashboard/
├── dashboard/
│   ├── migrations/
│   ├── static/
│   │   └── js/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── forms.py
├── social_dashboard/
│   ├── settings.py
│   ├── urls.py
├── media/
├── manage.py
└── db.sqlite3

---

## 🧑‍💻 How to Run the Project

### 1. Clone the Repository

```bash
git clone  https://github.com/Kumkumwebs/social_dashboard.git
>>
PS D:\social_dashboard> 
cd social_dashboard
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Then open in browser: http://127.0.0.1:8000

---

## 🔒 Login Credentials

You can either:
- Register as a new user
- Or log in with the superuser you created


📝 API Endpoints

- `GET /api/posts/` – Get all posts
- `POST /api/posts/` – Create a post (authenticated)
- `POST /api/posts/{id}/like/` – Like a post
- `GET /api/comments/` – Get all comments
- `POST /api/comments/` – Add a comment (authenticated)


🙋‍♀️ Author

**Kumkum Maurya**  
Feel free to reach out for contributions or feedback.
