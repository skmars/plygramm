from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    AccountUpdateView,
    ControllQuestionUpdateView,
    SignUpView,
    StudentInfoView,
    TeacherInfoView,
)

app_name = "users"

urlpatterns = [
    path("sign_up/", SignUpView.as_view(), name="signup"),
    path("teacher_info/<int:teacher_id>/", TeacherInfoView.as_view(), name="teacher_info"),
    path("student_info/<int:student_id>/", StudentInfoView.as_view(), name="student_info"),
    path("account_update/<int:account_id>/", AccountUpdateView.as_view(), name="account_update"),
    path(
        "change_question/<int:controll_qusetion_id>",
        ControllQuestionUpdateView.as_view(),
        name="change_question",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
