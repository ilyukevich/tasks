from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView

from .forms import TaskCreateForm
from .models import Task


class Home(CreateView):
    """Form for adding a task"""

    template_name = 'deals/home.html'
    form_class = TaskCreateForm
    success_url = reverse_lazy('deals:task_added')


class TaskList(LoginRequiredMixin, ListView):
    """List of all available tasks"""

    login_url = '/admin/login/'
    model = Task
    template_name = 'deals/task_list.html'


class TaskDetail(LoginRequiredMixin, DetailView):
    """Assignment in detail"""

    login_url = '/admin/login/'
    model = Task
    template_name = 'deals/task_detail.html'


class TaskAddSuccess(TemplateView):
    """Task added successfully"""

    template_name = 'deals/added.html'
