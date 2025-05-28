def show_employee(name, salary):
    frame = '*$' * (len(name) + len(str(salary)) + 15)
    print(frame)
    print(f"--- Имя: {name} Зарплата: {salary} ---")
    print(frame)


def calculate_total_salary(employees):
    return sum(employee['salary'] for employee in employees)


def start():
    show_employee("Иван Иванов", 50000)


    employees = [
        {"name": "Иван Иванов", "salary": 50000},
        {"name": "Петр Петров", "salary": 60000},
        {"name": "Сидор Сидоров", "salary": 70000}
    ]
    total = calculate_total_salary(employees)
    print(f"\n<<< Общая зарплата всех сотрудников: {total} >>>")


if __name__ == "__main__":
    start()