from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Post
from django.views import generic


# Create your views here.
def index(request):
    return render(request, "applications/index.html", {})

class apps(generic.ListView):
    # Get application data from database
    template_name = "applications/apps.html"
    context_object_name = "applications"

    def get_queryset(self):
        return Post.objects.all().order_by("-posted_date")
