from  interface.user import UserInterFace

class UserImp(UserInterFace):
    def __init__(self):
        self.username = None
        # self.user_id = None
        self.dob = None
        self.gender = None
        self.identity = None
        self.phone = None
        self.email = None
        self.password = None

    def create_user(self, username, password, dob, gender, identity, phone, email):
        self.username = username
        self.phone = phone
        self.password = password
        self.gender = gender
        self.identity = identity
        self.dob = dob
        self.email = email
        # self.generate_user_id()

    def get_user_details(self):
        return self
    #
    # def generate_user_id(self):
    #     self.user_id = str(self.username[0:2] + '_' + self.phone[:4])
    #