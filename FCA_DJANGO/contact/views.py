from django.shortcuts import render
from .forms import contactUs
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = contactUs(request.POST)
        if form.is_valid():
            myform = form.save()
            return render(request, 'success.html')
    else:
        form = contactUs

    context = {'form' : form}
    return render(request, 'contact.html', context)