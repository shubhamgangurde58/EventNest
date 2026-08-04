# EventNest - College Event Registration & Management System

# About the Project

**EventNest** is a web-based **College Event Registration and Management System** developed using **Python**, **Django**, **HTML**, **CSS**, **Bootstrap**, and **SQLite** as part of my MCA learning journey. The application is designed to simplify the process of creating, managing, and registering for college events through an easy-to-use web interface.

The system allows administrators to create and manage events, while students can browse available events and register online. It provides an organized platform for handling event details, participant registrations, and event schedules efficiently.


# Project Objectives

* Develop a centralized platform for college event management.
* Simplify the event registration process.
* Learn full-stack web development using Django.
* Implement CRUD operations using Django ORM.
* Understand MVC/MVT architecture and database management.

# Features

# User Authentication

* User Registration
* User Login
* Secure Authentication
* Logout Functionality

# Event Management

* Add New Event
* View Event Details
* Update Event Information
* Delete Events
* Search Events
* Event Categories
* Event Status Management

# Registration Module

* Online Event Registration
* Participant Information Management
* Seat Availability Tracking
* Registration Deadline Validation
* Duplicate Registration Prevention

# Dashboard

* View All Events
* Display Event Statistics
* Quick Navigation
* Event Management Dashboard

# Media Management

* Event Banner Upload
* Image Storage
* Media File Handling

# Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Django       | Web Framework        |
| HTML5        | Frontend Structure   |
| CSS3         | Styling              |
| Bootstrap 5  | Responsive UI        |
| SQLite       | Database             |
| Django ORM   | Database Operations  |
| Git & GitHub | Version Control      |
| Render       | Deployment Platform  |

# Project Architecture

```text
                    User
                      │
                      ▼
              Django Web Application
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
 Authentication    Event Module   Registration Module
      │               │               │
      └───────────────┼───────────────┘
                      │
                      ▼
                 Django ORM
                      │
                      ▼
                SQLite Database
```

The application follows Django's **MVT (Model-View-Template)** architecture, where models manage the database, views handle business logic, and templates provide the user interface.

# Project Modules

# Accounts Module

* User Registration
* Login
* Logout
* Authentication

# Events Module

* Add Event
* View Events
* Edit Event
* Delete Event
* Search Events

# Registration Module

* Register for Events
* Store Participant Details
* Seat Management
* Registration Validation

# Dashboard Module

* Event Overview
* Quick Navigation
* Event Statistics

# Project Structure

```text
EventNest
│
├── accounts
├── dashboard
├── events
├── registrations
├── templates
├── static
│   ├── css
│   ├── js
│   └── images
├── media
├── EventNest
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

# Application Workflow

1. User creates an account or logs into the system.
2. Administrator creates and manages college events.
3. Students browse available events.
4. Students view complete event information.
5. Students register for their preferred events.
6. The system validates seat availability.
7. Registration details are stored in the database.
8. Administrators can monitor and manage all events and registrations.

# Django Concepts Covered

* Django MVT Architecture
* Models
* Views
* Templates
* URL Routing
* Forms
* Authentication
* Static Files
* Media Files
* Django ORM
* CRUD Operations
* File Upload
* Database Relationships

# Getting Started

# Prerequisites

* Python 3.x
* Django
* Git
* VS Code or PyCharm

# Installation

Clone this repository:

```bash
git clone https://github.com/shubhamgangurde58/EventNest.git
```

Navigate to the project directory:

```bash
cd EventNest
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Python Programming
* Django Framework
* Django ORM
* CRUD Operations
* Authentication System
* Database Design
* HTML & CSS
* Bootstrap
* SQLite Database
* File Upload Handling
* Git & GitHub
* Web Application Deployment

---

## Future Improvements

I plan to enhance this project by adding:

* Email Notifications
* QR Code-Based Event Entry
* Event Certificates
* Payment Gateway Integration
* Admin Analytics Dashboard
* Attendance Tracking
* Event Feedback System
* REST API Development
* PostgreSQL Database Support
* Docker Deployment

---

## Author

**Shubham Santosh Gangurde**

MCA Student
Aspiring Java Full Stack Developer

GitHub: **https://github.com/shubhamgangurde58**


## Note

This project was developed as part of my MCA learning journey to understand full-stack web development using the Django framework. It demonstrates authentication, event management, online registration, database operations, file handling, and responsive web design in a real-world college event management system. Working on this project strengthened my understanding of Django, Python, database design, and modern web application development.

If you find this project useful, consider giving it a **Star** on GitHub.
