from sys import argv

script_name, work_in_hours, salary_one, bonus = argv

pay = (int(work_in_hours) * int (salary_one) + int(bonus))
print (pay)
