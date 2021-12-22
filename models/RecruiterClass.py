from models.EmployeeClass import Employee


class Recruiter(Employee):
    position = "Recruiter"

    def __str__(self):
        return f"{self.position}: {self.name} {self.surname}"

    @staticmethod
    def work():
        return "I come to the office and start hiring"
