from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to the database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to the json')


# class PersonDB:
#     def save_to_db(self, person):
#         print(f'Save the {person} to the database')
#
#     def save_to_json(self, person):
#         print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('Irfan')
    db = PersonDB()
    db.save(p)
    js = PersonJSON()
    js.save(p)
    # db.save_to_db(p)
    # db.save_to_json(p)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
