from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

def send_verification_email(request, email, token):
    try:
        subject  = "Verify Your account"
        body = f'''
    Click link below...
    http://{get_current_site(request)}/email_verify/{token}
    '''
        sender = settings.EMAIL_HOST_USER
        receiver = [email,]
        try:
            send_mail(subject, body, sender, receiver)
        except Exception as e:
            print(e)
    except Exception as e:
            print(e)