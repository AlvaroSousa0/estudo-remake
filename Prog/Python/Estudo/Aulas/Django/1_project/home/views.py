from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,
            'home/index.html',
            {
                'text':'Novo ola mudo from home',
                'title':'Home - Aprendendo Django - '
            },)