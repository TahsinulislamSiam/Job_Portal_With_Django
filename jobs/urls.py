from django.urls import path

from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    MyJobListView,
    apply_to_job,
    MyApplicationListView,
    register,
)

urlpatterns = [

    path(
        '',
        JobListView.as_view(),
        name='job_list'
    ),
    path(
    'register/',
    register,
    name='register'
   ),

    path(
        'job/<int:pk>/',
        JobDetailView.as_view(),
        name='job_detail'
    ),

    path(
        'job/create/',
        JobCreateView.as_view(),
        name='job_create'
    ),

    path(
        'job/<int:pk>/update/',
        JobUpdateView.as_view(),
        name='job_update'
    ),

    path(
        'job/<int:pk>/delete/',
        JobDeleteView.as_view(),
        name='job_delete'
    ),

    path(
        'my-jobs/',
        MyJobListView.as_view(),
        name='my_jobs'
    ),

    path(
        'job/<int:pk>/apply/',
        apply_to_job,
        name='apply_to_job'
    ),

    path(
        'my-applications/',
        MyApplicationListView.as_view(),
        name='my_applications'
    ),
]