# 🧘‍♂️ Fitness Studio Booking API

A simple Django-based RESTful API that allows users to:

- View available fitness classes (Yoga, Zumba, HIIT, etc.)
- Book a spot in a class
- View their bookings by email

This project uses **Django**, **Django REST Framework**, and **SQLite**.

---

## 📁 Project Structure

```
fitness_booking/
├── booking/                  # App with models, views, serializers, urls
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
├── fitness_booking/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3                # SQLite database
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

If you don't have `requirements.txt`, manually install:

```bash
pip install django djangorestframework pytz
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

### ✅ Get All Upcoming Classes

**GET** `/classes/`

Returns:
```json
[
  {
    "id": 1,
    "name": "Yoga",
    "datetime": "2025-06-15T08:00:00Z",
    "instructor": "Instructor 1",
    "available_slots": 10
  }
]
```

### ✅ Book a Class

**POST** `/book/`

```json
{
  "class_id": 1,
  "client_name": "Arun",
  "client_email": "arun@example.com"
}
```

Returns:
```json
{
  "message": "Booking successful"
}
```

### ✅ Get Bookings by Email

**GET** `/bookings/?email=arun@example.com`

Returns:
```json
[
  {
    "class": "Yoga",
    "datetime": "2025-06-15T08:00:00+05:30",
    "instructor": "Instructor 1"
  }
]
```

---

## 🧠 Features

- Class-based views (can easily extend to generic views)
- Timezone-aware (IST-based, adjusts per user timezone)
- Handles overbooking, missing data, and email validation
- Easily extendable (e.g., to add authentication or payments)

---



## 🧑‍💻 Author

**Arun Kumar Reddy Padala**
