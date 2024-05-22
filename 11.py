class Abiturient:
    def __init__(self, aid, last_name, first_name, middle_name, address, phone, grades):
        self.id = aid
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.phone = phone
        self.grades = grades

    def total_grade(self):
        return sum(self.grades)

# Створення масиву об'єктів
abiturients = [
    Abiturient(1, "Климов", "Іван", "Петрович", "вул. Шевченка 10", "123456789", [5, 4, 3, 2, 4]),
    Abiturient(2, "Струков", "Петро", "Сидорович", "вул. Лесі Українки 5", "987654321", [4, 4, 4, 4, 5]),
    # Додайте інших абітурієнтів за потреби
]

# a) список абітурієнтів, які мають незадовільні оцінки
unsatisfactory_grades = [abiturient for abiturient in abiturients if any(grade < 3 for grade in abiturient.grades)]

# b) список абітурієнтів, у яких сума балів вища за задану
def abiturients_with_total_grade_above(abiturients, threshold):
    return [abiturient for abiturient in abiturients if abiturient.total_grade() > threshold]

# c) вибрати задану кількість n абітурієнтів, які мають найвищу суму балів
def top_n_abiturients(abiturients, n):
    sorted_abiturients = sorted(abiturients, key=lambda x: x.total_grade(), reverse=True)
    return sorted_abiturients[:n]

# Приклад виклику функцій
print("a) Список абітурієнтів з незадовільними оцінками:")
for abiturient in unsatisfactory_grades:
    print(abiturient.last_name, abiturient.first_name, abiturient.middle_name)

threshold = 16  # Задана сума балів
print("\nb) Список абітурієнтів зі сумою балів вище", threshold, ":")
for abiturient in abiturients_with_total_grade_above(abiturients, threshold):
    print(abiturient.last_name, abiturient.first_name, abiturient.middle_name)

n = 2  # Задана кількість абітурієнтів з найвищою сумою балів
print("\nc) Топ", n, "абітурієнтів:")
top_n = top_n_abiturients(abiturients, n)
for i, abiturient in enumerate(top_n, 1):
    print(i, ".", abiturient.last_name, abiturient.first_name, abiturient.middle_name, "-", abiturient.total_grade(), "балів")

