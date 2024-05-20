from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'paginas/index.html')

def sobred(request):
    return render(request, 'sobre/index.html')