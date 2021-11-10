from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from Bets.models import Bets
from Users.models import MyUser
from Users.forms import EditProfileForm
from django.views.generic import View

# Home View when logged in


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        bets = Bets.objects.all().order_by('-posted_at')
        return render(request, 'homepage.html', {'bets': bets})


# Create Edit profile View


class EditProfile(LoginRequiredMixin, View):
    def get(self, request, id):
        profile = MyUser.objects.get(id=id)
        if request.user.id == id:
            form = EditProfileForm(initial={
                'password': profile.password
            })
            return render(request, 'generic_form.html', {'form': form})
        else:
            return render(request, 'no_access.html')

    def post(self, request, id):
        profile = MyUser.objects.get(id=id)
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.password = data['password']
            profile.prof_pic = data['prof_pic']
            profile.save()
            return HttpResponseRedirect(reverse('profile', args=(id,)))
        else:
            return render(request, 'server_err500.html')
