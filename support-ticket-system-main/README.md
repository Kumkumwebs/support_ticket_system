#  Support Ticket System REST API

A Django REST Framework based API to manage support tickets.  
Users can create and manage their own tickets. Admins can manage all tickets, update statuses, and delete them.


## Features

- Token-based authentication using Django's built-in User model
- Users can:
  - Register and authenticate
  - Create tickets
  - View and update their own tickets (if status is open)
- Admins can:
  - View all tickets
  - Update any ticket
  - Change ticket status
  - Delete any ticket

##  Technologies Used

- Django
- Django REST Framework
- Token Authentication

##  Setup Instructions

###  1. Clone or Download the Project

```bash
git clone https://github.com/Kumkumwebs/support-ticket-system
cd support-ticket-system

### 2. Install Dependencies

bash
pip install django djangorestframework


### 3. Add Apps in `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'tickets',
]

###  4. Run Migrations

bash
python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser
super user- user
password - 123456
python manage.py createsuperuser
###  6. Run Server
bash
python manage.py runserver

##  Token Authentication

### 1. Login to Get Token

**Endpoint:**
POST /api-token-auth/

**Request Body (raw JSON):**
{
  "username": "your_username",
  "password": "your_password"
}

**Response:**
{
  "token": "abc123tokenvalue..."
}

### 📥 2. Use Token in Headers for All API Requests:

Authorization: Token abc123tokenvalue...
Content-Type: application/json

---

## 📘 API Endpoints

| Method | Endpoint                      | Description                            |
|--------|-------------------------------|----------------------------------------|
| POST   | /api/tickets/                 | Create ticket (User)                   |
| GET    | /api/tickets/                 | View own tickets (User) / All (Admin)  |
| GET    | /api/tickets/<id>/            | View specific ticket                   |
| PUT    | /api/tickets/<id>/            | Update ticket (User if status=open)    |
| PATCH  | /api/tickets/<id>/status/     | Admin changes ticket status            |
| DELETE | /api/tickets/<id>/            | Admin deletes ticket                   |

---

## 👤 Roles and Permissions

| Action             | Role   | Permission Description                      |
|--------------------|--------|----------------------------------------------|
| Create ticket      | User   |  Can create own tickets                    |
| View ticket list   | User   |  Can view only own tickets                 |
| View ticket list   | Admin  |  Can view all tickets                      |
| Retrieve ticket    | User   |  Can retrieve own ticket                   |
| Retrieve ticket    | Admin  |  Can retrieve any ticket                   |
| Update ticket      | User   |  If ticket is "open" and created by user   |
| Update ticket      | Admin  |  Can update any ticket                     |
| Change status      | Admin  |  Can change any ticket's status            |
| Delete ticket      | Admin  |  Can delete any ticket                     |

---

## Testing in Postman

1. Login and get token from /api-token-auth/
2. Use token in headers: Token f531839b8286fffdf87284578910edbf8833e859

Authorization:Token f531839b8286fffdf87284578910edbf8833e859
Content-Type: application/json

3. Test all APIs (Create, Get, Update, Patch, Delete)



## Folder Structure

support_ticket_system/
├── manage.py
├── support_system/
│   └── settings.py, urls.py
├── tickets/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
├── db.sqlite3
└── README.md


##  Developed By

Kumkum Maurya  
Lucknow, India
