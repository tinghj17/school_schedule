from .student import Student

#inheritance
class HighSchoolStudent(Student):
    def __init__(self, name, grade, classes, has_parking_pass = False, clubs = None):
        super().__init__(name, grade, classes) 
        self.has_parking_pass = has_parking_pass
        self.clubs = clubs if clubs is not None else []

    def parking_pass_status(self):
        if self.has_parking_pass:
            return f"{self.name} has parking pass"
        else:
            return f"{self.name} does not have parking pass"

    def join_club(self, club_name):
        self.clubs.append(club_name)
    
    def display_clubs(self):
        list_of_clubs = ", ".join(self.clubs)
        return f"{self.name} is a member of {list_of_clubs}"
    

    


