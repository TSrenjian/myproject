from django import forms
from .models import Topic,Board,Post
from django.contrib.auth.models import User
#创建Topic的表单
#继承forms.ModelForm则需要 class Mate指明哪一个model，以及输入分别为哪一些字段。
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

#创建Post表单
class NewPostForm(forms.ModelForm):
    message = forms.CharField(
        widget= forms.Textarea(
            attrs={'row':5,'placeholder':'Writting your view!'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000'
    )
    class Meta:
        model = Post
        fields = ['message']

#创建登录表单
class UserForm(forms.Form):
    username = forms.CharField(
        label='Your UserName',
        help_text='The max length of the name is 6'
    )
    password = forms.CharField(
        label= 'your password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"})
    )
