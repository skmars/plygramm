from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
class LogInView(LoginView):
    template_name = "portal/authentication/log_in.html"
    fields = ["nickname", "password"]
    redirect_authenticated_user = True


class LogOutView(LogoutView):
    """
    default logout view
    """
