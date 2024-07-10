from LLD_Projects.proxy_design_pattern.employee_concrete import EmployeeTableImp
from LLD_Projects.proxy_design_pattern.employee_interface import EmployeeTable


class EmployeeTableProxy(EmployeeTable):
    def __init__(self):
        super().__init__()
        self.emp_obj = EmployeeTableImp()

    def create_employee(self, client, emp_do_obj):
        if client == 'ADMIN':
            self.emp_obj.create_employee(client, emp_do_obj)
            return
        raise Exception('Access Denied')

    def delete_employee(self, client, emp_id):
        if client == 'ADMIN':
            self.emp_obj.delete_employee(client, emp_id)
            return

        raise Exception('Access Denied')

    def get_employee(self, client, emp_id):
        if client == 'ADMIN' or client == 'USER':
            self.emp_obj.get_employee(client, emp_id)
            return

        raise Exception('Access Denied')
    