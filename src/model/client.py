
class Client:
    def __init__(self, credit, email, phone):
        self.email = email
        self.phone = phone
        self.fName = credit.fName
        self.lName = credit.lName
        self.credit = credit
    def __str__(self):
        return"------- Client -------\nFirst Name: {}\nLast Name: {}\nEmail: {}\nPhone: {}\n{}".format(self.fName, self.lName,self.email, self.phone, self.credit)