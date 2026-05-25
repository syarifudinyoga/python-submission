from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice, Submission


def submit(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        choice_id = request.POST.get("choice")
        selected_choice = get_object_or_404(
            Choice,
            id=choice_id
        )

        Submission.objects.create(
            username=request.POST.get("username"),
            question=question,
            choice=selected_choice
        )

        return redirect(
            "show_exam_result",
            submission_id=question.id
        )

    context = {
        "question": question
    }

    return render(
        request,
        "submit.html",
        context
    )


def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission,
        id=submission_id
    )

    is_correct = submission.choice.is_correct

    context = {
        "submission": submission,
        "is_correct": is_correct
    }

    return render(
        request,
        "exam_result.html",
        context
    )