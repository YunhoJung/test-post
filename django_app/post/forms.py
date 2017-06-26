from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'photo',
            'comment'
        ] # 모델에 있는 것들을 여기에 쓰면 쉽게 사용할 수 있다 !. db에 영향을 안줌. 굳이 사용하는 이유는 모델만들 때 용이하다. 쉽다.