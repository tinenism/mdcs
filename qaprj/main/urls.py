from django.urls import path
from .import views
from .views import ProfileView

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/',views.home, name='home'),
    path('detail/<int:id>', views.detail,name='detail'),
    path('save-comment', views.save_comment,name='save-comment'),
    path('save-upvote', views.save_upvote,name='save-upvote'),
    path('save-downvote', views.save_downvote,name='save-downvote'),
    # Ask QUestion
    path('ask-question',views.ask_form,name='ask-question'),
    # Tag Page
    path('tag/<str:tag>',views.tag,name='tag'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
