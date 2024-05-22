class Abiturient:
    """
    Class to describe information about an applicant.

    Attributes:
      id: Unique identifier of the applicant.
      прізвище: Surname of the applicant.
      ім'я: Name of the applicant.
      по_батькові: Patronymic of the applicant.
      адреса: Address of the applicant.
      телефон: Phone number of the applicant.
      оцінки: List of the applicant's grades.
    """
    def __init__(self, id, прізвище, ім_я, по_батькові, адреса, телефон, оцінки):
        self.id = id
        self.прізвище = прізвище
        self.ім_я = ім_я
        self.по_батькові = по_батькові
        self.адреса = адреса
        self.телефон = телефон
        self.оцінки = оцінки

    def __str__(self):
        return f"{self.прізвище} {self.ім_я} {self.по_батькові}"

    def get_sum_of_scores(self):
        return sum(self.оцінки)


class EducationalProgram:
    """
    Class to describe an educational program.

    Attributes:
      name: Name of the educational program.
      limit: Limit of the number of applicants who can be enrolled.
    """
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.applications = []

    def add_application(self, application):
        if len(self.applications) < self.limit:
            self.applications.append(application)
            return True
        else:
            return False

    def process_applications(self):
        self.applications.sort(key=lambda app: app.abiturient.get_sum_of_scores(), reverse=True)
        return self.applications[:self.limit]


class AdmissionApplication:
    """
    Class to describe an admission application.

    Attributes:
      абітурієнт: Applicant who submitted the application.
      програма: Educational program to which the application is submitted.
    """
    def __init__(self, абітурієнт, програма):
        self.abiturient = абітурієнт
        self.program = програма

    def __str__(self):
        return f"{self.abiturіent} - {self.program.name}"


class University:
    """
    Class to describe a university.

    Attributes:
      name: Name of the university.
      programs: List of educational programs of the university.
    """
    def __init__(self, name):
        self.name = name
        self.programs = []

    def add_program(self, program):
        self.programs.append(program)

    def process_admissions(self):
        admission_orders = {}
        for program in self.programs:
            admission_orders[program.name] = program.process_applications()
        return admission_orders


# Example usage

if name == "__main__":
    # Create a university
    university = University("National University")

    # Add educational programs
    program1 = EducationalProgram("Computer Science", 3)
    program2 = EducationalProgram("Engineering", 2)
    university.add_program(program1)
    university.add_program(program2)

    # Create applicants
    abiturient1 = Abiturient(1, "Сидоренко", "Сидір", "Петрович", "vul. Heroiv Dnipra, 25", "+380997654321", [3, 3, 4, 5, 4])
    abiturient2 = Abiturient(2, "Киселева", "Марія", "Олександрівна", "vul. Franka, 10", "+380957654321", [4, 5, 4, 5, 4])
    abiturient3 = Abiturient(3, "Мартинова", "Ольга", "Сергіївна", "vul. Lenina, 30", "+380931234567", [5, 5, 5, 5, 5])
    abiturient4 = Abiturient(4, "Волошенюк", "Ігор", "Миколайович", "vul. Kozatska, 20", "+380991234567", [4, 4, 4, 4, 4])

    # Submit applications to educational programs
    application1 = AdmissionApplication(abiturient1, program1)
    application2 = AdmissionApplication(abiturient2, program1)
    application3 = AdmissionApplication(abiturient3, program1)
    application4 = AdmissionApplication(abiturient4, program2)

    # Add applications to educational programs
    program1.add_application(application1)
    program1.add_application(application2)
    program1.add_application(application3)
    program2.add_application(application4)

    # Process applications and generate admission orders
    admission_orders = university.process_admissions()
    # Print admission orders
    print("Admission Orders:")
    for program_name, applications in admission_orders.items():
        print(f"\nEducational Program: {program_name}")
        for application in applications:
            print(application)
