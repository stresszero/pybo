from django.urls import path

from . import views

app_name = "pybo"  # 다른 앱에서 같은 url 별칭을 쓸 경우 중복 방지
urlpatterns = [
    path('', views.index, name="index"),  # /pybo/는 index
    path('<int:question_id>/', views.detail, name="detail"),  # /pybo/2는 detail
    path('answer/create/<int:question_id>/',
         views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
