from django.shortcuts import render, get_list_or_404, get_object_or_404  # type: ignore
from django.http import HttpResponse # pyright: ignore[reportMissingModuleSource]
from django.http import Http404 # type: ignore
from .models import Question


def index(request):
    latest_question_list = get_list_or_404(
        Question.objects.order_by("pub_date")[:5]
    )
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)



def detail(request, question_id):
    # return HttpResponse(f"You're looking at question {question_id}.")
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question" : question,
    }
    return render(request, "polls/details.html", context)

def results(request, question_id):
    return HttpResponse(f"You're looking at the result of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

def hello(request):
    return HttpResponse("<p>Hello from Django!</p>")
