class Applicant:
    """
    Class to describe information about an applicant.

    Attributes:
      id: Unique identifier of the applicant.
      surname: Surname of the applicant.
      name: Name of the applicant.
      patronymic: Patronymic of the applicant.
      address: Address of the applicant.
      phone: Phone number of the applicant.
      grades: List of the applicant's grades.
    """
    def __init__(self, id, surname, name, patronymic, address, phone, grades):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.phone = phone
        self.grades = grades

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def get_sum_of_scores(self):
        return sum(self.grades)


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
        self.applications.append(application)

    def process_applications(self):
        self.applications.sort(key=lambda app: app.applicant.get_sum_of_scores(), reverse=True)
        return self.applications[:self.limit]


class AdmissionApplication:
    """
    Class to describe an admission application.

    Attributes:
      applicant: Applicant who submitted the application.
      program: Educational program to which the application is submitted.
    """
    def __init__(self, applicant, program):
        self.applicant = applicant
        self.program = program

    def __str__(self):
        return f"{self.applicant} - {self.program.name}"


class DuplicateAdmissionException(Exception):
    pass


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
        accepted_applicants = set()

        for program in self.programs:
            try:
                processed_applications = program.process_applications()
                for application in processed_applications:
                    if application.applicant.id in accepted_applicants:
                        raise DuplicateAdmissionException(f"Applicant {application.applicant} is already admitted to another program.")
                    accepted_applicants.add(application.applicant.id)
                admission_orders[program.name] = processed_applications
            except DuplicateAdmissionException as e:
                print(f"Error: {e}")
                # Create a new list of applications excluding already accepted applicants
                program.applications = [app for app in program.applications if app.applicant.id not in accepted_applicants]
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
    applicant1 = Applicant(1, "Sydorenko", "Sydir", "Petrovych", "Heroiv Dnipra St, 25", "+380997654321", [3, 3, 4, 5, 4])
    applicant2 = Applicant(2, "Kiseleva", "Maria", "Oleksandrivna", "Franka St, 10", "+380957654321", [4, 5, 4, 5, 4])
    applicant3 = Applicant(3, "Martynova", "Olga", "Serhiivna", "Lenina St, 30", "+380931234567", [5, 5, 5, 5, 5])
    applicant4 = Applicant(4, "Voloshenyuk", "Ihor", "Mykolaiovych", "Kozatska St, 20", "+380991234567", [4, 4, 4, 4, 4])

    # Submit applications to educational programs
    application1 = AdmissionApplication(applicant1, program1)
    application2 = AdmissionApplication(applicant2, program1)
    application3 = AdmissionApplication(applicant3, program1)
    application4 = AdmissionApplication(applicant4, program2)

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
