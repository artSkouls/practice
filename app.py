import time

from models.EmployeeClass import Employee
from models.RecruiterClass import Recruiter
from models.Programmer import Programmer
from models.CandidateClass import Candidate
from models.Vacancy import Vacancy


def main():
    time_string = int(time.strftime("%d"))

    a = Programmer("Artur", "Ryhas", "gogo", "42424", 100)
    r = Recruiter("Oleg", "Ryhas", "mon", "42424", 20000)
    r1 = Recruiter("Semen", "Ivanov", "email", "number", 40)
    a1 = Programmer("Anton", "Lomov", "dafa", "42424", 101)
    a2 = Programmer("Mykola", "Vaschuk", "dafa", "42424", 102)
    k1 = Candidate(
        "Vlad Makarenko", "email", "technologies", "main_skill", "main_skill_grade"
    )
    k2 = Candidate(
        "Mykhailo Jovtyi", "email", "technologies", "main_skill", "main_skill_grade"
    )
    k3 = Candidate(
        "Egor Terekhov", "email", "technologies", "main_skill", "main_skill_grade"
    )
    v1 = Vacancy("TeamLead", "main_skill", "main_skill_level")
    v2 = Vacancy("Lawyer", "main_skill", "main_skill_level")
    print(a.work())
    print(r.work())
    print(a)
    print(r)
    print(
        a.comparison(
            a.salary_f_day, r.salary_f_day, a.name, a.surname, r.name, r.surname
        )
    )
    print(a.check_salary(time_string))
    print(r.check_salary(time_string))
    print(r1)
    print(a1)
    print(a2)
    print(k1)
    print(k2)
    print(k3)
    print(v1)
    print(v2)


if __name__ == "__main__":
    main()
