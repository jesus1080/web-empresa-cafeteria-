from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email ', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Cafeteria: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["jesusruizv12@gmail.com"],
                reply_to=[email]
            )
            try:
                #Todo a ido bien, redirecionamos a OK 
                email.send()
                return redirect(reverse('contact')+"?ok")
                
            except:
                #Alogo no a ido bien, redireccionamos a Fail
                return redirect(reverse('contact')+"?Fail")
            
    return render(request, "contact/contact.html",{'form':contact_form})