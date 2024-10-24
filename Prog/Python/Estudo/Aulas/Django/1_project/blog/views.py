from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render(request,
                   'blog/index.html',
                  {
                      'text':'Novo olá mundo from blog',
                      'title':'Blog - Aprendendo Django - '
                  })

def exemplo(request):
    return render(request,
                   'exemplo/index.html',
                  {
                      'text':'Novo olá mundo from exemplo',
                      'title':'Exemplo - Aprendendo Django - '
                  })