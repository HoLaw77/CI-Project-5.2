from django.shortcuts import render

# Create your views here.

def show_home(request):
    """
    Return index.html
    """
    return render (request, 'home/index.html')