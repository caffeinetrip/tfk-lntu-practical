from datetime import datetime

class Student():
    def __init__(self, name=None, surname=None, year=None):
        self.name = name
        self.surname = surname
        self.year = year
        
    def get_course(self):
        if self.year is None:
            return None
        
        current_year = datetime.now().year
        age = current_year - self.year
        
        if age <= 15:
            return 'too young'
        
        return min((age - 16) + 1, 4)
        
    def create_list(self):
        return [self.name, self.surname]
    
vp = Student('Vlad', 'Pavluk', 2008)
print(vp.get_course())
print(vp.create_list())
    
