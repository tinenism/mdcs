from django.db import models
from django.contrib.auth.models import User


    
# Question Model

class Question(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    tags=models.TextField(default='')
    
    def __str__(self):
        return self.title
        
# Answer Model

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.detail
    
# Comment 

class Comment(models.Model):
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    comment=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)
    
# UpVote

class UpVote(models.Model):
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_user')
    
# DownVote

class DownVote(models.Model):
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_user')



class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    # picture = models.ImageField(upload_to='uploads/profile_pictures',default='uploads/profile_pictures/default.png',blank=True)
    # TOM EDIT
