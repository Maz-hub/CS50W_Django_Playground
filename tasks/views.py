from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse




class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=3)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    # render a page that displays a list of all of my tasks
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# add function to add a new task
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })