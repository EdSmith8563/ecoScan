from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile, UserLocation, Location
from .models import *
from django.http import HttpResponseBadRequest

# Ensures that only authenticated users can access the camera view and quizzes
@login_required
def camera(request):
    return render(request, 'camera.html')
@login_required
def quiz1(request):
    quiz = get_object_or_404(Quiz, title='CREWW Building') # Retrieve the quiz by its title or return a 404 if not found
    request.session['quiz_title'] = quiz.title # Store the quiz title in the session for future reference
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz2(request):
    quiz = get_object_or_404(Quiz, title='Car Park B') 
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz3(request):
    quiz = get_object_or_404(Quiz, title='Greenhouse')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz4(request):
    quiz = get_object_or_404(Quiz, title='Reed Pond')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz5(request):
    quiz = get_object_or_404(Quiz, title='East Park')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz6(request):
    quiz = get_object_or_404(Quiz, title='Wellbeing Services Facility')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz7(request):
    quiz = get_object_or_404(Quiz, title='Taddiforde Valley')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz8(request):
    quiz = get_object_or_404(Quiz, title='Pine Tree Belt')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz9(request):
    quiz = get_object_or_404(Quiz, title='Field Above Car Park B')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz10(request):
    quiz = get_object_or_404(Quiz, title='Laver Pond')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz11(request):
    quiz = get_object_or_404(Quiz, title='Plantation')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})
@login_required
def quiz12(request):
    quiz = get_object_or_404(Quiz, title='Poole Gate')
    request.session['quiz_title'] = quiz.title
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

# Handles quiz submission
@login_required
def quiz_submit(request):
    if request.method == 'POST':
        quiz_title = request.session.get('quiz_title')
        if not quiz_title:
            return HttpResponseBadRequest("Quiz title is missing.")

        # Retrieve the Quiz and Location objects based on the quiz title
        quiz = get_object_or_404(Quiz, title=quiz_title)
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        location = get_object_or_404(Location, name=quiz_title)

        # Initialize counters for the points and correct answers
        points_for_this_quiz = 0
        questions_answered_right = 0
        
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = key.split('question')[1]
                selected_answer = value
                
                # Check if the selected answer is correct
                correct_answer = Answer.objects.filter(question_id=question_id, is_correct=True).first()
                if correct_answer and str(correct_answer.id) == selected_answer:
                    questions_answered_right += 1
                    points_for_this_quiz += 10  

        # Create or update the UserLocation record with the quiz results
        user_location, created = UserLocation.objects.get_or_create(
            user=user_profile,
            location=location,
            defaults={
                'points_obtained': points_for_this_quiz,
                'questions_answered_right': questions_answered_right,
            }
        )

        if not created:
            user_location.points_obtained = points_for_this_quiz
            user_location.questions_answered_right = questions_answered_right
            user_location.save()

         # Store the user's score in the session
        request.session['points_for_this_quiz'] = points_for_this_quiz

        return redirect('quiz_success')
    else:
        return HttpResponseBadRequest("Invalid request method.")

# Renders a success page after a quiz is successfully submitted
@login_required
def quiz_success(request):
    points_for_this_quiz = request.session.get('points_for_this_quiz', 0)  # Retrieve the score
    if 'points_for_this_quiz' in request.session:
        del request.session['points_for_this_quiz']  # Clear the score from the session
    return render(request, 'quiz/quiz_success.html', {'points_for_this_quiz': points_for_this_quiz})
