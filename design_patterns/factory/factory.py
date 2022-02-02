from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def print_role(self):
        pass

    def am_i_person(self):
        print('Yes I am a person')


class Student(IPerson):
    def __init__(self, name):
        self.name = name
    def print_role(self):
        print('student')


class Teacher(IPerson):
    def print_role(self):
        print('teacher')

class PersonFactory:

    @staticmethod
    def build_person(choice, **kwargs):
        if choice == 'student':
            return Student(**kwargs)
        elif choice == 'teacher':
            return Teacher()
        return -1

choice = input('chose the person you want to create:')
person = PersonFactory.build_person(choice)
person.print_role()
person.am_i_person()

student = PersonFactory.build_person('student',name = 'Farzan')
print(student.name)