from django.shortcuts import render,redirect
from .forms import AccountRegistrationForm
from django.contrib import messages
from django.views import View
from main.models import UserProfile

# Create your views here.


class AccountRegisterView(View):
    
    def get(self, request):
        form = AccountRegistrationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            UserProfile.objects.get_or_create(user=user)
            messages.success(request, 'User has been registered.')
            return redirect('login')  # Redirect to the login page or another appropriate page

        return render(request, 'registration/signup.html', {'form': form})
    
def front(request):
    return render(request, 'frontpage/frontpage.html')
