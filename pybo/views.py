from django.shortcuts import render
from .models import Question


def index(request):
    question_list = Question.objects.order_by(
        '-create_date')  # 질문 목록 데이터를 얻고 작성일시 역순으로 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
