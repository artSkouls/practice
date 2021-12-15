import time

time_string = int(time.strftime("%d"))

class Employee:
    def __init__(self, name, surname, email, number, salary_f_day):
        self.name = name
        self.surname = surname
        self.email = email
        self.number = number
        self.salary_f_day = salary_f_day

    @staticmethod
    def work():
        return "I come to the office"

    def check_salary(self, day):
        if day >= 7:
            self.raz = day - 2
        elif day >= 14:
            self.raz = day - 4
        elif day >= 21:
            self.raz = day - 6
        elif day >= 28:
            self.raz = day - 8
        zp_day = self.salary_f_day * self.raz
        return(zp_day)

    @staticmethod
    def comparison(emp1_zp, emp2_zp, n1, s1, n2, s2):
        if emp1_zp > emp2_zp:
            return f"{n1} {s1} получает ЗП больше, чем {n2} {s2}"
        elif emp1_zp < emp2_zp:
            return f"{n2} {s1} получает ЗП больше, чем {n1} {s2}"





class Programmer(Employee):
    position = "Recruiter"
    def __str__(self):
        return f"{self.position}: {self.name} {self.surname}"

    @staticmethod
    def work():
        return "I come to the office and start codding"

class Recruiter(Employee):
    position = "Programmer"
    def __str__(self):
        return f"{self.position}: {self.name} {self.surname}"

    @staticmethod
    def work():
        return "I come to the office and start hiring"

a = Programmer("Artur", "Ryhas", "dafa", "42424", 100)
r = Recruiter("Oleg", "Ryhas", "dafa", "42424", 20000)
print(a.work())
print(r.work())
print(a)
print(r)
print(a.comparison(a.salary_f_day, r.salary_f_day, a.name, a.surname, r.name, r.surname))
print(a.check_salary(time_string))
print(r.check_salary(time_string))