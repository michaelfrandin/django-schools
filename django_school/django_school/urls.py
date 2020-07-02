from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from classroom.views import classroom, students, teachers, quizes
from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'quizes', quizes.QuizesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
	path('admin/', admin.site.urls),
    path('', include('classroom.urls')),

    # path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]
