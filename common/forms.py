from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
    # UserCreationForm의 is_valid 함수는 폼에 위의 속성 3개가 모두 입력되었는지, 비밀번호1과 비밀번호2가 같은지,
    # 비밀번호의 값이 비밀번호 생성 규칙에 맞는지 등을 검사하는 로직을 내부적으로 가지고 있다.
