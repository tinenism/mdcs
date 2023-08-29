from django.shortcuts import render,redirect
from .forms import AccountRegistrationForm
from django.contrib import messages
from django.views import View

# Create your views here.


class AccountRegisterView(View):
    
    def get(self, request):
        form = AccountRegistrationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been registered.')
            return redirect('login')  # Redirect to the login page or another appropriate page

        return render(request, 'registration/signup.html', {'form': form})
    
def front(request):
    return render(request, 'frontpage/frontpage.html')
