from interface.admin import AdminInterface

class AdminImp(AdminInterface):

    def __init__(self):
        self.admin_name = None
        self.dob = None
        self.gender = None
        self.identity = None
        self.phone = None
        self.email = None
        self.password = None

    def create_admin(self, username, password, dob, gender, identity, phone, email):
        self.admin_name = username
        self.phone = phone
        self.password = password
        self.gender = gender
        self.identity = identity
        self.dob = dob
        self.email = email

    def get_admin_details(self):
        return self
