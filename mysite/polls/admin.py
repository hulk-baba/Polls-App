from django.contrib import admin

# Register your models here.
from .models import Question, Choice



# Modelling for Admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):

	fieldsets = [

		('Question Text' , {'fields': ['question_text']}),
		('Date Information' , {'fields':['pub_date'] , 'classes':['collapse']}),
		] 
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
