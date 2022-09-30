"""1"""
# list_1 = ["1" "2" "3" "5" "7" "4"]
#
# list_1.sort()
#
# str_a = str(list_1)
#
# second = str_a[0]
# first = str_a[1]
# third = str_a[2]
# fourth = str_a[3]
# hount = str_a[4]
# goik = str_a[5]
#
# set_a = set()
# for num in str_a:
#     set_a.add(num)
#
#
# # set_a.add(first)
# # print(set_a)
#
# if len(set_a) == 6:
#     print('Цифры уникальные')
# else:
#     print("есть повторения")

"""2"""
# list_1 = [13, 54, 18, 30]
#
# list_1.sort()
#
# namber = [x + 0 for x in list_1 if x % 2 != 0]
#
# print(namber)
#
# max_namber = max(namber)
#
# print(max_namber)

"""3"""
# list_1 = [1, -65, 45, -25, 32, 69]
#
# nam = [x + 0 for x in list_1 if x < 0]
#
# print(nam)

"""4"""
# list_1 = [1, 2, 8, 11, 45, 18, 36, 98, 12]
#
# list_1.sort()
#
# namber_ = [x + x for x in list_1 if x % 2 != 0]
#
# print(namber_)
#
# max_nambers = max(namber_)
#
# print(max_nambers)
#
# namber_.pop(2)
#
# print(namber_)

"""5"""
# list_1 = [5, 6, 9, 11, 18, 36, 69, 74, 92]
#
# namber = [x + 0 for x in list_1 if x % 2 == 0]
#
# print(namber)
#
# min_namber = min(namber)
#
# print(min_namber)


"""_1_"""
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = int(a)
#         self.b = int(b)
#         self.c = int(c)
#
#     def __koordinat__(self, koordinat):
#         print(f"Кордината равна: {self.a}, Кордината равна: {self.b}, Кордината равна: {self.c}")
#
#     def perimetr_(self, perimetr):
#         print(f"Периметр равен: {self.a + self.b + self.c }")
#
#     def triangles_(self, triangle_a, triangle_b, triangle_c):
#         if self.a + self.b and self.b + self.c and self.a and self.c:
#             print("Треугольник равностороний")
#         elif self.a + self.b and self.b + self.c != self.a + self.c:
#             print("Треугольник равнобедренный ")
#         else:
#             print("Треугольник произвольный")
#
# my_Triangle = Triangle("14", "7", "5")
# my_Triangle.__koordinat__(1)
# my_Triangle.perimetr_(1)
# my_Triangle.triangles_(4, 5, 3)

"""Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели. 
Функции- члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов. Вывести:
a)список рейсов для заданного пункта назначения;
список рейсов для заданного дня недели;."""

# class Airline:
#     def __init__(self, poi_1, namber_train, airline_, tame, day):
#         self.poi_1 = poi_1
#         self.namber_train = namber_train
#         self.airline_ = airline_
#         self.tame = tame
#         self.day = day
#
#     def poi__1(self, lknkmnk):
#         print(f"поезд минск - гомель\nномер рейса 2598\nпасажирский поезд\nвремя отправки 8.30\nпонедельник")
#
#
#     def refand_(self, refand_1):
#         refand_1 = referd_1 = [8.30, 9, 9.30, 10, 10.30, 11]
#         print(f'поезд минск - гомель, начинает ездить с {referd_1[0]} до {referd_1[5]}')
#
#
# my_Airline = Airline("минск - гомель", "номер поезда 2658", "пассажирный", "время отправки 9.30",
#                      "понедельник - пятница")
# my_Airline.poi__1(1)
# my_Airline.refand_(2)

"""Создать класс Student: id, Фамилия, Имя,  Отчество, Дата рождения, Адрес, Телефон, Факультет, Курс, Группа.
 Функции-члены реализуют запись и считывание полей (проверка корректности), 
 расчет возраста студента Создать список объектов. Вывести:
 a) список студентов заданного факультета;
d) список учебной группы."""

# class Student:
#     def __init__(self, last_name, name, dadname, data, namber, classroom, kyrc):
#         self.last_name = last_name
#         self.name = name
#         self.dadname = dadname
#         self.data = data
#         self.namber = namber
#         self.classroom = classroom
#         self.kyrc = kyrc
#
#     def id_(self, l_, n, d):
#         self.last_name = l_
#         self.name = n
#         self.dadname = d
#         if l_ == 'Markovtsov' and n == 'Maxim' and d == 'Anatol':
#             print(f'Добро пожаловать {l_} {n} {d}')
#         else:
#             print(f'По вашей фамилии {l_}, имя {n} и отчество {d} не найденно в базе сведенье ')
#
#     # while True:
#     #     if id_('Markovtsov', 'Maxim', 'Anatol') == id_('Markovtsov', 'Maxim', 'Anatol'):
#     #         print(f'Добро пожаловать')
#     #         break
#
#     def id_1(self, datas, nambers):
#         self.data = datas
#         self.namber = nambers
#         datas = input('Введите свою дату рождения\n')
#         limit = ('01.06.2006')
#
#         if datas < limit:
#             print(f'Извините но ваш возраст {datas} не подходит для обучения в универе')
#         else:
#             print(f'Ваша дата рождения\n{datas}\nВаш возраст подходит для обучения')
#
#         nambers = input('Введите свой номер телефона\n')
#         print(f'Ваш номер телефона {nambers}')
#
#     def id_2(self, classrooms, kyrcc):
#         self.classroom = classrooms
#         self.kyrc = kyrcc
#
#         classrooms = input('какой у вас факультет?\n')
#         matem = ("матем")
#         fizio = ('физ')
#         inf = ('информ')
#         if classrooms == matem:
#             print(f'ваш преподователь по {classrooms} факультету  Александер Анатольевич')
#         elif classrooms == fizio:
#             print(f'ваш преподователь по {classrooms} факультету Владимир Юрьевич')
#         elif classrooms == inf:
#             print(f'ваш преподователь по {classrooms} факультету Владимир Алексеевич')
#         else:
#             print(f'Такого факультета {classrooms} у нас нету')
#
#         kyrcc = int(input('какой у вас курс?\n'))
#         kyrc_1 = 1
#         kyrc_2 = 2
#         kyrc_3 = 3
#         kyrc_4 = 4
#         if kyrcc == kyrc_1:
#             print(f'Ваш курс {kyrcc} и ваш кабинет 1.7')
#         elif kyrcc == kyrc_2:
#             print(f'Ваш курс {kyrcc} и ваш кабинет 2.3')
#         elif kyrcc == kyrc_3:
#             print(f'Ваш курс {kyrcc} и ваш кабинет 1.2')
#         elif kyrcc == kyrc_4:
#             print(f'Ваш курс {kyrcc} и ваш кабинет 2.7')
#         else:
#             print(f'такого курса {kyrcc} нету')
#
#
#
# yniver_student = Student(1, 5, 6, 5, 2, 4, 5)
# yniver_student.id_('Markovtsov', 'Maxim', 'Anatol')
# yniver_student.id_1(1, 1)
# yniver_student.id_2(1, 1)
"""проверенно и сделано верно)))"""

"""Создать класс Customer: id, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, баланс.
 Функции- члены реализуют запись и считывание полей (проверка корректности), зачисление и списание сумм на счет.
Создать список объектов. Вывести:
a)список покупателей в алфавитном порядке;
список покупателей, у которых номер кредитной карточки находится в заданном интервале."""

# class Customer:
#     def __init__(self, surname: str, name: str, lastname: str, address: str, credit_number: int, balance: int):
#         self.surname = surname
#         self.name = name
#         self.lastname = lastname
#         self.address = address
#         self.credit_number = credit_number
#         self.balance = balance
#
#
#     def Check(self, check_, True_False):
#         self.True_False = True_False
#         self.check_ = check_
#         check_ = (self.surname, self.name, self.lastname)
#         print(f'приветствую {check_}')
#         True_False = input(f"Ваш адрес: {self.address}, верно ?\n")
#         if True_False == "да":
#             print(f'Добро пожаловать в наш банк!')
#         else:
#             print(f'Одну секунду, поищу ещё раз')
#
#     def Check_1(self, personal_check):
#         self.personal_check = personal_check
#         personal_check = input('Вы хотите проверить свой лицевой счёт ?\n')
#
#         if personal_check == 'да':
#             print(f'На вашей карте {self.credit_number}, {self.balance} рублей')
#         else:
#             print('Спасибо что зашли в наш банк!')
#
#     def Write_off_of_money(self, help_: int):
#         self.help_ = help_
#
#         self.help_ = input('что вы хотите сделать ?\n'
#                       'снять деньги\nположить\nперевести\nназад, выбор введите пожалуйста цифрой\n')
#         if self.help_ == '1':
#             print('идёт операция подождите')
#             take_off = input('Какую сумму вы хотите снять?\n'
#                         '10 рублей\n5 рублей\nвыбор введите пожалуйста цифрой\n')
#             if take_off == "1":
#                 print(f"с вашей карты снято: 10руб\nна вашей карте: {self.balance - 10 }")
#             elif take_off == '2':
#                 print(f"с вашей карты снято: 5руб\nна вашей карте: {self.balance - 5 }")
#         elif self.help_ == '2':
#             print('идёт операция подождите')
#             put = input('какую сумму вы хотите положить ?\n'
#                         '5 рублей\n10 рублей\nвыбор введите пожалуйста цифрой\n')
#             if put == '1':
#                 print(f'На ваш счёт зачисленно: 5 рублей\nна вашей карте: {self.balance + 5 }')
#             elif put == '2':
#                 print(f'На ваш счёт зачисленно: 10 рублей\nна вашей карте: {self.balance + 10 }')
#         elif self.help_ == '3':
#             print('идёт операция подождите')
#             transfer = input('какую сумму вы хотите перевести ?\n'
#                         '5 рублей\n10 рублей\nвыбор введите пожалуйста цифрой\n')
#             if transfer == "1":
#                 print(f"с вашей карты переведено: 5руб\nна вашей карте: {self.balance - 5 }")
#             elif transfer == '2':
#                 print(f"с вашей карты переведено: 10руб\nна вашей карте: {self.balance - 10 }")
#         else:
#             print('Cпасибо что выбираете наш банк!')
#
#
#
# data_Customer = Customer('марковцов', 'максим', 'анатольевич', 'п.бровки', 69412525, 63)
# data_Customer.Check('True', 'True')
# data_Customer.Check_1("True")
# data_Customer.Write_off_of_money(1)


"""Создать класс Abiturient: id, Фамилия, Имя, Отчество, Адрес, Телефон, Оценки.
Функции-члены реализуют запись и считывание полей (проверка корректности), расчета среднего балла.
Создать список объектов. Вывести:
a)список абитуриентов, имеющих неудовлетворительные оценки;
список абитуриентов, у которых сумма баллов выше заданной;"""

# class Abiturient:
#     def __init__(self, surname: str, name: str, lastname: str, address: str, telephone: int, *grades: int):
#         self.surname = surname
#         self.name = name
#         self.lastname = lastname
#         self.address = address
#         self.telephone = telephone
#         self.grades = grades
#
#     def Check(self, grades_1: int, grades_2: int, grades_3: int, grades_4: int, sum_grades_1: int):
#         self.grades_1 = grades_1
#         self.grades_2 = grades_2
#         self.grades_3 = grades_3
#         self.grades_4 = grades_4
#         self.sum_grades_1 = sum_grades_1
#
#         sum_grades_1 = sum({self.grades_1 + self.grades_2 + self.grades_3 + self.grades_4})
#         print(f'ваш средний бал за математику:{sum_grades_1 / 4}')
#         if sum_grades_1 < 5:
#             print(f'извините но ваш бал {sum_grades_1 / 4} не походит для обучения в нашем коледже(((')
#         else:
#             print(f'ваш бал {sum_grades_1 / 4} походит для обучения в нашем коледже)))')
#
#     def Check_1(self):
#         print(f'{self.surname}   {self.name}  {self.lastname}  {self.address}  {self.telephone}')
#
#
#     def Student_1(self, surname: str, name: str, lastname: str, address: str, telephone: int, *grades: int):
#         self.surname = surname
#         self.name = name
#         self.lastname = lastname
#         self.address = address
#         self.telephone = telephone
#         self.grades = grades
#
#     def Check_(self, grades_1_: int, grades_2_: int, grades_3_: int, grades_4_: int, sum_grades_1_: int):
#         self.grades_1_ = grades_1_
#         self.grades_2_ = grades_2_
#         self.grades_3_ = grades_3_
#         self.grades_4_ = grades_4_
#         self.sum_grades_1_ = sum_grades_1_
#         sum_grades_1_ = sum({self.grades_1_ + self.grades_2_ + self.grades_3_ + self.grades_4_})
#         print(f'ваш средний бал за математику:{sum_grades_1_ / 4}')
#         if sum_grades_1_ < 5:
#             print(f'извините но ваш бал {sum_grades_1_ / 4} не походит для обучения в нашем коледже(((')
#         else:
#             print(f'ваш бал {sum_grades_1_ / 4} походит для обучения в нашем коледже)))')
#
#     def Check_1_(self):
#         print(f'{self.surname}   {self.name}  {self.lastname}  {self.address}  {self.telephone}')
#
#
#     def Student_2(self, surname: str, name: str, lastname: str, address: str, telephone: int, *grades: int):
#         self.surname = surname
#         self.name = name
#         self.lastname = lastname
#         self.address = address
#         self.telephone = telephone
#         self.grades = grades
#
#     def Check__(self, grades_1__: int, grades_2__: int, grades_3__: int, grades_4__: int, sum_grades_1__: int):
#         self.grades_1__ = grades_1__
#         self.grades_2__ = grades_2__
#         self.grades_3__ = grades_3__
#         self.grades_4__ = grades_4__
#         self.sum_grades_1__ = sum_grades_1__
#         sum_grades_1__ = sum({self.grades_1__ + self.grades_2__ + self.grades_3__ + self.grades_4__})
#         print(f'ваш средний бал за математику:{sum_grades_1__ / 4}')
#         if sum_grades_1__ < 5:
#             print(f'извините но ваш бал {sum_grades_1__ / 4} не походит для обучения в нашем коледже(((')
#         else:
#             print(f'ваш бал {sum_grades_1__ / 4} походит для обучения в нашем коледже)))')
#
#     def Check_1__(self):
#         print(f'{self.surname}   {self.name}  {self.lastname}  {self.address}  {self.telephone}')
#
#
#     def Check_3(self):
#         if ((self.grades_1 + self.grades_2 + self.grades_3 + self.grades_4)//4) > 5:
#             print(f'ученик набравший {(self.grades_1 + self.grades_2 + self.grades_3 + self.grades_4)//4} '
#                   f'баллов подойдите пожалуйста в регистратуру для офформления документов на обучения')
#         else:
#             print(f'извините но вы не подходите для бесплатного обучения можете подойти в регистратуру на оформ.заочного')
#         if ((self.grades_1_ + self.grades_2_ + self.grades_3_ + self.grades_4_)//4) > 5:
#             print(f'ученик набравший {(self.grades_1_ + self.grades_2_ + self.grades_3_ + self.grades_4_)//4} '
#                   f'баллов подойдите пожалуйста в регистратуру для офформления документов на обучения')
#         else:
#             print(f'извините но вы не подходите для бесплатного обучения '
#                       f'можете подойти в регистратуру на оформ.заочного')
#         if ((self.grades_1__ + self.grades_2__ + self.grades_3__ + self.grades_4__)//4) > 5:
#             print(f'ученик набравший {(self.grades_1__ + self.grades_2__ + self.grades_3__ + self.grades_4__)//4}'
#                   f' баллов подойдите пожалуйста в регистратуру для офформления документов на обучения')
#         else:
#             print(f'извините но вы не подходите для бесплатного обучения можете подойти в регистратуру на оформ.заочного')
#
#
# school_Abiturient = Abiturient('марковцов', 'максим', 'анатольевич', 'п.бровки', 375292459132, 7, 5, 6, 8)
# school_Abiturient.Student_1('Стипов', 'андрей', 'юрьевич', 'косарева', 375292459133, 7, 2, 6, 5)
# school_Abiturient.Student_2('Столикин', 'артём', 'фёдорович', 'макаёнка', 375292459175, 8, 7, 9, 8)
# school_Abiturient.Check(7, 8, 6, 4, 1)
# school_Abiturient.Check_1()
# school_Abiturient.Check_(6, 9, 8, 7, 1)
# school_Abiturient.Check_1_()
# school_Abiturient.Check__(8, 6, 9, 7, 1)
# school_Abiturient.Check_1__()
# school_Abiturient.Check_3()

"""Создать класс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации. 
Функции-члены реализуют запись и считывание полей (проверка корректности), расчета возраста задания 
(необходимость в кап. ремонте).
Создать список объектов. Вывести:
a)список квартир, имеющих заданное число комнат;
список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке;"""

# class House:
#     def __init__(self, apartment_number: int, square: int, floor: int, number_of_rooms: int,
#                  street: str, building_type: str, validity: int):
#         self.apartment_number = apartment_number
#         self.square = square
#         self.floor = floor
#         self.number_of_rooms = number_of_rooms
#         self.street = street
#         self.building_type = building_type
#         self.validity = validity
#
#     def Check(self, name: str, lastname: str):
#         self.name = name
#         self.lastname = lastname
#
#         print([f'добро пожаловать {self.name} {self.lastname}: номер квартиры {self.apartment_number}:'
#               f' площадь вашей квартиры {self.square}: этаж {self.floor}: {self.number_of_rooms} комнаты:'
#               f' улица {self.street}: {self.building_type}здание: построено {self.validity} лет назад'])
#         if self.validity < 21:
#             print(f'в вашем здании сделаном из {self.building_type}безопасно жить)')
#         elif self.validity > 21 and self.validity < 40:
#             print('ваше здание немного старенькое но ещё можно жить)')
#         elif self.validity > 40:
#             print(f'ваше здание сделано из {self.building_type}уже старое ему бы не помешал ремонт(((')
#
#     def Check_1(self, name: str, lastname: str, apartment_number_1: int, square: int, floor: int, number_of_rooms_1: int,
#                  street: str, building_type: str, validity: int):
#         self.name = name
#         self.lastname = lastname
#         self.apartment_number_1 = apartment_number_1
#         self.square = square
#         self.floor = floor
#         self.number_of_rooms_1 = number_of_rooms_1
#         self.street = street
#         self.building_type = building_type
#         self.validity = validity
#
#         print([f'добро пожаловать {self.name} {self.lastname}: номер квартиры {self.apartment_number_1}:'
#               f' площадь вашей квартиры {self.square}: этаж {self.floor}: {self.number_of_rooms_1} комнаты:'
#               f' улица {self.street}: {self.building_type}здание: построено {self.validity} лет назад'])
#         if self.validity < 21:
#             print(f'в вашем здании сделаном из {self.building_type}безопасно жить)')
#         elif self.validity > 21 and self.validity < 40:
#             print('ваше здание немного старенькое но ещё можно жить)')
#         elif self.validity > 40:
#             print(f'ваше здание сделано из {self.building_type}уже старое ему бы не помешал ремонт(((')
#
#     def Check_2(self, name: str, lastname: str, apartment_number_2: int, square: int, floor: int, number_of_rooms_2: int,
#                  street: str, building_type: str, validity: int):
#         self.name = name
#         self.lastname = lastname
#         self.apartment_number_2 = apartment_number_2
#         self.square = square
#         self.floor = floor
#         self.number_of_rooms_2 = number_of_rooms_2
#         self.street = street
#         self.building_type = building_type
#         self.validity = validity
#
#         print([f'добро пожаловать {self.name} {self.lastname}: номер квартиры {self.apartment_number_2}:'
#               f' площадь вашей квартиры {self.square}: этаж {self.floor}: {self.number_of_rooms_2} комнаты:'
#               f' улица {self.street}: {self.building_type}здание: построено {self.validity} лет назад'])
#         if self.validity < 21:
#             print(f'в вашем здании сделаном из {self.building_type}безопасно жить)')
#         elif self.validity > 21 and self.validity < 40:
#             print('ваше здание немного старенькое но ещё можно жить)')
#         elif self.validity > 40:
#             print(f'ваше здание сделано из {self.building_type}уже старое ему бы не помешал ремонт(((')
#
#     def Check_3(self):
#         if self.floor > 5 and self.floor < 9:
#             print('в промежутке от 5 до 9 этажа находятся такие квартиры как...')
#         if self.number_of_rooms == self.number_of_rooms_1 == self.number_of_rooms_2:
#             print(f'в квартире {self.apartment_number},{self.apartment_number_1} и {self.apartment_number_2}'
#                   f' одинаковое кол-во комнат')
#         elif self.number_of_rooms == self.number_of_rooms_1:
#             print(f'в квартире {self.apartment_number} и {self.apartment_number_1} одинаковое кол-во комнат')
#         elif self.number_of_rooms == self.number_of_rooms_2:
#             print(f'в квартире {self.apartment_number} и {self.apartment_number_2} одинаковое кол-во комнат')
#         elif self.number_of_rooms_1 == self.number_of_rooms_2:
#             print(f'в квартире {self.apartment_number_1} и {self.apartment_number_2} одинаковое кол-во комнат')
#         else:
#             print('в каждой квартире, разное кол-во комнат')
#
#
#
#
#
#
# number_House = House(16, 37, 4, 4, 'п.бровки', 'железа бетона ', 9)
# number_House.Check('максим', 'марковцов')
# number_House.Check_1('вадим', 'сидоренко', 58, 23, 6, 2, 'cвиридова', 'железа бетона', 27)
# number_House.Check_2('давид', 'фелько', 117, 14, 7, 2, 'полевая', 'железа бетона', 50)
# number_House.Check_3()

"""Создать класс Bus:Фамилия и инициалы водителя, Номер автобуса, Номер маршрута, Марка, Год начала эксплуатации,Пробег.
Функции-члены реализуют запись и считывание полей (проверка корректности), вывод возраста автобуса.
Создать список объектов. Вывести:
a)список автобусов для заданного номера маршрута;
список автобусов, которые эксплуатируются больше заданного срока"""

# class Bus:
#     def __init__(self, lastname: str, initials: str, number_bus: int, number_route: int, brand: str,
#                  year_operation: int, mileage: int):
#         self.lastname = lastname
#         self.initials = initials
#         self.number_bus = number_bus
#         self.number_route = number_route
#         self.brand = brand
#         self.year_operation = year_operation
#         self.mileage = mileage
#
#     def Check_1(self):
#         print(f'__Водитель__\n{self.lastname}\n{self.initials}\nНомер автобуса:'
#               f' {self.number_bus}\nНомер маршрута: {self.number_route}\n'
#               f'Марка: {self.brand}\nГод выпуска: {self.year_operation}\nПробег: {self.mileage}')
#
#
#     def Check_2(self, lastname_1: str, initials_1: str, number_bus_1: int, number_route_1: int, brand_1: str,
#                  year_operation_1: int, mileage_1: int):
#         self.lastname_1 = lastname_1
#         self.initials_1 = initials_1
#         self.number_bus_1 = number_bus_1
#         self.number_route_1 = number_route_1
#         self.brand_1 = brand_1
#         self.year_operation_1 = year_operation_1
#         self.mileage_1 = mileage_1
#
#         print(f'__Водитель__\n{self.lastname_1}\n{self.initials_1}\nНомер автобуса:'
#               f' {self.number_bus_1}\nНомер маршрута: {self.number_route_1}\n'
#               f'Марка: {self.brand_1}\nГод выпуска: {self.year_operation_1}\nПробег: {self.mileage_1}')
#
#     def Check_3(self):
#         if self.number_route == self.number_route_1:
#             print(f'------------------\naвтобусы {self.number_bus} и {self.number_bus_1}'
#                   f' едут по одному маршруту {self.number_route}')
#         else:
#             print('------------------\nу каждого автобуса индивидуальный маршрут')
#
#         if self.year_operation < 2005 and self.mileage > 20000 and self.year_operation_1 < 2005 and self.mileage_1 > 20000:
#             print(f'автобусы {self.number_bus} и {self.number_bus_1} эксплуатируются больше срока')
#         elif self.year_operation < 2005 or self.mileage > 20000:
#             print(f'автобус {self.number_bus} эксплуатируется больше срока')
#         elif self.year_operation_1 < 2005 or self.mileage_1 > 20000:
#             print(f'автобус {self.number_bus_1} эксплуатируется больше срока')
#
#
# My_Bus = Bus('Васинькович', 'Андрей Фёдорович', 18, 3, 'Ford', 2004, 54000)
# My_Bus.Check_1()
# My_Bus.Check_2('Сидоренко', 'Олег Пёторович', 12, 2, 'Ford', 2004, 51482)
# My_Bus.Check_3()

"""Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
 (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
  и на них в следующем году тоже будут проценты).
Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму,
 которая будет на счету пользователя."""


# def Bank(a: int, years: int):
#     while True:
#         summa = input('')
#         if :
#             print(f'операция выполняется')
#         break
#
# User_1_Bank = Bank(2585, 5)