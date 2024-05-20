class Players:
    def __init__(self):
        self.name = ''
        self.user_id = ''
        self.gender = ''

    def create_player(self, name, user_id, gender):
        self.name = name
        self.user_id = user_id
        self.gender = gender
        print("User created successfully")
