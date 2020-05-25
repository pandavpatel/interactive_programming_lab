from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login


class CustomLoginView(LoginView):
    def form_valid(self, form):
        # Security check complete. Log the user in.
        auth_login(self.request, form.get_user())
        # Now check if user is required change password
        # If so redirect user to change password
        # This is just a hack. User is already logged in.
        # User can access everything without ever changing password.
        # But this would ask user to change password everytime after login,
        # until user actually changes password.
        if form.get_user().password_change_required:
            return HttpResponseRedirect(reverse('password_change'))
        else:
            return HttpResponseRedirect(self.get_success_url())


class CustomPasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        if self.request.user.password_change_required:
            self.request.user.password_change_required = False
            self.request.user.save()
        return super().form_valid(form)


@login_required
def after_login(request):
    # Need to add default_password field in User model
    # Set it when user is added first time
    # If not, force user to change password
    #
    return render(request, 'after_login.html')