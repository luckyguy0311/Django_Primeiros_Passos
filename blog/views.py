# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def blog(request):
    print("Blog")
    context = {
        'text': "Estou no Blog",
        'title': 'Blog'
    }
    return render(
        request,
        'blog/index.html',
        context=context
    )


def example(request):
    print("Blog")
    context = {
        'text': "Estou no Example",
        'title': "Example",
    }
    return render(
        request,
        'blog/example.html',
        context
    )
