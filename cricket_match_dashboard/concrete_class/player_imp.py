from interfaces.players import Player


class PlayerImp(Player):
    def __init__(self):
        self.name = ''
        self.age = 0
        self.email = None
        self.phone = None
        self.id = None

    def create_player(self, player_id):
        name = input("enter player's name")
        age = input("enter player's age")
        email = input("enter player's email")
        phone = input("enter player's phone")
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.id = player_id

    def print_detail(self):
        return f"player name {0} age {1} email {2} and phone {3} created successfully!".format(self.name, self.age
                                                                                               , self.email, self.phone)
