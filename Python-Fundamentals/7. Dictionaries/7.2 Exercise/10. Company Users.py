def add_employee(company, emp_id, company_dict):
    company_dict = dict(company_dict)
    if company not in company_dict.keys():
        company_dict[company] = [emp_id]
    else:
        if emp_id not in company_dict[company]:
            company_dict[company].append(emp_id)

    return company_dict


def company_stats(company_dict):
    company_dict = dict(company_dict)
    res = ""
    for key, val in company_dict.items():
        res += f"{key}\n"
        for x in val:
            res += f"-- {x}\n"

    return res


my_dict = {}
while True:
    line = input()
    if line == "End":
        break
    line = line.split(" -> ")
    company_name, user_id = line[0], line[1]
    my_dict = add_employee(company_name, user_id, my_dict)

print(company_stats(my_dict))