from LLD_Projects.proxy_design_pattern.employee_concrete import EmployeeTableImp
from LLD_Projects.proxy_design_pattern.employee_interface import EmployeeTable
from LLD_Projects.proxy_design_pattern.employee_proxy import EmployeeTableProxy


class Main:
    @staticmethod
    def start():
        try:
            emp_table_obj = EmployeeTableProxy()
            emp_table_obj.create_employee('ADMIN', EmployeeTableImp())
            print('operation successful')
        except Exception as e:
            print(e)


main = Main()
main.start()
