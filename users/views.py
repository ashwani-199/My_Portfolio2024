from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)
        messages.success(request, "Contact form is submitted successfully.")  # ignored
        contact.save()
        return redirect('index')
        
    return render(request, 'index.html')

