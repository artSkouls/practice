import time

from models.EmployeeClass import Employee
from models.RecruiterClass import Recruiter
from models.Programmer import Programmer
from models.CandidateClass import Candidate


def main():
    time_string = int(time.strftime("%d"))

    a = Programmer("Artur", "Ryhas", "dafa", "42424", 100)
    r = Recruiter("Oleg", "Ryhas", "dafa", "42424", 20000)
    print(a.work())
    print(r.work())
    print(a)
    print(r)
    print(a.comparison(a.salary_f_day, r.salary_f_day, a.name, a.surname, r.name, r.surname))
    print(a.check_salary(time_string))
    print(r.check_salary(time_string))


if __name__ == '__main__':
    main()
