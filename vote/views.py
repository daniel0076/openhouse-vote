from django.shortcuts import render
from django.http import JsonResponse
from . import forms
from . import models
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
		objs=models.Candidates.objects.all()
		json_data= json.loads(serializers.serialize('json', objs))
		for d in json_data:
			count=models.Votes.objects.filter(vote_to_id=d['pk']).count()
			d['fields']['votes']=count
			print(d)
		res=dict()
		res['success']=True
		res['data']=json_data
		return JsonResponse(res)

	form=forms.VoterForm()
	return render(request,'view.html',locals())

@ensure_csrf_cookie
def vote(request):
	res=dict()
	res['success']=True
	data=json.loads(request.body.decode())
	formdata=data.get('userdata')
	form=forms.VoterForm(formdata)

	if form.is_valid():
		form.save()
		for vote in data.get('votes'):
			voter=models.Voter.objects.get(idno=formdata.get('idno'))
			candida=models.Candidates.objects.get(pk=vote)
			votes_to = models.Votes(voter=voter,vote_to=candida)
			votes_to.save()

	else:
		res['errors']=dict(form.errors.items())
		res['success']=False

	return JsonResponse(res)

