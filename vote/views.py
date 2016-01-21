from django.shortcuts import render
from django.http import JsonResponse
from . import forms
from vote.models import Candidates
from django.core import serializers
import json
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.

#use admin
def addCandidates(request):
	if request.method =="POST":
		form=forms.CandidateForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()

	form=forms.CandidateForm()
	return render(request,'add.html',locals())

@ensure_csrf_cookie
def view(request):

	if request.method =="POST":
		objs=Candidates.objects.all()
		json_data= serializers.serialize('json', objs)
		res=dict()
		res['success']=True
		res['data']=json.loads(json_data)
		return JsonResponse(res)

	form=forms.VoterForm()
	return render(request,'view.html',locals())

@ensure_csrf_cookie
def vote(request):
	json_data=json.loads(request.body.decode())
	print(json_data)
	res=dict()
	res['success']=True
	return JsonResponse(res)

