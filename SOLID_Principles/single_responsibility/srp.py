class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    # @classmethod
    # def save(cls, person):
    #     print(f'Save the {person} to the database')


class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    person = Person('irfan')
    db = PersonDB()
    db.save(person)
    # Person.save(person)
