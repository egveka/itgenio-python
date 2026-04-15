class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email
    
    def get_email(self):
        return self.__email
    
    # todo: email should be passed as parameter
    def set_email(self, email):
        if email.count("@") == 1 and "." in email \
            and email.find(".") > email.find("@"):
            return email
        elif self.get_email:
            return "Invalid email!"

k = UserMail("snowhite227", "prince@wait.you")
print(k.set_email("princes@wait.you"))