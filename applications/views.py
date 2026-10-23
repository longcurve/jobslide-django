from django.conf.locale import el
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, User
from .forms import NewApplicationForm
from django.shortcuts import render

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
        user = User.objects.filter(user=request.user)
        return Post.objects.all().filter(user=user).order_by("-posted_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applications"] = Post.objects.all().order_by("-posted_date")
        return context

def newapp(request):
    if request.method == "POST":
        #submit the application data
        form = NewApplicationForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database
            application = Post(
                user=request.user,
                application_date=form.cleaned_data["application_date"],
                status=form.cleaned_data["status"],
                position=form.cleaned_data["position"],
                min_salary=form.cleaned_data["min_salary"],
                max_salary=form.cleaned_data["max_salary"],
                contact_name=form.cleaned_data["contact_name"],
                contact_phone=form.cleaned_data["contact_phone"],
                company_location=form.cleaned_data["company_location"],
                company_name=form.cleaned_data["company_name"],
                resume=form.cleaned_data["resume"]
            )
            application.save()
            return HttpResponseRedirect("/applications")  # Redirect to the applications page after successful submission
        else:
            # If the form is not valid, render the form with error messages
            context = {}
            context['form'] = form
            return render(request, "applications/newapp.html", context)
    else:
        context = {}
        context['form'] = NewApplicationForm()
        return render(request, "applications/newapp.html", context)