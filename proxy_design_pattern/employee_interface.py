from abc import ABC, abstractmethod


class EmployeeTable(ABC):
    def __init__(self):
        self.id = None
        self.name = None
        self.emp_type = None
        self.age = None

    @abstractmethod
    def create_employee(self, client, emp_obj):
        pass

    @abstractmethod
    def delete_employee(self, client, emp_id):
        pass

    @abstractmethod
    def get_employee(self,client,  emp_id):
        pass
