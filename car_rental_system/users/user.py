class User:
    def __init__(self):
        self.user_id = ''
        self.username = ''
        self.driving_license = ''

    def create_user(self, user_id):
        self.user_id = user_id

    def set_user_name(self, user_name):
        self.username = user_name

    def add_driving_license(self, driving_license):
        self.driving_license = driving_license

    def get_user_name(self):
        return self.username

    def get_user_id(self):
        return self.user_id

    def get_user_licence(self):
        return self.driving_license
