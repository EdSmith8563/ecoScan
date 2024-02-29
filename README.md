# ECM2434 Group Software Engineering project - Dev Dogs

### Group Members:
1. Edward Smith
2. Nathan de Beer
3. Sholto Bayley
4. Alexander Seton
5. Nicky Prowse
6. Seb White

# EcoScan
EcoScan is a web-based django application that was designed to use gamification to promote sustainability on the University of Exeter's streatham campus.

## Details
Users have to log in with a username and password to play, and can then use their camera to scan QR codes around the campus, which then lets them answer 5 questions in a quiz about that location. Users points and number of questions answered right are stored in a database and displayed in tables on the landing page. The leaderboard table allows users to compete for high scores against other players. The map page lets users see an approximate location of where the QR codes are located, however part of the game is searching for said QR codes. It also allows users to see which locations have been discoverd. The website also features a light and dark mode.

# How To Run
### Ensure no migrations need to be made:
```console
python3 manage.py makemigrations
python3 manage.py migrate
```
### Ensure quizzes and locations are populated:
```console
python3 manage.py populate_locations
python3 manage.py populate_quiz
```
### Run on localhost:
```console
python3 manage.py runserver
```
## Links
GitHub Link: https://github.com/EdSmith8563/ecoScan

Trello Link: https://trello.com/invite/b/abgL6Sr0/ATTIad3f6076c40f0526a0daab51af440fca50BDBB1B/dev-dogs-kanban-board


