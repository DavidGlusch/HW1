from email_validator import validate_email, EmailNotValidError


class A:
    def __init__(self, x):
        self.validate(x)

    def validate(self, email):
        try:
            validate_email(email)
            print('Email is valid')
        except EmailNotValidError:
            print('Email is not valid')


test1 = A
test1("1234.com")
test1("abc@asdw.com")

