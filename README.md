# Django-Authentication-and-Authorization-App

## Description

> A Django-based authentication system with custom user management, including features like registration, login, password management, and email verification.

## Features

- Custom user model
- Email verification
- Password reset and change functionality
- OTP-based user registration

## Installation

### Prerequisites

- Python 3.12.4
- Django 5.0.7
- Dependencies listed in `requirements.txt`

### Setup

1. **Clone the repository**
   git clone https://github.com/wizzpradeep/Django-Authentication-and-Authorization-App
   cd Django-Authentication-and-Authorization-App

2. **Install dependencies**
   `pip install -r requirements.txt`

3. **Apply database migrations**
   `python manage.py makemigrations`
   `python manage.py migrate`

4. **Create a superuser (optional, for admin access)**
   `python manage.py createsuperuser`

5. **Configure Email Settings**
   `EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`
   `EMAIL_HOST = 'your_email_host'`  
   `EMAIL_PORT = your_email_port`  
   `EMAIL_USE_TLS = True`  
   `EMAIL_HOST_USER = 'your_email_host_user'` # Your email address
   `EMAIL_HOST_PASSWORD = 'your_email/app_host_password'` # Your email/app password

6. **Run the development server**
   `python manage.py runserver`
