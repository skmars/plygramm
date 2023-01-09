from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import ChangeControllQuestionForm, SignUpForm
from .models import Account, Student, Teacher


class SignUpView(SuccessMessageMixin, CreateView):
    form = SignUpForm
    success_message = "Congrats! You signed up successfully 🚀"
    success_url = reverse_lazy("authentication:log_in")
    template_name = "portal/sign_up.html"


class StudentInfoView(DetailView):
    model = Student
    template_name = "portal/accounts/account_info.html"

    def get_context_data(self, **kwargs):
        account = super(StudentInfoView, self).get_context_data(**kwargs)
        account["Account"] = Account.objects.filter(student=self.get_object())
        return account


class TeacherInfoView(DetailView):
    model = Teacher
    template_name = "portal/accounts/account_info.html"

    def get_context_data(self, **kwargs):
        account = super(TeacherInfoView, self).get_context_data(**kwargs)
        account["Account"] = Account.objects.filter(teacher=self.get_object())
        return account


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    fields = "__all__"
    template_name = "portal/accounts/account_info.html"


class ControllQuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form = ChangeControllQuestionForm
    fields = ["controll_question", "answer_controll_question"]
    template_name = "portal/accounts/update_controll_question.html"
