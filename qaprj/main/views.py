from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Question, Answer, Comment, UpVote, DownVote, UserProfile
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import AnswerForm, QuestionForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.views import View
# Home Page

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(title__icontains=q).order_by('-id')
    else:
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).all().order_by('-id')
    paginator=Paginator(quests,3)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'main/home.html',{'quests':quests})

#Details

def detail(request,id):
    quest=Question.objects.get(pk=id)
    tags=quest.tags.split(',')
    answers=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            answer=answerData.save(commit=False)
            answer.question=quest
            answer.user=request.user
            answer.save()
            messages.success(request,'Answer has been submitted')
    return render(request, 'main/detail.html', {
        'quest': quest, 
        'tags':tags, 
        'answers':answers, 
        'answerform':answerform
        })
    
    #Save Comment
    
def save_comment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
    return JsonResponse({'bool':True})
#save upvote

def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=UpVote.objects.filter(answer=answer, user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
            answer=answer,
            user=user
        )
    return JsonResponse({'bool':True})
#savwDownvote

def save_downvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=DownVote.objects.filter(answer=answer, user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            DownVote.objects.create(
            answer=answer,
            user=user
        )
    return JsonResponse({'bool':True})

# Question Form 
def ask_form(request):
    form=QuestionForm
    if request.method=='POST':
        questForm=QuestionForm(request.POST)
        if questForm.is_valid():
            questForm=questForm.save(commit=False)
            questForm.user=request.user
            questForm.save()
            messages.success(request,'Question has been added.')
    return render(request,'main/ask-question.html',{'form':form})

# Questions according to tag
def tag(request,tag):
    quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(tags__icontains=tag).order_by('-id')
    paginator=Paginator(quests,10)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'tag.html',{'quests':quests,'tag':tag})


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
       
        # posts = Post.objects.filter(author=user).order_by('-created_on') tom configurations

        context = {
            'user': user,
            'profile': profile,
            # 'posts': posts
        }

        return render(request, 'main/profile.html', context)


