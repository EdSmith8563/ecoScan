from django.core.management.base import BaseCommand
from camera.models import Quiz, Question, Answer

class Command(BaseCommand):
    help = 'Populate database with quiz questions and answers'

    def handle(self, *args, **kwargs):
        quizzes_data = [
            {
                "title": "CREWW Building",
                "questions": [
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
                            {"text": "By incorporating a rooftop garden", "is_correct": False},
                            {"text": "By featuring extensive use of glass for natural lighting", "is_correct": False},
                            {"text": "By using recycled materials in construction", "is_correct": False},
                            {"text": "By utilizing a downhill 'cascade' design with lightweight cladding", "is_correct": True}
                        ]
                    },
                    {
                        "text": "What additional funding was secured to ensure the CREWW building achieves 'Net Zero in Operation' status?",
                        "answers": [
                            {"text": "£500,000", "is_correct": False},
                            {"text": "£1 million", "is_correct": True},
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
                            {"text": "Wind turbines and hydroelectric power generators", "is_correct": False},
                            {"text": "Air source heat pumps, high thermal efficiency materials, solar panels, and LED lighting", "is_correct": True},
                            {"text": "Geothermal heating and rainwater harvesting systems", "is_correct": False},
                            {"text": "Biogas digesters and composting toilets", "is_correct": False}
                        ]
                    }
                    # Additional questions for the first quiz
                ]
            },
            {
                "title": "Car Park B",
                "questions": [
                    {
                        "text": "What is the purpose of the solar panels installed on the roof of Car Park B?",
                        "answers": [
                            {"text": "To provide shade for parked cars", "is_correct": False},
                            {"text": "For water heating purposes", "is_correct": False},
                            {"text": "To generate solar electricity for the car park and electric charging points", "is_correct": True},
                            {"text": "To power the car park's lighting system only", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How many electric parking bays are included in Car Park B?",
                        "answers": [
                            {"text": "20", "is_correct": False},
                            {"text": "30", "is_correct": True},
                            {"text": "40", "is_correct": False},
                            {"text": "50", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which initiative is NOT part of the project's contribution to sustainable travel?",
                        "answers": [
                            {"text": "Increasing the Stagecoach bus discount to include all city routes", "is_correct": False},
                            {"text": "Introducing three pool cars on campus that colleagues can hire by the hour", "is_correct": False},
                            {"text": "Free parking for all university staff", "is_correct": True},
                            {"text": "A personalised travel plan service for all new staff", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What measure has been taken to reduce light pollution from Car Park B?",
                        "answers": [
                            {"text": "Installing low wattage lighting that dims after 10pm with proximity sensors", "is_correct": True},
                            {"text": "Completely turning off all lights after sunset", "is_correct": False},
                            {"text": "Using high-intensity discharge lamps", "is_correct": False},
                            {"text": "Lights are on at full brightness throughout the night", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What types of trees have been planted around Car Park B to improve its aesthetic look?",
                        "answers": [
                            {"text": "Maple, Elm, and Redwood", "is_correct": False},
                            {"text": "Palm, Cedar, and Bamboo", "is_correct": False},
                            {"text": "Common Oak, Silver Birch, and Scot Pine", "is_correct": True},
                            {"text": "Willow, Ash, and Poplar", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Greenhouse",
                "questions": [
                    {
                        "text": "Why are greenhouses considered sustainable for plant research?",
                        "answers": [
                            
                            {"text": "They require no artificial lighting or temperature control", "is_correct": False},
                            {"text": "They use more soil than open-air farms", "is_correct": False},
                            {"text": "They create controlled environments, reducing the need for pesticides and excessive water use", "is_correct": True},
                            {"text": "They only grow non-native plants", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How does the Exeter University greenhouse contribute to sustainability in research?",
                        "answers": [
                            {"text": "By supporting research in Cellular and Chemical Biology, Environmental Biology, and Microbes & Diseases in a controlled environment", "is_correct": True},
                            {"text": "By using genetically modified plants only", "is_correct": False},
                            {"text": "By exclusively studying non-organic farming techniques", "is_correct": False},
                            {"text": "By operating without any use of renewable energy sources", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is a key benefit of using a greenhouse for plant growth?",
                        "answers": [
                            {"text": "They are cheaper to build and maintain than open fields", "is_correct": False},
                            {"text": "They do not require monitoring or management", "is_correct": False},
                            {"text": "Plants grow larger and faster naturally without human intervention", "is_correct": False},
                            {"text": "Ability to grow plants year-round, regardless of external weather conditions", "is_correct": True}
                        ]
                    },
                    {
                        "text": "How do greenhouses help in conserving water?",
                        "answers": [
                            {"text": "Through the use of drip irrigation systems and recapturing condensation", "is_correct": True},
                            {"text": "By using large quantities of water to ensure plant growth", "is_correct": False},
                            {"text": "Water conservation is not possible in greenhouses", "is_correct": False},
                            {"text": "Relying solely on rainwater for all watering needs", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which of the following is NOT a sustainable practice commonly used in greenhouses?",
                        "answers": [
                            {"text": "Utilizing integrated pest management to reduce chemical use", "is_correct": False},
                            {"text": "Using high-volume, high-pressure water systems for irrigation", "is_correct": True},
                            {"text": "Employing renewable energy sources to power heating and cooling systems", "is_correct": False},
                            {"text": "Recycling plant waste into compost for soil enrichment", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Reed Pond",
                "questions": [
                    {
                        "text": "What is the primary ecological benefit of the recent project works at Reed Pond?",
                        "answers": [
                           
                            {"text": "Increasing the water volume of the pond for recreational use", "is_correct": False},
                            {"text": "Reducing the overall water content to prevent flooding", "is_correct": False},
                            {"text": "Introducing exotic fish species to boost ornamental value", "is_correct": False},
                            {"text": "Enhancing habitat diversity for invertebrates and aquatic life", "is_correct": True}
                        ]
                    },
                    {
                        "text": "Which of the following invertebrates has NOT been recorded at Reed Pond following conservation efforts?",
                        "answers": [
                            {"text": "Water beetles", "is_correct": False},
                            {"text": "Dragonflies", "is_correct": False},
                            {"text": "Butterflies", "is_correct": True},
                            {"text": "Caddisflies", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What purpose does the bug hotel behind Reed Pond serve in the ecosystem?",
                        "answers": [
                            {"text": "Providing shelter and breeding grounds for beneficial insects and small fauna", "is_correct": True},
                            {"text": "Serving as a tourist attraction to increase foot traffic around the pond", "is_correct": False},
                            {"text": "Acting as a physical barrier to protect the pond from pollutants", "is_correct": False},
                            {"text": "Housing ornamental fish during the colder months", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Why was the tallest tree on campus near Reed Pond felled?",
                        "answers": [
                            {"text": "To clear space for additional water features around the pond", "is_correct": False},
                            {"text": "Due to decline caused by weather impacts and Armillaria fungus", "is_correct": True},
                            {"text": "It was harvested for educational purposes", "is_correct": False},
                            {"text": "To use its wood for constructing more bug hotels", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How are veteran trees in the Arboretum area near Reed Pond being sustained?",
                        "answers": [
                            {"text": "By decompacting soil with an air spade", "is_correct": True},
                            {"text": "Regular pruning to stimulate growth", "is_correct": False},
                            {"text": "Applying chemical fertilizers to promote rapid tree growth", "is_correct": False},
                            {"text": "By installing physical supports to prevent the trees from falling", "is_correct": False}
                        ]
                    }
                ]
            },
        ]

        for quiz_data in quizzes_data:
            quiz_title = quiz_data['title']
            quiz, created = Quiz.objects.get_or_create(title=quiz_title)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Quiz "{quiz_title}" created successfully.'))

                for question_data in quiz_data['questions']:
                    question = Question.objects.create(quiz=quiz, text=question_data['text'])
                    self.stdout.write(self.style.SUCCESS(f'Question "{question.text}" created successfully.'))

                    for answer_data in question_data['answers']:
                        Answer.objects.create(question=question, text=answer_data['text'], is_correct=answer_data['is_correct'])
                        self.stdout.write(self.style.SUCCESS(f'Answer "{answer_data["text"]}" created successfully for question "{question.text}".'))

            else:
                self.stdout.write(self.style.WARNING(f'Quiz "{quiz_title}" already exists. Database not modified.'))

