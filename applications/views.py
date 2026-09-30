from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView
from .models import Post

# Create your views here.
def index(request):
    return render(request, "applications/index.html", {})

class apps(generic.ListView):
    # Get application data from database
    model = Post
    template_name = "applications/apps.html"
    context_object_name = "applications"

    def get_queryset(self):
        return Post.objects.all().order_by("-posted_date")
