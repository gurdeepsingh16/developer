from django.shortcuts import render
from quiz_app.models import paper
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


# def paper_func(request):
#     right = paper.objects.all()

#     return render(request, 'quiz/paper.html', {'data': right})


def check_answer(request):
    score = 0
    wrong = 0
    correct = 0
    total = 0
    if request.method == 'POST':
        print(request.POST)
        questions = paper.objects.all()
        for q in questions:
            total += 1
            if q.right_answer == request.POST.get(q.questions):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        questions = paper.objects.all().order_by("?")
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'questions': questions
        }

        return render(request, 'quiz/result.html', context)
    else:
        questions = paper.objects.all().order_by("?")
        context = {
            'questions': questions
        }
        return render(request, 'quiz/paper.html', context)
