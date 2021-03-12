# task1
class Car:
    license = 'hello'

    def __init__(self,
                 id='0',
                 carBrand='BMW',
                 model='X5',
                 yearOfIssue='2015',
                 color='black',
                 price='150000',
                 registryNumber='1234'):
        self.__id = id
        self.__carBrand = carBrand
        self.__model = model
        self.__yearOfIssue = yearOfIssue
        self.__color = color
        self.__price = price
        self.__registryNumber = registryNumber

    """def __del__(self):
        print('Вызван деструктор')"""

    def __setattr__(self, attr, value):
        if attr != 'license':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_car_brand(self, carBrand):
        self.__carBrand = carBrand

    def get_car_brand(self):
        return self.__carBrand

    def set_car_model(self, model):
        self.__model = model

    def get_car_model(self):
        return self.__model

    def set_year_of_issue(self, yearOfIssue):
        self.__yearOfIssue = yearOfIssue

    def get_year_of_issue(self):
        return self.__yearOfIssue

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_price(self, price):
        self.__price == price

    def get_price(self):
        return self.__price

    def set_registry_number(self, registryNumber):
        self.__registryNumber == registryNumber

    def get_registry_number(self):
        return self.__registryNumber


car_list = [
    Car(),
    Car('1', 'Mercedes', 'AMG GT', '2020', 'black', '117410', '1221'),
    Car('2', 'Opel', 'Cadet', '2010', 'red', '15000', '1223'),
    Car('3', 'BMW', 'X5', '2015', 'black', '150000', '1234'),
    Car('4', 'Mercedes', 'C-Class Couple', '2018', 'black', '38300', '1111'),
    Car('5', 'Opel', 'Astra', '2010', 'blue', '16000', '2223'),
    Car('6', 'Mercedes', 'A-Class', '2020', 'white', '1117410', '1226'),
    Car('7', 'Mercedes', 'AMG GT', '2020', 'grey', '117110', '1261')
]


def print_list(obj_list, param):
    if len(obj_list) > 0:
        print(f'Result by parameter {param}:')
        for obj in obj_list:
            print(obj_list[obj.get_car_brand()], ' - ', obj.get_car_model())
        return


def show_result(arg, lambda_exp):
    filter_result = list(filter(lambda_exp, car_list))
    print(filter_result, arg) if len(filter_result) > 0 else print('Car not found')


car_brand_request = input('Enter car brand: \n')
show_result(car_brand_request, lambda x: x.get_car_brand() == car_brand_request)


car_model_request = input('Enter the car model: \n')
show_result(car_model_request, lambda x: x.get_car_model() == car_model_request)


year_request = input('Enter the car year: \n')
show_result(year_request, lambda x: x.get_year_of_issue() == year_request)

