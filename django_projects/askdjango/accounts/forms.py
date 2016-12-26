from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import Profile


class SignupForm(UserCreationForm):
    phone = forms.CharField(label='휴대폰번호')
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'last_name', 'first_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        phone = self.cleaned_data.get('phone')
        address = self.cleaned_data.get('address')

        try:
            # Profile.objects.get(user=user) 와 동일
            user.profile.phone = phone
            user.profile.address = address
            user.profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=user, phone=phone, address=address)

        return user


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('땡~!!!')
        return answer

