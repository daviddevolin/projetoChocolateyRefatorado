from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Pacote

def home(request):
    return render (request, 'index.html')
    
def cadastro_pacote(request):
    if request.method == 'POST':
        #cadastrar pacote
        form = PostForm(request.POST)
        #pacote = form.save(commit=False)
        pacote = form.save()
        pacote.save()
        print(pacote.icon_URL)
    
    form = PostForm()
    pacotes = Pacote.object.all()
    contexto = {'form': form,
                'pacotes': pacotes}
    return render(request, 'cadastro_pacote.html',contexto )

def visualiza_pacote(request):
    pacotes = Pacote.object.all()
    
    contexto = {'pacotes': pacotes}
    
    return render(request, 'lista_pacotes.html', contexto)    

# Create your views here.

def listar_detalhes_pacote(request, id_pacote):
    pacote = Pacote.object.get(id_do_pacote = id_pacote)
    contexto = {'pacote': pacote}
    return render(request, 'lista_detalhe_pacote.html', contexto)