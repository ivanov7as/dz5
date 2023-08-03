def dict(name_list, salary_list, premium_list):
    return {name: salary * (1 + int(premium.strip('%')) / 100) for name, salary, premium in
            zip(name_list, salary_list, premium_list)}


name = ["Ivanov", "Petrov", "Sidorov"]
salary = [1000, 2000, 3000]
premium = ["10", "20", "25%"]

print(dict(name, salary, premium))
