from models import Student, Subject, Department
from exceptions import *


class faculty():
    def __init__(self, name: str):
        self.name = name
        self.majors: set[str] = set()
        self.departments: list[Department] = []
        self.students: dict[int, Student] = {}
    
    def add_major(self, major: str) -> None:
        self.majors.add(major)

    def add_department(self, department: Department) -> None:
        if department not in self.departments:
            self.departments.append(department)

    def add_students(self,student_id: int, student: Student):
        self.students[student_id] = student

    def Print(self):
        print(f"{print(self.name)}:",
              f"кафедры {[print(department.name) for department in self.departments]}",
              f"специальности {print(*self.majors)}", sep = "\n")
        if self.students != None:
            for key,value in self.students.items():
                print(f"Id студента:{key}", end= " ")
                value.Print()
        else:
            print("Список пуст")

    def add_subject_to_student(self, student_id: int, subject: Subject) -> None:
        if student_id not in self.students:
            raise StudentNotFoundError(f"Студент с ID {student_id} не найден!")

        student = self.students[student_id]

        found_department = None
        for dept in self.departments:
            if dept.check_subject(student.major, subject):
                found_department = dept
                break

        if found_department is None:
            raise CourseNotAllowedError(
                f"Предмет '{subject.name}' не читается ни одной кафедрой "
                f"для специальности '{student.major}'!"
            )

        if subject.semester != student.semester:
            raise CourseNotAllowedError(
                f"Предмет '{subject.name}' изучается в {subject.semester} семестре, "
                f"а студент {student.name} сейчас на {student.semester} семестре!"
            )

        if subject in student.grades:
            raise CourseNotAllowedError(
                f"Студент {student.name} уже записан на '{subject.name}'!"
            )

        student.add_subject(subject)
        print(f"Студент {student.name} записан на '{subject.name}' "
              f"(читает: {found_department.name})")

    def remove_student_from_subject( self, student_id: int, subject: Subject) -> None:
        if student_id not in self.students:
            raise StudentNotFoundError(
                f"Студент с ID {student_id} не найден на факультете."
            )

        student = self.students[student_id]

        student.remove_subject(subject)
        print(f"Студент {student.name} успешно удален из списка изучающих '{subject.name}'.")

    def grade_student(self, student_id: int, subject: Subject) -> None:
        if student_id not in self.students:
            raise StudentNotFoundError(
                f"Студент с ID {student_id} не найден на факультете."
            )

        student = self.students[student_id]
        grade = int(input("Введите оценку: "))
        student.set_grade(subject, grade)
        print(
            f"Оценка {grade} по предмету '{subject.name}' успешно выставлена студенту {student.name}."
        )

    def transfer_student_to_next_semester(self, student_id: int) -> None:
        if student_id not in self.students:
            raise StudentNotFoundError(f"Студент с ID {student_id} не найден!")

        student = self.students[student_id]

        current_subjects = [
            subj for subj in student.grades if subj.semester == student.semester
        ]

        if not current_subjects:
            raise SemesterTransferError(
                f"Студент {student.name} не записан ни на одну дисциплину в {student.semester} семестре!"
            )

        for subj in current_subjects:
            grade = student.grades[subj]
            if grade is None or grade < 4:
                raise SemesterTransferError(
                    f"Студент {student.name} не может быть переведен: дисциплина '{subj.name}' не сдана успешно!"
                )

        student.semester += 1
        print(f"Студент {student.name} успешно переведен на курс {student.semester}!")

    def generate_student_report(self, student_id: int) -> str:
        if student_id not in self.students:
            raise StudentNotFoundError(f"Студент с ID {student_id} не найден!")

        student = self.students[student_id]
        filename = f"report_{student.student_id}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Ведомость успеваемости\n")
            f.write(f"Студент: {student.name} (ID: {student.student_id})\n")
            f.write(f"Специальность: {student.major}\n")
            f.write(f"Текущий курс/семестр: {student.semester}\n")
            f.write("Дисциплины:\n")

            for subj, grade in student.grades.items():
                dept_name = "Не закреплена"
                for dept in self.departments:
                    if dept.check_subject(student.major, subj):
                        dept_name = dept.name
                        break
                f.write(f"- {subj.name} (Кафедра: {dept_name}) — Оценка: {grade}\n")

            
            f.write(f"Средний балл: {student.get_average_grade():.2f}\n")

        print(f"Ведомость сохранена в файл {filename}")
        return filename

