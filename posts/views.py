from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #return HttpResponseRedirect(instance.get_absolute_url())
    #if request.method == "post":
    #    print(request.post.get("content"))
    #    print(request.post.get("title"))

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post, id=id)
    context = {
    "title": instance.title,
    "instance": instance,
    #"pagedetail": pagedetail,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
    "object_list": queryset,
    "title": "list"
    }
    return render(request, "index.html", context)

#def post_update(request, id=None):
def post_update(request):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
    "title": instance.title,
    "instance": instance,
    "form": form
    }
    #edit_form = "post_form.html"
    #return render(request, edit_form, context)
    return render(request, "post_form.html")
#    return render(request, "index.html", context)

#def post_update(request, id=None):
#    obj = get_object_or_404(BlogPost, slug=slug)
#    form = PostForm(request.POST or None, instance=obj)
#    if form.is_valid():
#        form.save()
#    context = {"title": f"Update {obj.title}", "form": form}
#    return render(request, "post_form.html", context)
#    return HttpResponse("<h1>EDIT</h1>")


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messagges.success(request, "Successfully deleted")
    return redirect("posts:list")
