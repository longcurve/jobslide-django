from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.
def index(request):
    return render(request, "applications/index.html", {})


class apps(LoginRequiredMixin,ListView):
    # Get application data from database
    model = Post
    paginate_by = 50
    template_name = "applications/apps.html"
    context_object_name = "applications"

    def get_queryset(self):
        return Post.objects.all().order_by("-posted_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applications"] = Post.objects.all().order_by("-posted_date")
        return context
