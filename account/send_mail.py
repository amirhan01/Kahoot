from django.core.mail import send_mail


def send_confirmation_email(code, email):
    full_link = f'http://localhost:8000/account/active/{code}'
    send_mail(
        'Подтверждение почты',
        full_link,
        'shamuza0102@gmail.com',
        [email]
    )
