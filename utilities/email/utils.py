from django.core.mail import send_mail

from main.settings import EMAIL_HOST_USER


def send_email(subject: str, message, recipient_list: list):
    try:
        return send_mail(subject, message, EMAIL_HOST_USER, recipient_list)
    except:
        return False
