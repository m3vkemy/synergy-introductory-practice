from datetime import datetime

# Запрашивает у пользователя день, месяц и год рождения, проверяя корректность введённых данных.
# Возвращает дату рождения.
def get_user_birthday():
    while True:
        try:
            day = int(input("Введите день вашего рождения (1-31): "))
            month = int(input("Введите месяц вашего рождения (1-12): "))
            year = int(input("Введите год вашего рождения: "))
            datetime(year, month, day)
            return day, month, year
        except ValueError:
            print("Неверно введённые данные. Попробуйте снова.")

# Определяет день недели, в который родился пользователь.
# Возвращает строку с днем недели.
def day_of_week(day, month, year):
    date = datetime(year, month, day)
    days = {
        0: "в понедельник",
        1: "во вторник",
        2: "в среду",
        3: "в четверг",
        4: "в пятницу",
        5: "в субботу",
        6: "в воскресенье"
    }
    return days[date.weekday()]

# Определяет, является ли год рождения пользователя високосным.
# Возвращает True если год високосный и False если нет.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
# Вычисляет текущий возраст пользователя.
# Возвращает возраст в годах.
def calculate_age(day, month, year):
    today = datetime.today()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

# Определяет правильное склонение слова "год" в зависимости от возраста.
# Возвращает строку с возрастом и правильным склонением.
def get_age_declension(age):
    if 11 <= age % 100 <= 14:
        return f"{age} лет"
    elif age % 10 == 1:
        return f"{age} год"
    elif 2 <= age % 10 <= 4:
        return f"{age} года"
    else:
        return f"{age} лет"

# Выводит дату рождения прорисованную звездочками (*).
def print_date_in_stars(day, month, year):
    digits = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***']
    }

    date_str = f"{day:02d} {month:02d} {year:04d}"
    for row in range(5):
        line = ""
        for char in date_str:
            if char == ' ':
                line += "   "
            else:
                line += digits[char][row] + " "
        print(line)

# Основная функция программы, которая координирует выполнение всех других функций и взаимодействие с пользователем.
def main():
    while True:
        day, month, year = get_user_birthday()

        # Выводим в какой день недели родился пользователь.
        dow = day_of_week(day, month, year)
        print(f"Вы родились {dow}.")

        # Выводим, был ли год рождения пользователя вискокосным.
        leap_year = is_leap_year(year)
        print(f"{year} год {'был' if leap_year else 'не был'} високосным.")

        # Выводим возраст пользователя.
        age = calculate_age(day, month, year)
        age_str = get_age_declension(age)
        print(f"Вам сейчас {age_str}.")

        # Выводим дату рождения пользователя звездочками (*).
        print("Дата вашего рождения:")
        print_date_in_stars(day, month, year)

        # Спрашиваем пользователя, хочет ли он ввести другую дату?
        while True:
            another = input("Хотите ввести другую дату? (да/нет): ").strip().lower()
            if another in ['да', 'нет']:
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")
        if another == 'нет':
            break

if __name__ == "__main__":
    main()
