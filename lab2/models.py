from exceptions import *

class Subject():
    def __init__(self, name: str, semester: int):
        self.name: str = name
        self.semester: int = semester


class Student():
    def __init__(self, name: str, id: int, semester: int, major: str):
        self.name: str = name
        self.student_id: int = id
        self.semester: int = 1 
        self.major: str = major
        self.grades: dict[Subject , int ] = {}

    def Print(self):
        print(f"Имя студента: {self.name}, Курс: {self.semester}, Специальность: {self.major} ")

    def add_subject(self, subject: Subject) -> None:
        self.grades[subject] = None

    def remove_subject(self, subject: Subject) -> None:
        if subject not in self.grades:
            raise NotEnrolledError(
                f"Студент {self.name} не записан на дисциплину '{subject.name}'."
            )
        del self.grades[subject]

    def set_grade(self, subject: Subject, grade: int) -> None:
        if subject not in self.grades:
            raise NotEnrolledError(
                f"Нельзя выставить оценку: студент {self.name} не записан на дисциплину '{subject.name}'."
            )

        if not (1 <= grade <= 10):
            raise InvalidGradeError(
                f"Некорректная оценка '{grade}'. Оценка должна быть целым числом от 1 до 10."
            )

        self.grades[subject] = grade

    def get_average_grade(self) -> float:
        valid_grades = [g for g in self.grades.values() if g is not None]
        if not valid_grades:
            return 0.0
        return sum(valid_grades) / len(valid_grades)


    


class Department():
    def __init__(self, name: str, ):
        self.name = name
        self.curriculum: dict[str, list[Subject]] = {}

    def add_curriculum(self, major: str, subjects: list[Subject]) -> None:
        if major not in self.curriculum:
            self.curriculum[major] = list(subjects)
        else:
            for subj in subjects:
                if subj not in self.curriculum[major]:
                    self.curriculum[major].append(subj)

    def check_subject(self,major , subject: Subject) -> bool:
        if major not in self.curriculum:
            return False

        return subject in self.curriculum[major]
        


