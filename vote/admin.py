from django.contrib import admin
from vote.models import Candidates

# Register your models here.

@admin.register(Candidates)
class CandidatesAdmin(admin.ModelAdmin):
	list_display = ('concept', 'logo')

