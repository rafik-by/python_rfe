class FacultyError(Exception):
    """Базовый класс для всех исключений системы управления факультетом."""
    pass


class StudentNotFoundError(FacultyError):
    """Вызывается, если студент с указанным ID не найден."""
    pass


class StudentAlreadyExistsError(FacultyError):
    """Вызывается при попытке зачислить студента с уже существующим ID."""
    pass


class MajorNotFoundError(FacultyError):
    """Вызывается, если указанной специальности нет на факультете."""
    pass


class CourseNotAllowedError(FacultyError):
    """Вызывается, если ни одна кафедра не читает курс для специальности студента."""
    pass


class NotEnrolledError(FacultyError):
    """Вызывается при действиях с курсом, на который студент не записан."""
    pass


class InvalidGradeError(FacultyError):
    """Вызывается при попытке выставить оценку вне допустимого диапазона."""
    pass


class SemesterTransferError(FacultyError):
    """Вызывается, если студент не выполнил условия для перевода в следующий семестр."""
    pass