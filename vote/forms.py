from django.forms import ModelForm
from . import models

class CandidateForm(ModelForm):
	class Meta:
		model=models.Candidates
		fields='__all__'

class VoterForm(ModelForm):
	class Meta:
		model=models.Voter
		fields='__all__'
		exclude=['added']
	def __init__(self, *args, **kwargs):
			super(VoterForm, self).__init__(*args, **kwargs)
			self.fields['identity'].widget.attrs.update({
				'class': 'ui dropdown',
				'ng-model': 'form.identity',
				})
			self.fields['idno'].widget.attrs.update({
				'ng-model': 'form.idno',
				})
			self.fields['name'].widget.attrs.update({
				'ng-model': 'form.name',
				})
			self.fields['cellphone'].widget.attrs.update({
				'ng-model': 'form.cellphone',
				})
			self.fields['email'].widget.attrs.update({
				'ng-model': 'form.email',
				})

