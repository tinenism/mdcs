from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<int:id>', views.detail,name='detail'),
    path('save-comment', views.save_comment,name='save-comment'),
    path('save-upvote', views.save_upvote,name='save-upvote'),
    path('save-downvote', views.save_downvote,name='save-downvote')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
