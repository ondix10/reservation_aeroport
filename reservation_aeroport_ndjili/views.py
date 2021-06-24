from django.shortcuts import render


def index(request):
    
    return render(request, './index.html')

def reservation(request):
    
    return render(request, './reservation.html')