<img src="./static/accounts/images/banner.png" alt="EcoScan Banner" title="EcoScan Banner" width="700" height="auto">

## ECM2434 Group Software Engineering project - Dev Dogs

### **Group Members:**
1. Edward Smith
2. Nathan de Beer
3. Sholto Bayley
4. Alexander Seton
5. Nicky Prowse
6. Sebastian White

# EcoScan
EcoScan is a web-based django application that was designed to use gamification to promote sustainability on the University of Exeter's streatham campus.

# How To Run
## **Website**
https://www.ecoscan.online/
## **Locally**
### Ensure quizzes and locations are populated:
```console
python3 manage.py populate_locations
python3 manage.py populate_quiz
```
### Run on localhost:
```console
python3 manage.py runserver
```
# Walkthrough (Phone):
It is easiest to use the website https://www.ecoscan.online/ on a phone
<br> **or**<br>
Run locally on chrome (desktop) -> Inspect -> Toggle device toolbar for phone view <br>
(This method you will need the QR codes on your phone since you are scanning from the desktop's camera)

## Steps:
1. Click **Accept** in bottom right of screen
2. Click **Sign Up** 
3. Fill in **Username** and **Password** (x2)
4. click **I agree to...** checkbox 
5. click **Sign Up** (*you will be automatically logged in*)
6. Close congratulatory message at the top of screen (**cross button** to the right)
7. Click **triple line** menu button at top right of screen
8. Click **Camera** in navbar dropdown
9. Allow camera access if prompted 
10. Scan one of the 12 QR codes:
<div align="center">
    <img src="./static/qr/QR_quiz1.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz2.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz3.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz4.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz5.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz6.png" alt="Image 1" title="Image 1" height="120">
</div>
<div align="center">
    <img src="./static/qr/QR_quiz7.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz8.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz9.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz10.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz11.png" alt="Image 1" title="Image 1" height="120">
    <img src="./static/qr/QR_quiz12.png" alt="Image 1" title="Image 1" height="120">
</div>

QR Codes can also be found here:
- Root (EcoScan)
    - static
        - qr 
            - QR_quiz1.png
            - ...
            - QR_quiz12.png
11. Once successfully scanned, complete the quiz (5 questions)
12. Click green **Submit** button
13. Click red **Close** button
14. Scroll down to **leaderboard** table
15. Click on any username in the username column to view their stats
16. Click anywhere outside of the popup box to exit
17. Click triple line menu button ( top right )
18. Click **Map**
19. Allow location access if prompted (your location will not display on map if you are not within the bounds)
20. Click the **Places Discovered** widget
21. Click anywhere on **Places Discovered** widget again to close it
22. Zoom on the map to the green tick (the quiz location you discovered) 
23. Click on that green tick icon on the map (shows you points obtained for that location)
24. Repeat step 23 to close (or click on the cross at top right of info window)
25. Click **blue  gradient triple line** menu toggle at top right of screen (to show navbar)
26. Click **triple line** navbar button
27. Click **Settings**
28. Click **Theme**
29. If Navbar still displaying (if not repeat steps 25 and 26) click **Home** (or EcoScan)
30. Repeat steps 26,27,28 (dark mode)
31. Click **Add Email** under theme
32. Enter email and click **Add Email**
33. Close email success banner at top of screen
34. Feel free to explore **Logout, Login** and the **About** page + scanning more qr codes (quizzes)
35. Thank you
# Gamekeeper Admin (Desktop):
 - Accounts
     - User Locations
        - Gamekeepers can view the discovered locations of each user, they can change the points obtained at that location and the number of questions answered right. Any of these user locations can be deleted and the points obtained at the deleted lcoation will be removed from total points for that user. 
     - User profiles
        - A UserProfile is an extension of the user model. A gamekeeper can change their total points and theme preference (level will change automatically based on points). Deleteing a user will remove their associated UserProfile.
 - Authentication and Authorization
    - Groups
    - Users
        - A gamekeeper can modify the email address of a user and modify their staff/ superuser status.
 - Camera
    - Answers
        - Here a gamekeeper can view all answers to each questions and whether they are correct or not.
    - Questions
        - Here you can view the question and the quiz parent of that question.
    - Quizs
        - Here you can view all 12 quizes 
 - Map
     - Location

## Details
Users have to log in with a username and password to play, and can then use their camera to scan QR codes around the campus, which then lets them answer 5 questions in a quiz about that location. Users points and number of questions answered right are stored in a database and displayed in tables on the landing page. The leaderboard table allows users to compete for high scores against other players. The map page lets users see an approximate location of where the QR codes are located, however part of the game is searching for said QR codes. It also allows users to see which locations they have discoverd. 



    
## Links
GitHub Link: <br>
https://github.com/EdSmith8563/ecoScan

Trello Link: <br>
https://trello.com/invite/b/abgL6Sr0/ATTIad3f6076c40f0526a0daab51af440fca50BDBB1B/dev-dogs-kanban-board


