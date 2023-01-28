class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    text = input()

    if text == "End":
        break

    if "@" not in text:
        raise MustContainAtSymbolError("Email must contain @")

    name, mail = text.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    mail_provider, domain = mail.split(".")

    if domain not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")