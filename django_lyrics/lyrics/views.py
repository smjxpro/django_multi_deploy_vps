from django.shortcuts import render, get_object_or_404

from lyrics.models import Lyric


def index(request):
    lyrics = Lyric.objects.all()

    context = {
        'lyrics': lyrics,
        'title': 'Lyrics'
    }

    return render(request, 'lyrics/index.html', context)


def details(request, pk):
    lyric = get_object_or_404(Lyric, pk=pk)

    context = {
        'lyric': lyric,
    }

    return render(request, 'lyrics/details.html', context)
