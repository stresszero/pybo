from django.db import models

# 질문 테이블


class Question(models.Model):
    subject = models.CharField(max_length=200)
    # 제목 200자 제한, 제한된 텍스트는 CharField
    content = models.TextField()
    # 제한없는 텍스틑 TextField
    create_date = models.DateTimeField()

    def __str__(self):  # id값 대신 제목을 표시할 수 있는 메서드
        return self.subject

# 답변 테이블


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 외부키할당=ForeignKey on_delete=models.CASCADE 는 답변과 연결된 질문이 삭제되면 답변도 함께 삭제된다는것
    content = models.TextField()
    create_date = models.DateTimeField()
