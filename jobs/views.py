from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Job, Application
from .forms import Jobform


# Create your views here.


class JobListView(ListView):
    model=Job
    template_name = '/jobs/templates/job_list.html'
    context_object_name = 'all_jobs'

class JobDetailView(DetailView):
    model=Job
    template_name='/jobs/templates/job_detail.html '
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['already_applied']= Application.objects.filter(
                job=self.object, applicant = self.request.user
            ).exists()
        return context
    
class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = Jobform
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = Jobform
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)
    
class MyJobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/my_jobs.html'
    context_object_name = 'my_jobs'

    def get_queryset(self):
        return Job.objects.filter(
            posted_by=self.request.user
        ).order_by('-date_posted')
    
    
@login_required
def apply_to_job(request, pk):

    job = get_object_or_404(Job, pk=pk)

    # Check whether user already applied
    already_applied = Application.objects.filter(
        job=job,
        applicant=request.user
    ).exists()

    if already_applied:
        return redirect('job_detail', pk=job.pk)

    # Create application
    Application.objects.create(
        job=job,
        applicant=request.user
    )

    return redirect('my_applications')




class MyApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'jobs/my_applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        ).select_related('job').order_by('-date_applied')