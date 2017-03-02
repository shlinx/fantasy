from django.shortcuts import render, redirect


def index(request):
    return render(request, 'contact/contact.html')


def submit(request):
    data = request.POST
    print(data)
    return render(request, 'contact/contact.html', {
        'message': '我们已经收到您的消息，感谢与我们联系。',
        'message_type': 'good'
    })
