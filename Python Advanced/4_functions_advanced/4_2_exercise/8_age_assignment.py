def age_assignment(*args, **kwargs):

    res = []

    for name in sorted(args):
        if name[0] in kwargs.keys():
            age = kwargs[name[0]]

            res.append(f"{name} is {age} years old.")

    return "\n".join(res)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))