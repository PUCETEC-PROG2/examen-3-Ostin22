from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render

from album_manager.forms import ArtistForm, DiscosForm
from .models import Discos, Artist


# Create your views here.
def index(request):
    discos = Discos.objects.order_by('genre')
    return render(request, 'index.html', {'discos': discos})

def add_artist(request):

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = ArtistForm()
    return render(request, 'artist_form.html', {'form': form})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists':artists})

def artist(request, artist_id):
    artist = Artist.objects.get(pk = artist_id)
    template = loader.get_template('artist_index.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))

def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('discos:artist_list')
    else:
        form = ArtistForm(instance=artist)
    return render (request, 'artist_form.html', {'form': form})
        
def delete_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    artist.delete()
    return redirect("discos:artist_list")

def disco(request, disco_id):
    disco = Discos.objects.get(pk = disco_id)
    template = loader.get_template('display_disco.html')
    context = {
        'disco': disco
    }
    return HttpResponse(template.render(context, request))


def add_disco(request):
    if request.method == 'POST':
        form = DiscosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('discos:index')
    else:
        form = DiscosForm()
    return render(request, 'disco_form.html', {'form': form})


def edit_disco(request, id):
    disco = get_object_or_404(Discos, pk = id)
    if request.method == 'POST':
        form = DiscosForm(request.POST, request.FILES, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = DiscosForm(instance=disco)
    return render (request, 'disco_form.html', {'form': form})
    

def delete_disco(request, id):
    disco = get_object_or_404(Discos, pk = id)
    disco.delete()
    return redirect("discos:index")