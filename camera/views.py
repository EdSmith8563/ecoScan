from django.shortcuts import render

def camera(request):
    return render(request, 'camera.html')