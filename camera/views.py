from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile, UserLocation, Location
from django.db.models import F

def camera(request):
    return render(request, 'camera.html')
def quiz1(request):
    # Your view logic
    return render(request, 'quiz/quiz1.html')

def quiz2(request):
    # Your view logic
    return render(request, 'quiz/quiz2.html')
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
        location = Location.objects.get(location_id='1')  # Assuming this location already exists
        user_location, _ = UserLocation.objects.get_or_create(user=user_profile, location=location)
        
        # Calculate points for this quiz
        points_for_this_quiz = 0
        correct_answers = {'question1': 'C', 'question2': 'D', 'question3': 'C', 'question4': 'D', 'question5': 'A'}  # Example answers
        for question, correct_answer in correct_answers.items():
            if request.POST.get(question) == correct_answer:
                points_for_this_quiz += 10
        
        # Update points in UserProfile and UserLocation
        user_profile.total_points = F('total_points') + points_for_this_quiz
        user_profile.save()
        user_profile.refresh_from_db()  # Ensure the F() expression update is applied

        user_location.points_obtained += points_for_this_quiz
        user_location.questions_answered_right += sum(1 for answer in request.POST.values() if answer in correct_answers.values())
        user_location.save()

        # Redirect to a new page after form submission
        return redirect('quiz_success')  # Replace 'some_success_url' with the actual URL name
    
    # If not a POST request, or some other logic needed
    return redirect('quiz1')  # Redirect back to quiz or elsewhere as needed

@login_required
def quiz_success(request):
    return render(request, 'quiz/quiz_success.html')