from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import PostForm, contactForm


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if request.POST.get('day_time') != "":
            instance.dayTime = request.POST.get('day_time')
        instance.save()
        messages.success(request, "Add Successful")
        return HttpResponseRedirect(instance.get_absolute_url())
    # if request.method == "POST":
    #     print(request.POST.get("title"))
    #     print(request.POST.get("content"))
    #     print(request.POST.get("mail"))
    context = {
        "form": form,
        "title": "Create Form",
    }

    return render(request, "create.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Details",
        "instance": instance
    }
    return render(request, "detail.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted ... ", extra_tags='delete')
    return redirect("posts:list")


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.dayTime = request.POST.get('day_time')
        print("instance: ", instance.dayTime)
        print("POST : ", request.POST.get('day_time'))
        instance.save()
        messages.success(request, "Saved ... ", extra_tags='some-tags')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Update",
        "instance": instance,
        "form": form,
    }
    return render(request, "create.html", context)


def post_list(request):
    querySet = Post.objects.all()
    context = {
        "object_list": querySet,
        "title": "Post List"
    }
    return render(request, "list.html", context)


def contact(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        # instance = form.save(commit=False)
        # print(form.cleaned_data)
        for key, value in form.cleaned_data.items():
            print(key,value)
            # print(form.cleaned_data.get(key))

        # print(form.cleaned_data.get("name"))
        # print(request.POST.get("name"))

    context = {
        "title": "Contact Form",
        "form": form
    }

    return render(request, "contact.html", context)
