class Credit:

    def __init__(self, cred):
        self.fName = cred['fName']
        self.lName = cred['lName']
        self.address = cred['address']
        self.city = cred['city'],
        self.state = cred['state']
        self.zipCode = cred['zipCode']
        self.cardNumber = cred['cardNumber']
        self.cardType = cred['cardType'] 
        self.cv = cred['cv']
        self.exp = cred['exp']

    def __str__(self):
        return "------- Credit -------\nAddress: {}\nCity: {}\State: {}\nZip: {}\nCard#: {}\ntype: {}\nCv: {}\nExp: {}\n".format(self.address, self.city, self.state, self.zipCode, "*****"+ self.cardNumber[-4:], self.cardType, self.cv, self.exp)