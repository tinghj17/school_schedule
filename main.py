from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")
quinn.get_num_classes()
quinn.summary()

# second instance
claire = Student(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )

claire.get_num_classes()
claire.summary()

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function

# instance od high school student
Tres = HighSchoolStudent(
                "Tres", 
                "senior", 
                [
                    "Algebra", 
                    "Writing"
                ],
                has_parking_pass= True,
                clubs = ["NSBE", "Yearbook"]
            )



print(Tres.display_classes())

Tres.join_club("coding")
print(Tres.display_clubs())