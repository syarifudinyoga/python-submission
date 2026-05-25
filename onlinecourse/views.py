from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Course,
    Enrollment,
    Question,
    Choice,
    Submission
)


def submit(request, course_id):
    course = get_object_or_404(
        Course,
        pk=course_id
    )

    enrollment = get_object_or_404(
        Enrollment,
        user=request.user,
        course=course
    )

    if request.method == 'POST':

        selected_choices = request.POST.getlist(
            'choices'
        )

        submission = Submission.objects.create(
            enrollment=enrollment
        )

        for choice_id in selected_choices:
            choice = Choice.objects.get(
                pk=choice_id
            )

            submission.choices.add(choice)

        return redirect(
            'show_exam_result',
            course_id=course.id
        )

    context = {
        'course': course
    }

    return render(
        request,
        'exam.html',
        context
    )


def show_exam_result(request, course_id):

    course = get_object_or_404(
        Course,
        pk=course_id
    )

    enrollment = get_object_or_404(
        Enrollment,
        user=request.user,
        course=course
    )

    submission = Submission.objects.filter(
        enrollment=enrollment
    ).last()

    selected_choices = submission.choices.all()

    total_score = 0
    possible_score = 0

    for question in Question.objects.filter(
        lesson__course=course
    ):

        possible_score += question.grade

        correct_choices = question.choices.filter(
            is_correct=True
        )

        if all(
            choice in selected_choices
            for choice in correct_choices
        ):
            total_score += question.grade

    context = {
        'course': course,
        'enrollment': enrollment,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(
        request,
        'exam_result_bootstrap.html',
        context
    )
