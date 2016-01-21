from django.shortcuts import render
from django.http import JsonResponse
from . import forms
from vote.models import Candidates
from django.core import serializers


# Create your views here.

#use admin
def addCandidates(request):
	if request.method =="POST":
		form=forms.CandidateForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()

	form=forms.CandidateForm()
	return render(request,'add.html',locals())

def view(request):
	objs=Candidates.objects.all()
	json_res= serializers.serialize('json', objs)
	print(json_res)

	return JsonResponse(json_res,safe=False)


	return render(request,'view.html',locals())
