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
        zp_day = self.salary_f_day * day
        print(zp_day)
        return zp_day



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

a = Programmer("Artur", "Ryhas", "dafa", "a42424", 10)
r = Recruiter("Oleg", "Ryhas", "dafa", "a42424", 20)
print(a.work())
print(r.work())
print(a)
print(r)