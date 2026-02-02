from django.shortcuts import get_object_or_404, redirect, render
from contacts import models

# Create your views here.
def read_contacts(request):
    if request.method == 'GET':
        contacts = models.Contact.objects.all()
        return render(request, 'contacts.html', {'contacts': contacts})
   



def create_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        contact = models.Contact(
            name = name,
            email = email,
            phone_number = phone_number
        )
        
        contact.save()
        return redirect('read_contacts')
    
def update_contact(request, id):
    contact = get_object_or_404(models.Contact, id=id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        contact.name = name
        contact.email = email
        contact.phone_number = phone_number

        contact.save()
        return redirect('read_contacts')
    
    return render(request, 'contacts.html', {'contact': contact})


def delete_contact(request, id):
    contact = get_object_or_404(models.Contact, id=id)
    contact.delete()
    return redirect('read_contacts')