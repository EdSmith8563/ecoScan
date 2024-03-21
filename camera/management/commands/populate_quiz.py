from django.core.management.base import BaseCommand
from camera.models import Quiz, Question, Answer

# Define a custom management command to populate the database with quiz data
class Command(BaseCommand):
    help = 'Populate database with quiz questions and answers'

    def handle(self, *args, **kwargs):
        # Define a list of dictionaries containing quiz data
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
            {
                "title": "East Park",
                "questions": [
                    {
                        "text": "Which sustainable building certification did East Park aim for, reflecting its commitment to environmental responsibility?",
                        "answers": [
                            {"text": "LEED Platinum", "is_correct": False},
                            {"text": "BREEAM Excellent", "is_correct": True},
                            {"text": "Green Globes", "is_correct": False},
                            {"text": "Living Building Challenge", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What percentage of on-site waste was recycled during the construction of East Park?",
                        "answers": [
                            {"text": "60%", "is_correct": False},
                            {"text": "75%", "is_correct": False},
                            {"text": "85%", "is_correct": False},
                            {"text": "90%", "is_correct": True}
                        ]
                    },
                    {
                        "text": "Which of the following is NOT a feature of East Park's sustainable design?",
                        "answers": [
                            {"text": "Including A or A+ rated appliances and low energy fittings", "is_correct": False},
                            {"text": "Recycling 100% of the waste generated on site", "is_correct": True},
                            {"text": "Providing high levels of insulation", "is_correct": False},
                            {"text": "Incorporating green materials with high environmental ratings", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the primary purpose of the green spine in the layout of East Park?",
                        "answers": [
                            {"text": "To provide a central area for vehicle access", "is_correct": False},
                            {"text": "To connect all levels of the residences", "is_correct": True},
                            {"text": "To serve as a barrier between different residential terraces", "is_correct": False},
                            {"text": "To create a space for large community events", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How does East Park promote social interaction and prevent isolation among its residents?",
                        "answers": [
                            {"text": "By limiting access to shared spaces", "is_correct": False},
                            {"text": "By providing private spaces only", "is_correct": False},
                            {"text": "By making the entire site fully accessible", "is_correct": True},
                            {"text": "By discouraging community activities", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Wellbeing Services Facility",
                "questions": [
                    {
                        "text": "How much energy was saved during the construction of the Wellbeing Services Facility compared to traditional methods?",
                        "answers": [
                            {"text": "23%", "is_correct": False},
                            {"text": "40%", "is_correct": False},
                            {"text": "67%", "is_correct": True},
                            {"text": "80%", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is one feature of the Wellbeing Services Facility that contributes to its sustainable design?",
                        "answers": [
                            {"text": "Inclusion of energy-intensive appliances", "is_correct": False},
                            {"text": "Use of air-permeable materials", "is_correct": True},
                            {"text": "Minimal insulation", "is_correct": False},
                            {"text": "No consideration for waste management", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Where is the Wellbeing Services Facility located in relation to existing wellbeing services on campus?",
                        "answers": [
                            {"text": "Adjacent to the Forum and Queens", "is_correct": False},
                            {"text": "Adjacent to Reed Hall and Reed Mews", "is_correct": True},
                            {"text": "In the heart of the city center", "is_correct": False},
                            {"text": "At the bottom of Mardon Hill", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What was the primary construction method used for the Wellbeing Services Facility, contributing to its sustainability goals?",
                        "answers": [
                            {"text": "Traditional on-site construction", "is_correct": False},
                            {"text": "Using non-recyclable materials", "is_correct": False},
                            {"text": "No specific construction method was employed", "is_correct": False},
                            {"text": "Off-site construction with Modern Methods of Construction (MMC)", "is_correct": True},
                        ]
                    },
                     {
                        "text": "How does the Wellbeing Services Facility aim to support students' mental health?",
                        "answers": [
                            {"text": "By providing only physical health services", "is_correct": False},
                            {"text": "By offering confidential spaces for counselling sessions", "is_correct": True},
                            {"text": "By organizing social events outside the facility", "is_correct": False},
                            {"text": "By limiting access to appointments", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Taddiforde Valley",
                "questions": [
                    {
                        "text": "What was the primary purpose behind the creation of the watercourse and series of ponds in Taddiforde Valley?",
                        "answers": [
                            {"text": "To provide recreational activities for visitors", "is_correct": False},
                            {"text": "To create diverse habitats and support local biodiversity", "is_correct": True},
                            {"text": "To study water flow dynamics in man-made environments", "is_correct": False},
                            {"text": "To generate hydroelectric power", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How does the large pond at Taddiforde Valley contribute to bird conservation efforts?",
                        "answers": [
                            {"text": "By providing artificially heated water sources", "is_correct": False},
                            {"text": "By using drones to monitor bird populations", "is_correct": False},
                            {"text": "By leaving fallen branches for roosting points", "is_correct": True},
                            {"text": "By importing exotic birds to increase diversity", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which of the following species benefits from the habitat piles left in wooded areas of Taddiforde Valley?",
                        "answers": [
                            {"text": "Domestic cats", "is_correct": False},
                            {"text": "Dormice, hedgehogs, and water voles", "is_correct": True},
                            {"text": "Rabbits and squirrels", "is_correct": False},
                            {"text": "Coyotes", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What makes the plant life in the watercourses of Taddiforde Valley notable for conservation?",
                        "answers": [
                            {"text": "Exotic plants imported from tropical regions", "is_correct": False},
                            {"text": "Artificially engineered super-plants", "is_correct": False},
                            {"text": "Plants genetically modified to require less water", "is_correct": False},
                            {"text": "Rare plant species such as lesser water parsnip", "is_correct": True}
                        ]
                    },
                    {
                        "text": "Which of the following best describes the management approach used for the large pond at Taddiforde Valley?",
                        "answers": [
                            {"text": "High-intensity management with regular chemical treatments", "is_correct": False},
                            {"text": "Sympathetic management, leaving natural elements like fallen branches", "is_correct": True},
                            {"text": "Complete removal of all natural debris to improve water clarity", "is_correct": False},
                            {"text": "Use of artificial structures to replace natural habitats", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Pine Tree Belt",
                "questions": [
                    {
                        "text": "What role do sloe berries and brambles/blackberries play in the Pine Tree Belt ecosystem?",
                        "answers": [
                            {"text": "They are primarily used for human consumption", "is_correct": False},
                            {"text": "They act as decorative plants to enhance the aesthetic value of the area", "is_correct": False},
                            {"text": "They provide food sources for a range of mammal species", "is_correct": True},
                            {"text": "They are toxic to most animal species and are used to control pest populations", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which group of insects is particularly attracted to the Pine Tree Belt during early Spring?",
                        "answers": [
                            {"text": "Locusts and cicadas seeking warmth", "is_correct": False},
                            {"text": "Solitary bees and bumblebees visiting flowers for nectar and pollen", "is_correct": True},
                            {"text": "Moths and butterflies migrating through the area", "is_correct": False},
                            {"text": "Aphids and leafhoppers feeding on sap", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How does the steep bank to the rear of the Harrison Building contribute to the biodiversity of the Pine Tree Belt area?",
                        "answers": [
                            {"text": "By serving as a sunbathing area for reptiles", "is_correct": False},
                            {"text": "Through minimal management, encouraging rough grass and scrub species", "is_correct": True},
                            {"text": "By being a designated feeding area for herbivorous mammals", "is_correct": False},
                            {"text": "By hosting competitive insect-eating contests", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the significance of the Wild Conifer Collection within the Pine Tree Belt area?",
                        "answers": [
                            {"text": "It is primarily for decorative purposes to attract tourists", "is_correct": False},
                            {"text": "It serves as a Christmas tree supply for the local community", "is_correct": False},
                            {"text": "Part of an international research project on trees from wild seeds", "is_correct": True},
                            {"text": "To test the commercial viability of various conifer species", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which bird species is NOT mentioned as visitors or residents of the Pine Tree Belt?",
                        "answers": [
                            {"text": "Sparrow", "is_correct": True},
                            {"text": "Blue Tit", "is_correct": False},
                            {"text": "Robin", "is_correct": False},
                            {"text": "Wren", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Field Above Car Park B",
                "questions": [
                    {
                        "text": "What is the purpose of the Devon Bank that surrounds one side of the Field Above Car Park B?",
                        "answers": [
                            {"text": "To serve as a natural boundary that enhances security for the surrounding wildlife", "is_correct": False},
                            {"text": "For aesthetic appeal and to increase the property value", "is_correct": False},
                            {"text": "To reduce noise pollution from nearby roads", "is_correct": False},
                            {"text": "To provide habitat for native hedgerow species, promoting biodiversity", "is_correct": True}
                        ]
                    },
                    {
                        "text": "What sustainability practice is applied in the Field Above Car Park B with regards to green waste?",
                        "answers": [
                            {"text": "It is incinerated to generate power", "is_correct": False},
                            {"text": "Recycled as mulch and soil improver under an Environment Agency licence", "is_correct": True},
                            {"text": "Shipped off-site for disposal in landfill", "is_correct": False},
                            {"text": "Used to create sculptures and decorative elements", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is a key feature of the Exeter Community Garden developed in the Field Above Car Park B?",
                        "answers": [
                            {"text": "It hosts a large-scale composting facility", "is_correct": False},
                            {"text": "Includes raised production beds, an orchard, and a bee hive", "is_correct": True},
                            {"text": "It is a research area for genetically modified crops", "is_correct": False},
                            {"text": "Focuses solely on the cultivation of ornamental plants", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How does the Exeter Community Garden promote biodiversity?",
                        "answers": [
                            {"text": "Via sustainable growing practices and providing habitats like bee hives", "is_correct": True},
                            {"text": "By using pesticides to ensure high yield crops", "is_correct": False},
                            {"text": "By planting a single crop type to increase efficiency", "is_correct": False},
                            {"text": "Through weekly biodiversity awareness events", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What role does the orchard in the Exeter Community Garden play?",
                        "answers": [
                            {"text": "It's primarily used for commercial fruit production", "is_correct": False},
                            {"text": "Serves as an educational tool for sustainable agriculture practices", "is_correct": True},
                            {"text": "It's a genetic modification testing site for new fruit varieties", "is_correct": False},
                            {"text": "Used for recreational purposes by staff and students of the University", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Laver Pond",
                "questions": [
                    {
                        "text": "Why was Laver Pond introduced on campus?",
                        "answers": [
                            {"text": "To provide recreational water sports facilities", "is_correct": False},
                            {"text": "To create a natural habitat exclusively for exotic plant species to thrive", "is_correct": False},
                            {"text": "So that buildings integrate with the landscape rather than dominating it", "is_correct": True},
                            {"text": "For the collection and storage of rainwater for irrigation purposes", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How does the design of the Living Systems Institute research building complement Laver Pond?",
                        "answers": [
                            {"text": "By using reflective materials to mirror the pond's surface", "is_correct": False},
                            {"text": "Through high-rise construction that overlooks the pond", "is_correct": False},
                            {"text": "Inclusion of wildflower planting to blend with the existing landscape", "is_correct": True},
                            {"text": "Utilizing underwater laboratories accessible by diving", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which of the following plant species is NOT mentioned as part of Laver Pond's habitat?",
                        "answers": [
                            {"text": "Maple Trees", "is_correct": True},
                            {"text": "Bulrush", "is_correct": False},
                            {"text": "Flag Irises", "is_correct": False},
                            {"text": "Pond Lilies", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What role do the water boatmen and back-swimmers play in Laver Pond's ecosystem?",
                        "answers": [
                            {"text": "They primarily feed on algae, keeping the water clear", "is_correct": False},
                            {"text": "Contribute to the pond's biodiversity as part of the aquatic food web", "is_correct": True},
                            {"text": "They are used to control the mosquito population", "is_correct": False},
                            {"text": "Decorative purposes to enhance the visual appeal of the pond", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which bird species mentioned is known for its ability to climb tree trunks in Laver Pond's vicinity?",
                        "answers": [
                            {"text": "The Great Spotted Woodpecker", "is_correct": True},
                            {"text": "The Kingfisher", "is_correct": False},
                            {"text": "The Sparrowhawk", "is_correct": False},
                            {"text": "The Barn Owl", "is_correct": False}
                        ]
                    }
                ]
            },
            {
                "title": "Plantation",
                "questions": [
                    {
                        "text": "What characteristic feature is noted about the Eucalyptus species found in the Plantation?",
                        "answers": [
                            {"text": "They exude an aromatic resin with a characteristic astringent odour", "is_correct": True},
                            {"text": "They change color with the seasons", "is_correct": False},
                            {"text": "They are the tallest trees in the Plantation", "is_correct": False},
                            {"text": "They bloom year-round, providing constant color to the surroundings", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What is the primary purpose of the bug hotel located close to the pond in the Plantation?",
                        "answers": [
                            {"text": "To serve as a research facility for entomologists", "is_correct": False},
                            {"text": "To attract tourists to the area", "is_correct": False},
                            {"text": "To provide a habitat for invertebrates and overwintering insects", "is_correct": True},
                            {"text": "To control the population of pests in the Plantation", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Which of the following plant groups is NOT mentioned as part of the Plantation's flora?",
                        "answers": [
                            {"text": "Cacti", "is_correct": True},
                            {"text": "Bamboo", "is_correct": False},
                            {"text": "Camellia", "is_correct": False},
                            {"text": "Rhododendron", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What role does the watercourse in the Plantation play for its wildlife?",
                        "answers": [
                            {"text": "It is primarily used for human water sports", "is_correct": False},
                            {"text": "Habitats for amphibians, small mammals, and a variety of bird species", "is_correct": True},
                            {"text": "Acts as a barrier to prevent the spread of invasive plant species", "is_correct": False},
                            {"text": "It is artificially colored to enhance aesthetic appeal", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Why are exotic plants like Bamboo, Camellia, and Rhododendron included in the Plantation's design?",
                        "answers": [
                            {"text": "To promote the growth of local plants and support wildlife", "is_correct": False},
                            {"text": "For their ability to adapt and thrive in the local climate", "is_correct": False},
                            {"text": "To test their potential as cash crops for the local economy", "is_correct": False},
                            {"text": "To add to the diversity and enrich the habitat's biodiversity", "is_correct": True}
                        ]
                    }
                ]
            },
            {
                "title": "Poole Gate",
                "questions": [
                    {
                        "text": "What is the significance of the wildflower roof on top of the Mood Disorder Centre near Poole Gate?",
                        "answers": [
                            {"text": "It's primarily for aesthetic purposes to improve building appearances", "is_correct": False},
                            {"text": "Creates a habitat for pollen and nectar-dependent species", "is_correct": True},
                            {"text": "To reduce heating and cooling costs for the building", "is_correct": False},
                            {"text": "It serves as a recreational area for patients and staff", "is_correct": False}
                        ]
                    },
                    {
                        "text": "Why are purple crocus planted at the banking near Washington Singer?",
                        "answers": [
                            {"text": "To provide a colorful display during spring", "is_correct": False},
                            {"text": "To attract an endangered specific species of butterfly for study", "is_correct": False},
                            {"text": "Purple is the University's official color", "is_correct": False},
                            {"text": "As part of a local initiative to raise funds for Polio eradication", "is_correct": True}
                        ]
                    },
                    {
                        "text": "What historical investment significantly contributed to the establishment of Reed Arboretum?",
                        "answers": [
                            {"text": "A government grant of £20,000 for educational development", "is_correct": False},
                            {"text": "A donation from East Indian Merchantman, Richard Thornton West", "is_correct": True},
                            {"text": "Funding from a private botanical research foundation", "is_correct": False},
                            {"text": "Crowdfunding by the local community", "is_correct": False}
                        ]
                    },
                    {
                        "text": "What role do the cherry trees near Washington Singer play in the ecosystem?",
                        "answers": [
                            {"text": "They are purely ornamental, with no impact on the local ecosystem", "is_correct": False},
                            {"text": "They produce early season flowers, providing a welcome and food for pollinators", "is_correct": True},
                            {"text": "Their deep roots help stabilize the soil, preventing erosion", "is_correct": False},
                            {"text": "They are a source of timber for sustainable campus construction projects", "is_correct": False}
                        ]
                    },
                    {
                        "text": "How does the original Old Botanic Garden contribute to the campus's botanical diversity?",
                        "answers": [
                            {"text": "Through its collection of exotic species such as Acea and Californian Nutmeg", "is_correct": True},
                            {"text": "By serving as a repository for endangered plant species", "is_correct": False},
                            {"text": "It is used for the cultivation of vegetables and fruits for the campus cafeteria", "is_correct": False},
                            {"text": "Hosting annual flower shows to fund campus greening initiatives", "is_correct": False}
                        ]
                    }
                ]
            }
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
