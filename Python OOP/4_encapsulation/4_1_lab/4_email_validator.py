class EmailValidator:
    def __init__(self, min_length: int, e_mails: list, domain: list):
        self.min_length = min_length
        self.mails = e_mails
        self.domains = domain

    def __is_name_valid(self, name: str):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain: str):
        return domain in self.domains

    def validate(self, email: str):

        name, other = email.split('@')
        mail, domain = other.split(".")

        return all([self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)])


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

