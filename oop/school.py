class School:
    def __init__(self, name, level, number_of_students):
        self.name = name
        self.level = level
        self.number_of_students = number_of_students

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_number_of_students(self, new_number_of_students):
        self.number_of_students = new_number_of_students
        return self.number_of_students

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.number_of_students} students"


class PrimarySchool(School):
    def __init__(self, name, level, number_of_students, pickup_policy):
        super().__init__(name, level, number_of_students)
        self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
        return self.pickup_policy

    def __repr__(self):
        School = super().__repr__()
        return School + f"The pickup policy is {self.pickup_policy}"


class HighSchool(School):

    def __init__(self, name, level, number_of_students, sport_team):
        super().__init__(name, level, number_of_students)
        self.sport_team = sport_team

    def get_sport_team(self):
        return self.sport_team

    def __repr__(self):
        school = super().__repr__()
        return school + f"The sport team is {self.sport_team}"
