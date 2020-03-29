from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError

from book01.models import UserInfo


class UserReg(forms.Form):
    name = forms.CharField(
        min_length=4,
        label='用户名',
        error_messages={
            'required': '用户名不能为空',
            'min_length': '用户名不能少于4位'
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        min_length=8,
        label='密码',
        error_messages={'required': '需要填写密码', 'min_length': '密码必须大于8位'},
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            },
        ),
    )
    r_password = forms.CharField(
        min_length=8,
        label='重复密码',
        error_messages={
            'required': '重复填入密码',
            'min_length': '密码必须大于8位',
        },
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            },
        ),
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'required': '邮箱必填',
        },
        widget=widgets.EmailInput(
            attrs={
                'class': 'form-control',
            },
        )
    )
    tel = forms.CharField(
        max_length=3,
        label='手机号码',
        error_messages={
            'required': '手机号码是必填的',
            'min_length': '手机号必须大于3位',
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    def clean_name(self):
        val = self.cleaned_data.get('name')
        ret = UserInfo.objects.filter(name=val)
        if not ret:
            return val
        else:
            raise ValidationError('该用户已注册')

    def clean(self):
        pwd1 = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('r_password')
        if pwd1 and pwd2:
            if pwd1 == pwd2:
                return self.cleaned_data
            else:
                raise ValidationError('两次密码不一致!')
        else:
            return self.cleaned_data
