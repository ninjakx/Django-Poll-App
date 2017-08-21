from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


def Index(request):
	
	questions = Question.objects.all()
	template = 'polls/index.html'
	context = {
		"questions": questions,
		
		}
	return render(request, template, context)


def Detail(request,question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
            'question': question,})


def Results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
            'question': question,})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error': "Plz select a choice.",
        })
    else:
        selected.votes += 1
        selected.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
