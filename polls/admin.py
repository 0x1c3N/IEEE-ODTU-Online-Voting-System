from django.contrib import admin

from .models import Question, Choice, Voter

# Register your models here.

class InLineChoice(admin.TabularInline):
    model = Choice
    extra = 1
    fieldsets = (
        (None,{'fields': ('choice_text','birinci','ikinci','ucuncu','dorduncu','besinci','altinci','yedinci','image','votes','negativevotes','imagename')
        }),
    )
    readonly_fields = ['votes','negativevotes']




class QuestionAdmin(admin.ModelAdmin):
    inlines = [InLineChoice]
    fieldsets = (
        (None, {'fields': ('question_text','date','totalvote', 'is_active')
        }),
    )
    list_filter = ('question_text', 'date')
    readonly_fields = ['totalvote']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Voter)
