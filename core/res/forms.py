from django.forms import ModelForm, Textarea
from .models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
            'message': Textarea()
        }
		labels = {
            'first_name': 'Name',
			'subject': 'Subject',
			'email': 'Email',
			'message': 'Message'
        }

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({'class': 'input-field'})
		self.fields['subject'].widget.attrs.update({'class': 'input-field'})
		self.fields['email'].widget.attrs.update({'class': 'input-field'})
		self.fields['message'].widget.attrs.update({'class': 'input-field'})