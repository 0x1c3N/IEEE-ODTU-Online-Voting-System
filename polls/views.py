from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Voter
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
# Create your views here.

def index(request):
    return render(request,"index.html")



def index1(request):
    questions = Question.objects.all().filter(is_active=True).order_by('-date')


    context = {'questions':questions}
    return render(request,'polls.html',context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not question.is_active:
        raise Http404("Poll does not exist")

    return render(request, 'detail.html',{'question':question})



@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if Voter.objects.filter(questions_id=question_id, user_id=request.user.id).exists():
        return render(request, 'detail.html', {'question':question, 'error_message':'Daha önce oyladınız!!'})

    a = 1
    for i in question.choice_set.all():
        a +=1
    b = 1

    while b<a:
        try:
            if request.POST['choice{}'.format(b)] and request.POST['choicenegative{}'.format(b)]:
                return render(request, 'detail.html', {'question':question, 'error_message':'Hatalı Seçim Yaptınız!!'})
            else:
                b += 1
        except:
            b += 1

    b = 1

    while b<a:
        if "computer" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="cs").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
        elif "power" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="pes").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

        elif "robotics" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="ras").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
        elif "basın" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="basinik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1


                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
        elif "sistem" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="sistemik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

        elif "sponsorluk" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="sponsorlukik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
        elif "sosyal" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="sosyalik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
        elif "tanıtım" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="tanitimik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

        elif "yayın" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="yayinik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
        
        elif "kişisel" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="kisiselik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
           
        else:
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choice{}'.format(b)])
                    selected_choice.votes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

    b = 1

    while b<a:
        if "computer" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="cs").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

        elif "power" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="pes").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1     

        elif "robotics" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="ras").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1
        elif "basın" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="basinik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

        elif "sistem" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="sistemik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1     

        elif "sponsorluk" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="sponsorlukik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1              
        elif "sosyal" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="sosyalik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

        elif "tanıtım" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="tanitimik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1     

        elif "yayın" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="yayinik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1 
        elif "kişisel" in question.question_text.lower():
            try:
                if request.user.groups.filter(name="kisiselik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yeniyk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1                                                
        else:
            try:
                if request.user.groups.filter(name="ik").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b +=1

                elif request.user.groups.filter(name="yk").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=2
                    selected_choice.save()
                    b+=1

                elif request.user.groups.filter(name="üye").exists():
                    selected_choice = question.choice_set.get(pk=request.POST['choicenegative{}'.format(b)])
                    selected_choice.negativevotes +=1
                    selected_choice.save()
                    b+=1

                else:
                    return render(request, 'detail.html', {'question':question, 'error_message':'Oy verme hakkına sahip değilsiniz!!'})
            except:
                b+=1

    v = Voter(user=request.user, questions=question)
    v.save()
    messages.success(request,'Başarıyla Oy Kullandınız')

    if "basın" in question.question_text.lower():
        if request.user.groups.filter(name="basinik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yeniyk").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
            question.totalvote += 1
            question.save()
    elif "sistem" in question.question_text.lower():
        if request.user.groups.filter(name="sistemik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yeniyk").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
            question.totalvote += 1
            question.save()
    elif "sponsorluk" in question.question_text.lower():
        if request.user.groups.filter(name="sponsorlukik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yeniyk").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
            question.totalvote += 1
            question.save()
    elif "sosyal" in question.question_text.lower():
        if request.user.groups.filter(name="sosyalik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yeniyk").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
            question.totalvote += 1
            question.save()
    elif "tanıtım" in question.question_text.lower():
        if request.user.groups.filter(name="tanitimik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yeniyk").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
            question.totalvote += 1
            question.save()
    elif "yayın" in question.question_text.lower():
        if request.user.groups.filter(name="yayinik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yeniyk").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
            question.totalvote += 1
            question.save()
    elif "kişisel" in question.question_text.lower():
        if request.user.groups.filter(name="kisiselik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yeniyk").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="üye").exists() or request.user.groups.filter(name="yk").exists() or request.user.groups.filter(name="ik").exists():
            question.totalvote += 1
            question.save()
    else:
        if request.user.groups.filter(name="ik").exists():
            question.totalvote += 2
            question.save()
        elif request.user.groups.filter(name="yk").exists():
            question.totalvote += 2 
            question.save()
        elif request.user.groups.filter(name="üye").exists():
            question.totalvote += 1
            question.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

