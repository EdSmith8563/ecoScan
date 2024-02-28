from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile, UserLocation, Location
from django.db.models import F
from .models import *
from django.contrib import messages
from django.http import HttpResponseBadRequest

def camera(request):
    return render(request, 'camera.html')
@login_required
def quiz1(request):
    quiz = get_object_or_404(Quiz, title='CREWW Building')  # Adjust the title as necessary
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz2(request):
    quiz = get_object_or_404(Quiz, title='Car Park B')  # Adjust the title as necessary
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
def quiz3(request):
    quiz = get_object_or_404(Quiz, title='Greenhouse')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz4(request):
    quiz = get_object_or_404(Quiz, title='Reed Pond')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
def quiz5(request):
    quiz = get_object_or_404(Quiz, title='East Park')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz6(request):
    quiz = get_object_or_404(Quiz, title='Wellbeing Services Facility')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz7(request):
    quiz = get_object_or_404(Quiz, title='Taddiforde Valley')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz8(request):
    quiz = get_object_or_404(Quiz, title='Pine Tree Belt')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
def quiz9(request):
    quiz = get_object_or_404(Quiz, title='Field above Car Park B')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz10(request):
    quiz = get_object_or_404(Quiz, title='Laver Pond')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz11(request):
    quiz = get_object_or_404(Quiz, title='Plantation')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def quiz12(request):
    quiz = get_object_or_404(Quiz, title='Poole Gate')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})


@login_required
def quiz_submit(request):
    if request.method == 'POST':
        # Extract quiz title from POST data or URL
        quiz_title = request.session.get('quiz_title')
        if not quiz_title:
            return HttpResponseBadRequest("Quiz title is missing.")

        quiz = get_object_or_404(Quiz, title=quiz_title)
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        
        # Assume each quiz is linked to a location via a ForeignKey or similar
        location = get_object_or_404(Location, name=quiz_title)

        points_for_this_quiz = 0
        questions_answered_right = 0
        
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = key.split('question')[1]
                selected_answer = value
                
                correct_answer = Answer.objects.filter(question_id=question_id, is_correct=True).first()
                
                if correct_answer and str(correct_answer.id) == selected_answer:
                    questions_answered_right += 1
                    points_for_this_quiz += 10  

        # Check if UserLocation for this quiz exists
        user_location, created = UserLocation.objects.get_or_create(
            user=user_profile,
            location=location,
            defaults={
                'points_obtained': points_for_this_quiz,
                'questions_answered_right': questions_answered_right,
            }
        )

        if not created:
            previous_points = user_location.points_obtained
            points_difference = points_for_this_quiz - previous_points
            user_location.points_obtained = points_for_this_quiz
            user_location.questions_answered_right = questions_answered_right
            user_location.save()
        else:
            points_difference = points_for_this_quiz

        # Update points in UserProfile, considering the points difference
        user_profile.total_points = F('total_points') + points_difference
        user_profile.save()

        return redirect('quiz_success')
    else:
        return HttpResponseBadRequest("Invalid request method.")

@login_required
def quiz_success(request):
    return render(request, 'quiz/quiz_success.html')