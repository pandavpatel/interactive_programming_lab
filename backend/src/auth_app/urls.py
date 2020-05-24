from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomPasswordChangeView, after_login

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='auth_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(template_name='auth_app/password_change.html',
                                                              success_url='/logout/'), name="password_change"),
    path('after-login/', after_login, name='after-login'),
]
