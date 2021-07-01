from django.http.response import HttpResponse
from django.shortcuts import render
from random import randrange

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    entries = util.list_entries()
    if title in entries:
        return render(request, "encyclopedia/wiki.html", 
        {"text": markdown2.markdown(util.get_entry(title)), "title": title})
    else:
        return render(request, "encyclopedia/wiki.html", {"text": None, "title": title})

def search(request):
    entries = util.list_entries()
    term = request.POST["term"]
    if term in entries:
        return render(request, "encyclopedia/wiki.html", 
        {"text": markdown2.markdown(util.get_entry(term)), "title": term})
    search_list = []
    for item in entries:
        if term.lower() in item.lower():
            search_list.append(item)
    if search_list:
        return render(request, "encyclopedia/results.html", {"entries": search_list})
    else:
        return render(request, "encyclopedia/wiki.html", {"text": None, "title": term})

def new_entry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST["new_title"]
        content = request.POST["new_content"]
        if title in util.list_entries():
            return render(request, "encyclopedia/existing.html", {"title": title})
        else:
            util.save_entry(title, content)
            return wiki(request, title)

def random_entry(request):
    entries = util.list_entries()
    num = len(entries)
    entry = randrange(num)
    title = entries[entry]
    return wiki(request, title)

def edit(request):
    if request.method == "GET":
        title = request.GET["title"]
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {"content": content, "title": title})
    else:
        title = request.POST["title"]
        text = request.POST["new_content"]
        util.save_entry(title, text)
        return wiki(request, title)