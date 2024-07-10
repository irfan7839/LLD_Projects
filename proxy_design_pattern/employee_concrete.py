from LLD_Projects.proxy_design_pattern.employee_interface import EmployeeTable


class EmployeeTableImp(EmployeeTable):

    def create_employee(self, client, name):
        print('created new role in employee table')
        pass

    def delete_employee(self, client, emp_id):
        print(f'deleted role with employee id: {emp_id} from employee table')
        pass

    def get_employee(self, client, emp_id):
        print('fetching data from employee table')
        pass
