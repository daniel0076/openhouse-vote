from django.forms import ModelForm
from . import models

class CandidateForm(ModelForm):
	class Meta:
		model=models.Candidates
		fields='__all__'


