from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name, receiver):
    """
    Creating message subject and sender
    """
    subject = 'Welcome to the Moringa Tribune NewsLetter'
    sender = 'uzalendoproject@gmail.com'

    """
    Passing in the context variables
    """
    text_content = render_to_string('email/newsemail.txt', {"name": name})
    html_content = render_to_string('email/newsemail.html', {"name": name})

    message = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    message.attach_alternative(html_content, 'text/html')
    message.send()
