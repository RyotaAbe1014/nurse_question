from django.views.generic.list import ListView
from .models import Question

class QuestionView(ListView):
    model = Question
    template_name = 'question.html'

    def get_queryset(self):
        return Question.objects.order_by('?')[:5]