from django import forms
from .models import Adding,Tweet,Convert,Reader,Chat


class AddForm(forms.ModelForm):
	class Meta:
		model = Adding
		fields = ["Name","Marks"]
	def clean(self):
		pass

class TweetForm(forms.ModelForm):
 	class Meta:
 		model = Tweet
                fields = ['fullname','tweetcount']


class Converter(forms.ModelForm):
	amount = forms.IntegerField(required = True,label = 'value')
	class Meta:
		model=Convert
		fields=['convert_from','convert_to','amount']
	def clean(self):
		return self.cleaned_data

class reader(forms.ModelForm):
	class Meta:
		model = Reader
		fields = ['url']

class Chatroom(forms.ModelForm):
	class Meta:
		model = Chat
		fields = ["message"]


