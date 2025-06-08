# Часть 1: bool
> [!IMPORTANT]  
> для всех проверок использовать `True` и `False`.

1) Написать программму, которая проверяет права доступа к контенту; пользователь должен быть старше 12 лет **и** иметь подписку
- запрашивает возраст и наличие подписки (yes/no) пользователя
- выводит `True` если доступ разрешен и `False` если запрещен
2) Написать программу, которая проверяет пароль по критериям:
- длина больше 8 символов,
- содержит хотя бы одну цифру,
- содержит заглавную букву

Если пароль валиден, то вывести `You password is strong`; в противном случае `You password is weak`\
Для реализации пригодится функция [any()](https://letpy.com/handbook/builtins/any/) 

3) Написать програму, которая проверяет, принадлежит ли точка с координатами (x, y) кругу радиуса r с центром в (0, 0)
- координаты точки (x, y) запросить у пользователя
- радиус r задать константой, равной 10
- точка принадлежит кругу, если выполняется условие 
<img width="115" alt="image" src="https://github.com/user-attachments/assets/da0cd08d-75ad-4cd4-b5a6-9f78eff51625" />

4) Написать программу, которая проверяет, может ли существовать треугольник с сторонами a, b, c. Условие существования треугольника: сумма любых двух сторон должна быть больше третьей.

# Часть 2: словари
1) Задан словарь
```
address_book = {
  'Jerry': 'mousejerry@gmail.com',
  'Boss': 'mralien@company.com',
  'Spamer': 'hotchicks@gmail.com',
  'Greg': 'superuser013@yahoo.com'
}
```
- удалить из словаря контакт спамера
- вывести словарь в формате
```
#1 Jerry - mousejerry@gmail.com
#2 Boss - mralien@company.com
#3 Greg - superuser013@yahoo.com
```
- добавить в словарь новый контакт `Guido` со значением `guido@python.org`
2) Создать словарь, который описывает человека:
- имя - `Tom`
- возраст - `30`
- место работы - `Anestesia Tech`
- отдел - `PR`
- навыки - `copywriting`, `project management`, `lead generation`
Вывести словарь на экран в формате
```
name: Tom
age: 30
place of work: Anestesia Tech
department: PR
skills:
  - copywriting
  - project management
  - lead generation
```
модифицировать создание словаря таким образом, чтобы все значения запрашивались у пользователя

3) Содать словарь car:
- бренд - Ford
- модель - Mustang
- год выпуска - 1964
Добавить в словарь цвет (значение запросить у пользователя)\
Если цвет НЕ белый ИЛИ черный, то вывести `Wow! You like bright colors!`

4) Задан список словарей
```
cars = [
    {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "black", "price": 25000},
    {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "silver", "price": 30000},
    {"brand": "Tesla", "model": "Model 3", "year": 2023, "color": "white", "price": 45000},
    {"brand": "BMW", "model": "X5", "year": 2020, "color": "blue", "price": 60000},
    {"brand": "Honda", "model": "Civic", "year": 2019, "color": "red", "price": 22000},
    {"brand": "Audi", "model": "A4", "year": 2021, "color": "gray", "price": 42000},
    {"brand": "Mercedes-Benz", "model": "C-Class", "year": 2022, "color": "black", "price": 48000},
    {"brand": "Chevrolet", "model": "Camaro", "year": 2018, "color": "yellow", "price": 32000},
    {"brand": "Hyundai", "model": "Tucson", "year": 2023, "color": "green", "price": 29000},
    {"brand": "Kia", "model": "Sportage", "year": 2021, "color": "orange", "price": 26500}
]
```
- вывести информацию о машинах в формате
```
Ford Mustang (1964)
Toyota Camry (2022)
Tesla Model 3 (2023)
...
```
- вывести все автомобили новее 2020 года
- вывести все черные автомобили
- запросить у пользователя бренд, проверить что такой есть и вывести доступную модель с годом выпуска и ценой; например
```
Enter brand: BMW
Model: X5
Year: 2020
Price: 60000
```
- спросить у пользователя, готов ли он купить машину, которую мы нашли ему в предыдущем пункте и если да, то рассчитать цену с учетом скидки 5%
