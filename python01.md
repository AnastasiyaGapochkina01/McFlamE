> [!NOTE]  
> Справка

> Переменные предназначены для хранения данных. Название переменной в Python должно начинаться с алфавитного символа или со знака подчеркивания и может содержать алфавитно-цифровые символы и знак подчеркивания. И кроме того, название переменной не должно совпадать с названием ключевых слов языка Python
> 
> <img width="451" alt="image" src="https://github.com/user-attachments/assets/95910441-a08c-4840-b84a-b414a71ccf44" />
>
> Python поддерживает все распространенные арифметические операции:\
> **Сложение двух чисел:** ```print(6 + 2)  # 8```\
> **Вычитание двух чисел:** ```print(6 - 2)  # 4```\
> **Умножение двух чисел:** ```print(6 * 2)  # 12```\
> **Деление двух чисел:** ```print(6 / 2)  # 3.0```\
> **Целочисленное деление двух чисел:** ```print(7 / 2)  # 3.5 print(7 // 2)  # 3```\
Данная операция возвращает целочисленный результат деления, отбрасывая дробную часть\
> **Возведение в степень:** ```print(6 ** 2)  # Возводим число 6 в степень 2. Результат - 36```\
> **Получение остатка от деления:** ```print(7 % 2)  # Получение остатка от деления числа 7 на 2. Результат - 1```\
В данном случае ближайшее число к 7, которое делится на 2 без остатка, это 6. Поэтому остаток от деления равен 7 - 6 = 1
>
> Результат этих операций можно присваивать (записывать) в переменные
> ```
> num1 = 6
> num2 = 2
> sum = num1 + num2
> diff = num1 - num2
> mult = num1 * num2
> div = num1 / num2
> ```
> Так же можно делать так (со всеми операторами [+ - / *])
> ```
> num = 10
> num += 5
> print(num) # 15
> ```

---

1) Написать программу, которая выводит на экран значение и тип переменных 
```
name = "Xen"
age = 143
power = 100
weapon = "sword"
```
2) Написать программу, которая запросит у пользователя ввести значения переменных из задачи №1 и выведет их на экран в формате
```
Your character is Xen:
- age: 143
- power: 100
- weapon: sword
```
3) Дополнить программу из задания №2 так, чтобы задавалась переменная с именем xen_map и значением "magic map" и выводилась строка
```
Xen met wizard Merlin. Merlin gave him a magic map 
```

4) Дополнить программу из задания №3 так, чтобы кроме age, power и weapon задавалась переменная coins со значением 0. Добавить вывод переменной coins вместе с остальными. То есть вывод программы здесь должен быть похож на
```
Your character is Xen:
- age: 144
- power: 100
- weapon: sword
- coins: 0

Xen met wizard Merlin. Merlin gave him a magic map 
```
5) Дополнить программу из задания №4 так, чтобы выводилась строка
```
After a long journey, Xen found a hut. After searching it, he found 5 coins and a bottle with an unknown potion.
```
так как теперь у персонажа есть 5 монет, надо увеличить значение переменной coins на 5 и задать переменную stuff, в которую записать "bottle of potion", а так же вывести обновленную информацию о персонаже
```
Now Xen have 5 coins, magic map and bottle of potion
```
*ВАЖНО: при вызове print() для подставления количества монет, строки "magic map" и "bottle of potion" использовать f-строки и обращения к переменным*

6) Дополнить программу из задания №5 так, чтобы кроме age, power, weapon и coins задавалась переменная health со значением 150. Добавить вывод переменной health вместе с остальными. То есть вывод программы здесь должен быть похож на
```
Your character is Xen:
- age: 144
- power: 100
- health: 150
- weapon: sword
- coins: 0

Xen met wizard Merlin. Merlin gave him a magic map
After a long journey, Xen found a hut. After searching it, he found 5 coins and a bottle with an unknown potion.
Now Xen have 5 coins, magic map and bottle of potion
```
7) Дополнить программу из задания №6 так, чтобы выводилась строка 
```
Xen met a big angry griffon! Now is time to battle!
```
теперь реализуем драку с грифоном: чтобы победить персонажу надо нанести три удара, каждый отнимает 5 поинтов от силы (переменная power) и 10 от здоровья (health);
обновить значения переменных power и health и вывести строку
```
Xen won, but he was very tired and the griffin dealt him 30 points of damage and 15 points of power. Now he has 120 points of health and 85 points od power
```
*ВАЖНО: при вызове print() использовать f-сроки*

8) Дополнить программу из задания №7 так, чтобы выводилась строка 
```
Now Xen needs to decide what to do: test his bottle of potion or just have a rest
```
