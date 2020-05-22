from django.shortcuts import render, get_object_or_404

from poems.models import Poem


def index(request):
    poems = Poem.objects.all()

    context = {
        'poems': poems,
        'title': 'Poems',
    }

    return render(request, 'poems/index.html', context)

def details(request, pk):
    poem = get_object_or_404(Poem, pk=pk)

    context = {
        'poem': poem,
    }

    return render(request, 'poems/details.html', context)