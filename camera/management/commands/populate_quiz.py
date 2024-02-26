from django.core.management.base import BaseCommand
from camera.models import Quiz, Question, Answer

class Command(BaseCommand):
    help = 'Populate database with quiz questions and answers'

    def handle(self, *args, **kwargs):
        quiz_title = "CREWW Building"
        quiz, created = Quiz.objects.get_or_create(title=quiz_title)

        if created:
            self.stdout.write(self.style.SUCCESS(f'Quiz "{quiz_title}" created successfully.'))

            questions_data = [
                {
                    "text": "What was the primary source of funding for the construction of the CREWW building?",
                    "answers": [
                        {"text": "Government grant", "is_correct": True},
                        {"text": "University endowment", "is_correct": False},
                        {"text": "Corporate sponsorship", "is_correct": False},
                        {"text": "Private donations", "is_correct": False}
                    ]
                },
                {
                    "text": "How does the design of the CREWW building reflect its thematic focus on water and sustainability?",
                    "answers": [
                        {"text": "By utilizing a downhill 'cascade' design with lightweight cladding", "is_correct": True},
                        {"text": "By incorporating a rooftop garden", "is_correct": False},
                        {"text": "By featuring extensive use of glass for natural lighting", "is_correct": False},
                        {"text": "By using recycled materials in construction", "is_correct": False}
                    ]
                },
                {
                    "text": "What additional funding was secured to ensure the CREWW building achieves 'Net Zero in Operation' status?",
                    "answers": [
                        {"text": "£1 million", "is_correct": True},
                        {"text": "£500,000", "is_correct": False},
                        {"text": "£2.5 million", "is_correct": False},
                        {"text": "£100,000", "is_correct": False}
                    ]
                },
                {
                    "text": "How will the CREWW building contribute to sustainable research infrastructure beyond its own operations?",
                    "answers": [
                        {"text": "By serving as a living laboratory for monitoring and optimizing energy and water efficiency", "is_correct": True},
                        {"text": "By hosting community events on sustainability", "is_correct": False},
                        {"text": "By implementing water-saving measures in the surrounding area", "is_correct": False},
                        {"text": "By providing free sustainability workshops for students", "is_correct": False}
                    ]
                },
                {
                    "text": "Which sustainable features are incorporated into the CREWW building to achieve 'Net Zero in Operation' status?",
                    "answers": [
                        {"text": "Air source heat pumps, high thermal efficiency materials, solar panels, and LED lighting", "is_correct": True},
                        {"text": "Wind turbines and hydroelectric power generators", "is_correct": False},
                        {"text": "Geothermal heating and rainwater harvesting systems", "is_correct": False},
                        {"text": "Biogas digesters and composting toilets", "is_correct": False}
                    ]
                }
                # Add more questions and answers data as needed
            ]

            for question_data in questions_data:
                question = Question.objects.create(quiz=quiz, text=question_data['text'])
                self.stdout.write(self.style.SUCCESS(f'Question "{question.text}" created successfully.'))

                for answer_data in question_data['answers']:
                    Answer.objects.create(question=question, text=answer_data['text'], is_correct=answer_data['is_correct'])
                    self.stdout.write(self.style.SUCCESS(f'Answer "{answer_data["text"]}" created successfully for question "{question.text}".'))

        else:
            self.stdout.write(self.style.WARNING(f'Quiz "{quiz_title}" already exists. Database not modified.'))

