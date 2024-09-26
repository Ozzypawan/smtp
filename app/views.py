# app/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
        
            
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, 
                ["ujinaparajuli57@gmail.com"],  
            )
            return render(request, 'app/success.html')
        
    return render(request, 'app/contact.html', {'form': form})

