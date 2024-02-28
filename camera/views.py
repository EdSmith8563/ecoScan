from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile, UserLocation, Location
from django.db.models import F
from .models import *

def camera(request):
    return render(request, 'camera.html')
@login_required
def quiz1(request):
    quiz = get_object_or_404(Quiz, title='CREWW Building')  # Adjust the title as necessary
    return render(request, 'quiz/quiz1.html', {'quiz': quiz})
@login_required
def quiz2(request):
    quiz = get_object_or_404(Quiz, title='Car Park B')  # Adjust the title as necessary
    return render(request, 'quiz/quiz2.html', {'quiz': quiz})
def quiz3(request):
    # Your view logic
    return render(request, 'quiz/quiz3.html')

def quiz4(request):
    # Your view logic
    return render(request, 'quiz/quiz4.html')
def quiz5(request):
    # Your view logic
    return render(request, 'quiz/quiz5.html')

def quiz6(request):
    # Your view logic
    return render(request, 'quiz/quiz6.html')
def quiz7(request):
    # Your view logic
    return render(request, 'quiz/quiz7.html')

def quiz8(request):
    # Your view logic
    return render(request, 'quiz/quiz8.html')
def quiz9(request):
    # Your view logic
    return render(request, 'quiz/quiz9.html')

def quiz10(request):
    # Your view logic
    return render(request, 'quiz/quiz10.html')
def quiz11(request):
    # Your view logic
    return render(request, 'quiz/quiz11.html')

def quiz12(request):
    # Your view logic
    return render(request, 'quiz/quiz12.html')


@login_required
def quiz1_submit(request):
    if request.method == 'POST':
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        # Assuming each quiz has a unique identifier, like a slug or id
        quiz = get_object_or_404(Quiz, title='CREWW Building')  # Adjust based on your Quiz model
        location = Location.objects.get(location_id='1')  # Fetch the location related to this quiz
        
        user_location, _ = UserLocation.objects.get_or_create(user=user_profile, location=location)
        
        points_for_this_quiz = 0
        questions_answered_right = 0
        
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = key.split('question')[1]
                selected_answer = value
                
                correct_answer = Answer.objects.filter(question_id=question_id, is_correct=True).first()
                
                if correct_answer and str(correct_answer.id) == selected_answer:
                    points_for_this_quiz += 10
                    questions_answered_right += 1

        # Update points in UserProfile and UserLocation
        user_profile.total_points = F('total_points') + points_for_this_quiz
        user_profile.save()
        user_profile.refresh_from_db()

        user_location.points_obtained += points_for_this_quiz
        user_location.questions_answered_right += questions_answered_right
        user_location.save()

        return redirect('quiz_success')
    
    return redirect('quiz1')
@login_required
def quiz2_submit(request):
    if request.method == 'POST':
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        # Assuming each quiz has a unique identifier, like a slug or id
        quiz = get_object_or_404(Quiz, title='Car Park B')  # Adjust based on your Quiz model
        location = Location.objects.get(location_id='2')  # Fetch the location related to this quiz
        
        user_location, _ = UserLocation.objects.get_or_create(user=user_profile, location=location)
        
        points_for_this_quiz = 0
        questions_answered_right = 0
        
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = key.split('question')[1]
                selected_answer = value
                
                correct_answer = Answer.objects.filter(question_id=question_id, is_correct=True).first()
                
                if correct_answer and str(correct_answer.id) == selected_answer:
                    points_for_this_quiz += 10
                    questions_answered_right += 1

        # Update points in UserProfile and UserLocation
        user_profile.total_points = F('total_points') + points_for_this_quiz
        user_profile.save()
        user_profile.refresh_from_db()

        user_location.points_obtained += points_for_this_quiz
        user_location.questions_answered_right += questions_answered_right
        user_location.save()

        return redirect('quiz_success')
    
    return redirect('quiz2')


@login_required
def quiz_success(request):
    return render(request, 'quiz/quiz_success.html')