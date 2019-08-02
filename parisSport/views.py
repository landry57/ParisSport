from django.shortcuts import render
def home(request):
    return render(request,'home.html')


def  about(request):
    return render(request,'pages/about.html')

def  handler404(request, exception):
   return render(request,'errors/404.html', {'error':exception} ,status=404)


def  handler405(request, exception):
   return render(request,'errors/405.html', {'error':exception} ,status=405)
