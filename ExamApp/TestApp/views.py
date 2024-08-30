from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from TestApp.models import *
from datetime import datetime
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

def welcome(request):
    
    return render(request, 'welcome.html')

def candidateRegistrationForm(request):
    if request.method =='POST':
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        candidate = Candidate.objects.create(
            username = username,
            name = name,
            password = password,
            test_attmpted = 0,
            points = 0
        )

        candidate.save()

        return redirect('login')
    res=render(request,'registration_form.html')
    return res

# def candidateRegistration(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         #Check if the user already exists
#         if(len(Candidate.objects.filter(username=username))):
#             userStatus=1
#         else:
#             candidate=Candidate()
#             candidate.username=username
#             candidate.password=request.POST['password']
#             candidate.name=request.POST['name']
#             candidate.save()
#             userStatus=2
#     else:
#         userStatus=3 #Request method is not POST
#     context={
#         'userStatus':userStatus
#     }
#     res=render(request,'registration.html',context)
#     return res

def loginView(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        candidate=Candidate.objects.filter(username=username,password=password)
        if len(candidate)==0:
            loginError="Invalid Username or Password"
            res=render(request,'login.html',{'loginError':loginError})
        else:
            #login Success
            request.session['username']=candidate[0].username
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        res=render(request,'login.html')
    return res

@login_required(login_url='/login/')
def candidateHome(request):
    c_username = request.session.get('username')
    candidate = Candidate.objects.get(pk=c_username)
    return render(request,'home.html', {'candidate': candidate})

@login_required(login_url='/login/')
def testPaper(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    #fetch question from database table
    n=int(request.GET['n'])
    question_pool=list(Question.objects.all())
    random.shuffle(question_pool)
    questions_list=question_pool[:n]
    context={'questions':questions_list}
    res=render(request,'test_paper.html',context)
    return res

@login_required(login_url='/login/')
def calculateTestResult(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    total_attempt=0
    total_right=0
    total_wrong=0
    c_datetime = datetime.now()
    c_date = c_datetime.date()
    c_time = c_datetime.time()
    qid_list=[]
    for k in request.POST:
        if k.startswith('qno'):
            qid_list.append(int(request.POST[k]))
    for n in qid_list:
        question=Question.objects.get(qid=n)
        try:
            if question.ans==request.POST[f'q{question.qid}']:
                total_right+=1
            else:
                total_wrong+=1
            total_attempt+=1
        except:
            pass
    points=total_right*10
    #store result in Result Table
    result=Result()
    result.username=Candidate.objects.get(username=request.session['username'])
    result.attempt=total_attempt
    result.date = c_date
    result.time = c_time
    result.right=total_right
    result.wrong=total_wrong
    result.point=points
    result.save()
    
    #update candidate table
    candidate=Candidate.objects.get(username=request.session['username'])
    candidate.test_attmpted+=1
    candidate.points+=result.point
    candidate.save()
    return redirect('result')

@login_required(login_url='/login/')
def testResultHistory(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")

    candidate=Candidate.objects.filter(username=request.session['username'])
    results=Result.objects.filter(username_id=candidate[0].username)
    context={'candidate':candidate[0],'results':results}
    res=render(request,'candidate_history.html',context)
    return res

@login_required(login_url='/login/')
def showTestResult(request):
    if 'username' not in request.session.keys():
        res=HttpResponseRedirect("login")
    #fetch latest result from Result table
    result=Result.objects.filter(resultid=Result.objects.latest('resultid').resultid,username_id=request.session['username'])
    context={'result':result}
    res=render(request,'show_result.html',context)
    return res

@login_required(login_url='/login/')
def logoutView(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')
