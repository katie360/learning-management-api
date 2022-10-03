from django.contrib import admin
from .models import Curriculum, Subject, Class, Resource, ResourceChapter, ResourcePlanBoost, ResourceTextbook, AskQuestion, AskQuestionAnswer

admin.site.register(Curriculum)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Resource)
admin.site.register(ResourceChapter)
admin.site.register(ResourcePlanBoost)
admin.site.register(ResourceTextbook)
admin.site.register(AskQuestion)
admin.site.register(AskQuestionAnswer)
