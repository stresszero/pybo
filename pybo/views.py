from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    question_list = Question.objects.order_by(
        '-create_date')  # 질문 목록 데이터를 얻고 작성일시 역순으로 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):  # url 매핑시 저장된 question_id로 함수호출
    # question = Question.objects.get(id=question_id)
    # pk는 primary key, path에 없는 url 요청시 500 에러대신 404 에러 뜨게 만듬
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
