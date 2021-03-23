from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "title": util.get_title(entry),
        "entry": util.get_entry(entry)
    })    

def search(request, entry):
    return render(request, "encyclopedia/search.html", {
        "q": util.search(entry)
    })

    