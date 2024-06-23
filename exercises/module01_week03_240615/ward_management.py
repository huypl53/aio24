from datetime import datetime
from typing import List, Type


class Person:
    def __init__(self, name: str, yob: int) -> None:
        self._name = name
        self._yob = yob

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @name.getter
    def name(self):
        return self._name

    @property
    def yob(self):
        return self._yob

    @yob.setter
    def yob(self, value: int):
        self._yob = value

    @yob.getter
    def yob(self):
        return self._yob

    @property
    def age(self):
        return datetime.now().year - self._yob

    def describe(self):
        attrs = {k.replace("_", "").capitalize(): v for k,
                 v in self.__dict__.items()}
        attrs_str = [f"{k}: {v}" for k, v in attrs.items()]
        print(f'{self.__class__.__name__}{" - ".join(attrs_str)}')


class Student(Person):
    def __init__(self, *args, grade: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value: str):
        self._grade = value

    @grade.getter
    def grade(self):
        return self._grade


class Teacher(Person):
    def __init__(self, *args, subject: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._subject = subject

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value: str):
        self._subject = value

    @subject.getter
    def subject(self):
        return self._subject


class Doctor(Person):
    def __init__(self, *args, specialist: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._specialist = specialist

    @property
    def specialist(self):
        return self._specialist

    @specialist.setter
    def specialist(self, value: str):
        self._specialist = value

    @specialist.getter
    def specialist(self):
        return self._specialist


class Ward:
    def __init__(self, name: str, residents: List[Person]) -> None:
        self._name = name
        self._residents = residents
        if residents is None:
            self._residents = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @name.getter
    def name(self):
        return self._name

    def add_person(self, p: Person):
        self._residents.append(p)

    def describe(self):
        print(f"Ward name: {self._name}")
        for p in self._residents:
            p.describe()

    def __get_person_by_type(self, person_type: Type[Person]):
        return [p for p in self._residents if isinstance(p, person_type)]

    def count_docter(self):
        return len(self.__get_person_by_type(Doctor))

    def sort_age(self):
        self._residents = sorted(
            self._residents, key=lambda p: p.yob, reverse=True)

    def calc_average_teacher_age(self):
        teachers = self.__get_person_by_type(Teacher)
        return sum([t.age for t in teachers]) / len(teachers)

    def calc_average_teacher_yob(self):
        teachers = self.__get_person_by_type(Teacher)
        return sum([t.yob for t in teachers]) / len(teachers)


if __name__ == "__main__":
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    student1.describe()
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher1.describe()
    doctor1 = Doctor(name=" doctorA ", yob=1945,
                     specialist=" Endocrinologists ")
    doctor1.describe()
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = Ward(name=" Ward1 ")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    print(f"Number of doctors: { ward1.count_docter() }")

    print("After sorting Age of Ward1 people ")
    ward1.sort_age()
    ward1.describe()

    print(
        f"Average year of birth ( teachers ): { ward1 . calc_average_teacher_yob ()}")
