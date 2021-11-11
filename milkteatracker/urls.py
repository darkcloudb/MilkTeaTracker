"""milkteatracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Users import views as u_view
from Bets import views as b_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', b_view.HomeView.as_view(), name='homepage'),
    path('login/', u_view.LoginView.as_view()),
    path('signup/', u_view.SignUpView.as_view()),
    path('logout/', u_view.LogoutView.as_view()),
    path('profile/<int:id>/', b_view.EditProfile.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
