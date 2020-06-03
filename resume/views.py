from django.shortcuts import redirect, render
from .models import Document, Mails
from .forms import EmailForm
from django.core.mail import send_mail
from django.http import FileResponse
from django.core.mail import EmailMessage
from django.utils import timezone
from mySite.settings import MY_EMAIL
import mimetypes




def home(request, template='home.html'):
    return render(request, template, {'about':'nav__links__active'})

def resume(request, template='resume.html'):
    return render(request, template, {'resume':'nav__links__active'})

def projects(request, template='projects.html'):
    return render(request, template, {'projects':'nav__links__active'})

def contact(request, template='contact.html'):
    if request.method == "POST":
        form = EmailForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            email_object = Mails(name=name, email=email, subject=subject, message=message)
            email_object.save()

            # Send the email
            send_mail(
                name + ': ' + subject + ' ' + email,
                message,
                email,
                [MY_EMAIL]
            )
            return render(request, template, {'contact':'nav__links__active', 'name': name})
        else:
            return render(request, template, {'contact':'nav__links__active', 'fail': True})
    else:
        return render(request, template, {'contact':'nav__links__active'})

def download(request):
    code = request.GET.get('filename')
    if code == 'resume':
        fl_path = 'resume/static/docs/Vinay_Resume_PostGrad.pdf'
        response = FileResponse(open(fl_path, 'rb'))
    elif code == 'thesis':
        fl_path = 'resume/static/docs/GopalanVinay_FinalThesis.pdf'
        response = FileResponse(open(fl_path, 'rb'))
    else:
        fl_path = 'resume/static/docs/BERT_Fine_tuning_at_SemEval_2020_Task_9__Sentiment_Analysis_on_Code_Mixed_Tweets.pdf'
        response = FileResponse(open(fl_path, 'rb'))
    return response