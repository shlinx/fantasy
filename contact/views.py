from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.utils import timezone

from .forms import ContactForm
from .models import ContactRecord


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                submit(form.cleaned_data)
            except(TypeError, ValueError):
                return render(request, 'contact/contact.html', {
                    'form': form,
                    'message': '发生点小意外，请稍后再试。',
                    'message_type': 'bad'
                })
            else:
                return render(request, 'contact/contact.html', {
                    'message': '我们已经收到您的信息，感谢与我们联系。',
                    'message_type': 'good'
                })
        else:
            return render(request, 'contact/contact.html', {
                'form': form,
                'message': '请正确填写所需信息。',
                'message_type': 'bad'
            })
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form, 'message': None, 'message_type': None})


def submit(data):
    """
    Save it to record and send email.
    :param data:
    :return:
    """
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')
    name = data.get('name')

    record = ContactRecord(**data)
    record.created = timezone.now()
    record.save()

    text_content = 'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\n'\
        .format(name=name, email=email, subject=subject, message=message)
    template = get_template('contact/email.html')
    context = Context({
        'subject': subject,
        'message': message,
        'name': name,
        'email': email,
    })
    html_content = template.render(context)
    email = EmailMultiAlternatives(
        'FantasyNZ contact form submission',
        text_content,
        'no-reply@fantasynz.com',
        ['shawnxiaolin@gmail.com'],
        headers={'Reply-To': data.get('email')}
    )
    email.attach_alternative(html_content, 'text/html')
    email.send(fail_silently=True)

