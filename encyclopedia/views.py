from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random


app_name="wiki"

# Render the default page that shows the list of entries
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Render particular page that the user search fo it the search box
def search(request):
    if request.method == 'GET':
        # Define an empty list
        search = []
        entry = request.GET['q']

        # Search if the inputed char in any entry name
        for x in util.list_entries():
            if entry.upper() in x.upper():
                search.append(x)
    if search:            
        return render(request, "encyclopedia/index.html", {
            "entries": search
            })
    else:
        return render(request, "encyclopedia/notexist.html", {
            "content": "Page Not Found"
        })

# Render any page that select from the shown list
def select(request, name):
    try:
        # Convert the markdown input to html content
        output = Markdown().convert(util.get_entry(name))
        return render(request, "encyclopedia/title.html", {
            "title": name, "content": output
        })
    except:
        return render(request, "encyclopedia/notexist.html")


def add(request):
    return render(request, "encyclopedia/newpage.html")


def create(request):
    if request.method == 'POST':
        # Handel every entry by the user by it's own
        title = request.POST['title']
        content = request.POST['content']

    # If the page is already exist render this page
    if title in util.list_entries():
        return render(request, "encyclopedia/notexist.html", {
            "content": "Encyclopedia Already Exist"
        })
    else:
        # Save the title and the content using the save function from util file
        util.save_entry(title, content)

        markdowner = Markdown()
        output = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/title.html", {
            "title": title, "content": output
        })

def edit(request):
    if request.method == 'POST':
        edit_title = request.POST['title']
        edit_content = util.get_entry(request.POST['title'])

        return render(request, "encyclopedia/edit.html", {
        'title': edit_title, 'content': edit_content
        })


def random_page(request):
    # Return the name of an entry
    randompage = random.choice(util.list_entries())

    # Get the content of the page that randomly picked from random function
    output = Markdown().convert(util.get_entry(randompage))
    return render(request, "encyclopedia/title.html", {
        "title": randompage, "content": output
    })

def afteredit(request):
    if request.method == 'POST':
        old_title = request.POST["oldtitle"]
        new_title = request.POST["newtitle"]
        new_content = request.POST["newcontent"]

        util.save_entry(old_title, new_content)

    output = Markdown().convert(util.get_entry(old_title))
    return render(request, "encyclopedia/title.html", {
        'title': old_title, 'content': output
    })