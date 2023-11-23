from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):  # Stacked choices
    model = Choice
    extra = 3


# Change the admin options for a model
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"]}),
    # ]  # Make pub date come before question text

    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]  # User can select a filter to change what is displayed
    search_fields = ["question_text"]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)