import numpy as np


np.random.seed(42)


num_students = 22
subjects = ["Матан", "Физика", "Программирование", "Английский", "История"]
students = [f"Студент_{i + 1}" for i in range(num_students)]


possible_grades = [4, 5, 6, 7, 8, 9, 10]
probabilities = [0.08, 0.14, 0.16, 0.18, 0.18, 0.16, 0.10]
grades = np.random.choice(possible_grades, size=(num_students, len(subjects)), p=probabilities)


assert grades.shape == (num_students, len(subjects)), "Неверный размер таблицы оценок!"
assert np.all((grades >= 1) & (grades <= 10)), "Оценки выходят за пределы 1..10!"

print("    ТАБЛИЦА ОЦЕНОК  ")
header = f"{'Студент':<12} | " + " | ".join(f"{subj:<16}" for subj in subjects)
print(header)
for name, row in zip(students, grades):
    row_str = " | ".join(f"{mark:<16}" for mark in row)
    print(f"{name:<12} | {row_str}")


student_avg = np.mean(grades, axis=1)

print("\n     СРЕДНИЙ БАЛЛ СТУДЕНТОВ    ")
for name, avg in zip(students, student_avg):
    print(f"{name:<12}: {avg:.2f}")


max_avg = np.max(student_avg)
min_avg = np.min(student_avg)

best_indices = np.where(student_avg == max_avg)[0]
worst_indices = np.where(student_avg == min_avg)[0]

print(f"\nЛучший средний балл ({max_avg:.2f}):", ", ".join(students[i] for i in best_indices))
print(f"Худший средний балл ({min_avg:.2f}):", ", ".join(students[i] for i in worst_indices))


subject_avg = np.mean(grades, axis=0)

print("\n=== СРЕДНИЙ БАЛЛ ПО ПРЕДМЕТАМ ===")
for subj, avg in zip(subjects, subject_avg):
    print(f"{subj:<18}: {avg:.2f}")

easiest_idx = np.argmax(subject_avg)
hardest_idx = np.argmin(subject_avg)

print(f"\nСамый простой предмет: {subjects[easiest_idx]} (средний балл {subject_avg[easiest_idx]:.2f})")
print(f"Самый сложный предмет: {subjects[hardest_idx]} (средний балл {subject_avg[hardest_idx]:.2f})")


scholarship_fund = 4000.0

conditions = [
    (student_avg >= 5.0) & (student_avg < 6.0),
    (student_avg >= 6.0) & (student_avg < 8.0),
    (student_avg >= 8.0) & (student_avg < 9.0),
    (student_avg >= 9.0) & (student_avg <= 10.0),
]
multipliers = [1.0, 1.2, 1.4, 1.6]

weights = np.select(conditions, multipliers, default=0.0)

print(f"\n    РАСПРЕДЕЛЕНИЕ СТИПЕНДИАЛЬНОГО ФОНДА ({scholarship_fund:.2f} BYN) ")
total_weight = np.sum(weights)

if total_weight == 0:
    print("Никто из студентов не прошёл на стипендию (у всех средний балл ниже 5.0).")
    scholarships = np.zeros(num_students)
else:
    scholarships = (weights / total_weight) * scholarship_fund
    recipients_count = np.count_nonzero(scholarships > 0)

    for i in range(num_students):
        if scholarships[i] > 0:
            print(
                f"{students[i]:<12} | ср. балл {student_avg[i]:<5.2f} | "
                f"коэфф. {weights[i]:.1f}x | {scholarships[i]:.2f} BYN"
            )

    distributed_sum = np.sum(scholarships)
    assert np.isclose(distributed_sum, scholarship_fund), "Сумма выплат не совпадает с фондом!"
    print(f"\nВсего стипендиатов: {recipients_count} из {num_students}")
    print(f"Итого распределено: {distributed_sum:.2f} BYN (совпадает с фондом).")