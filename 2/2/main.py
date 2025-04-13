from datetime import datetime

class Student:
    def __init__(self, name=None, surname=None, year=None):
        self.name = name
        self.surname = surname
        self.year = year
    
    @property
    def list(self):
        return [self.name, self.surname]
    
    @property
    def course(self):
        if self.year is None:
            return None
        current_year = datetime.now().year
        age = current_year - self.year
        if age <= 15:
            return 'too young'
        return min((age - 16) + 1, 4)
        
    def _get_full_name(self):
        if self.name and self.surname:
            return f"{self.name} {self.surname}"
        elif self.name:
            return self.name
        elif self.surname:
            return self.surname
        return "Unknown"


class UniversityStudent(Student):
    def __init__(self, spec, student_id, grade_points, name=None, surname=None, year=None):
        super().__init__(name, surname, year)
        self.spec = spec
        self.student_id = student_id
        self.grade_points = grade_points
    
    @property
    def average_grade_point(self):
        if not self.grade_points:
            return 0
        return round(sum(self.grade_points) / len(self.grade_points), 1)
        
    def _get_student_info(self):
        full_name = self._get_full_name()
        return f"ID: {self.student_id}, Name: {full_name}, Specialization: {self.spec}"
    
    
vp = UniversityStudent('ICT', 101010, [5,3,4,5,3,5], 'Vlad', 'Pavluk', 16)
print(vp.list)
print(vp.course)
print(vp.average_grade_point)