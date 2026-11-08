from models import Student, Subject, Department
from faculty import faculty
from exceptions import *

major_pi = "Прикладная информатика"
major_kb = "Кибербезопасность"
major_intel = "Интелектуальная электроника"
major_rf = "Радиофизика и информационные технологии"

subject_mat = Subject("Математический анализ", 1)
subject_programing = Subject("Программирование на с++", 1)
subject_agila = Subject("Агилла", 1)
subject_bd = Subject("Базы данных", 2)
subject_orel = Subject("Основы радиоэлектроники", 2)
subject_chm = Subject("Численные методы", 2)
subject_cripto = Subject("Основы криптографии", 3)
subject_ai = Subject("Исскуственный интеллект", 3)
subject_cs = Subject("Компьютерные сети", 3)

department5 = Department("Кафедра интелектуальных систем")
department6 = Department("Кафедра кибербезопасности и информационных технологий")
department4 = Department("Кафедра информатики и компьютерных систем")
department1 = Department("Кафедра радиофизики и цифровых медиа технологий")

subjects_rf = [subject_agila,subject_programing,subject_orel,subject_chm,subject_ai,subject_cs]
department1.add_curriculum(major_rf,subjects_rf)

subjects_intel = [subject_mat, subject_agila, subject_orel, subject_bd, subject_cripto, subject_cs]
department4.add_curriculum(major_intel,subjects_intel)

subjects_pi = [subject_mat,subject_programing, subject_bd, subject_chm, subject_ai, subject_cripto]
department5.add_curriculum(major_pi, subjects_pi)

subjects_kb = [subject_mat,subject_programing,subject_agila,subject_bd,subject_orel,subject_chm,
              subject_cripto,subject_ai,subject_cs]
department6.add_curriculum(major_kb, subjects_kb)

student1 = Student("Александр", 1, 1,major_pi)
student2 = Student("Сергей", 2, 2,major_kb)
student3 = Student("Максим", 3, 1,major_rf)
student4 = Student("Яна", 4, 1, major_intel)



def main():
    rfe = faculty("Faculty of radiophysics and computer technologies")
    rfe.add_major(major_pi)
    rfe.add_major(major_kb)
    rfe.add_major(major_intel)
    rfe.add_major(major_rf)

    rfe.add_department(department1)
    rfe.add_department(department4)
    rfe.add_department(department5)
    rfe.add_department(department6)

    rfe.add_students(student1.student_id, student1)
    rfe.add_students(student2.student_id, student2)
    rfe.add_students(student3.student_id, student3)
    rfe.add_students(student4.student_id, student4)

    rfe.Print()

    while True:
        print(f"1. Зачисление студента на определенную специальность факультета.",
              f"2. Отчисление студента.",
              f"3. Добавление студента для изучения дисциплины",
              f"4. Удаление студента из списка изучающих дисциплину.",
              f"5. Выставление отметки студенту за изученную дисциплину.",
              f"6. Перевод студента в следующий семестр при успешном изучении всех дисциплин.",
              f"7. Сформировать ведомость успеваемости студента.",
              f"0. закончить программу", sep = "\n")
        key = int(input("Введите ключ, чтобы продолжить: ")) 
        match(key):
            case 1:
                majories = {1: "Прикладная информатика", 2: "Кибербезопасность", 3: "Рфиит", 4:"Интэл"}
                print("Выберите специальность для зачисления сутдента:",
                      "1. Прикладная информатика",
                      "2. Кибербезопасность",
                      "3. Рфиит",
                      "4. Интэл", sep = "\n")
                key_major = int(input("Введите ключ: "))
                id_of_student = int(input("Введите id: "))
                if id_of_student in rfe.students:
                    raise StudentAlreadyExistsError("Такой id уже существует")
                match(key_major):
                    case 1:
                        rfe.add_students(id_of_student, Student(input('Введите имя студента: '), id_of_student,
                                        int(input("Введите курс:")), major_pi))
                        print(f"Студент успешно добавлен на {majories[key_major]}")
                        break
                    case 2:
                        rfe.add_students(id_of_student, Student(input('Введите имя студента: '), id_of_student,
                                        int(input("Введите курс:")), major_kb))
                        print(f"Студент успешно добавлен на {majories[key_major]}")
                        break
                    case 3:
                        rfe.add_students(id_of_student, Student(input('Введите имя студента: '), id_of_student,
                                        int(input("Введите курс:")), major_rf))
                        print(f"Студент успешно добавлен на {majories[key_major]}")
                        break
                    case 4:
                        rfe.add_students(id_of_student, Student(input('Введите имя студента: '), id_of_student,
                                                                    int(input("Введите курс:")), major_intel))
                        print(f"Студент успешно добавлен на {majories[key_major]}")
                        break
            case 2:
                checked_id = int(input("Введите id студента на отчисление: "))
                if checked_id not in rfe.students:
                    raise StudentNotFoundError("Студент с таким id не найден!")
                else:
                    del rfe.students[checked_id]

                rfe.Print()
            case 3:
                id_checking_stud = int(input("Введите id проверяемого студента: "))
                print("Выберите предмет который хотите зачислить студенту: ",
                      "1.Математический анализ",
                      "2.Программирование на с++",
                      "3.Агилла",
                      "4.Базы данных",
                      "5.Основы радиоэлектроники",
                      "6.Численные методы",
                      "7.Основы криптографии",
                      "8.Исскуственный интеллект",
                      "9.Компьютерные сети",
                      sep = "\n")
                key_subjects = int(input("Введите ключ для выбора предмета: "))
                rfe.add_subject_to_student(id_checking_stud,subjects_kb[key_subjects-1])
            case 4:
                id_checking_stud = int(input("Введите id проверяемого студента: "))
                print("Выберите предмет который хотите зачислить студенту: ",
                      "1.Математический анализ",
                      "2.Программирование на с++",
                      "3.Агилла",
                      "4.Базы данных",
                      "5.Основы радиоэлектроники",
                      "6.Численные методы",
                      "7.Основы криптографии",
                      "8.Исскуственный интеллект",
                      "9.Компьютерные сети",
                      sep = "\n")
                key_subjects = int(input("Введите ключ для выбора предмета: "))
                rfe.remove_student_from_subject(id_checking_stud,subjects_kb[key_subjects-1])
            case 5:
                id_checking_stud = int(input("Введите id проверяемого студента: "))
                print("Выберите предмет который хотите зачислить студенту: ",
                        "1.Математический анализ",
                        "2.Программирование на с++",
                        "3.Агилла",
                        "4.Базы данных",
                        "5.Основы радиоэлектроники",
                        "6.Численные методы",
                        "7.Основы криптографии",
                        "8.Исскуственный интеллект",
                        "9.Компьютерные сети",
                        sep = "\n")
                key_subjects = int(input("Введите ключ для выбора предмета: "))

                rfe.grade_student(id_checking_stud, subjects_kb[key_subjects-1])
            case 6:
                id_checking_stud = int(input("Введите id проверяемого студента: "))
                rfe.transfer_student_to_next_semester(id_checking_stud)
            case 7:
                id_checking_stud = int(input("Введите id студента для формирования ведомости: "))
                rfe.generate_student_report(id_checking_stud)

            case 0:
                break
            


if __name__ == "__main__":
    main()