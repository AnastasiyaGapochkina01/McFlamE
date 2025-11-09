def calculate_tip(bill_amount, service_level):
    if service_level == 1:
        percent = 0.10
    elif service_level == 2:
        percent = 0.15
    elif service_level == 3:
        percent = 0.20
    else:
        print("Incorrect service level")
    tip = bill_amount * percent
    return tip


def check_calc_tip_function():
    bill = 1000
    level = 2
    tip = calculate_tip(bill, level)
    print(f"Сумма чаевых: {tip}")

    bills = {
        "bill-1": (1000, 2),
        "bill-2": (1500, 1),
        "bill-3": (2000, 3),
        "bill-4": (750, 1),
        "bill-5": (500, 1)
    }

    summ_tip = 0
    for bill_info in bills.values():
        amount, level = bill_info
        summ_tip += calculate_tip(amount, level)

    print(f"Общая сумма чаевых: {int(summ_tip)}")


def gen_greeting(name, event):
    greetings = {
        "др": f"С днем рождения, {name}! Желаю всего самого прекрасного!",
        "8 марта": f"С 8 марта, {name}! Пусть все будет хо-ро-шо",
        "нг": f"С новым годом, {name}! Новых свершений!"
    }
    res = greetings.get(event, f"Поздравляю с праздником, {name}")
    return res

def run_greeting():
    #name = "Саша"
    #event = "др"
    name = input("Введи имя: ")
    event = input("Введи праздник: ")
    print(f"{gen_greeting(name, event)}")

import random

def game(user_choice):
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)
    if user_choice not in choices:
        return f"Ошибка! Выбери из {choices}"
    
    if user_choice == computer_choice:
        return "Ничья"
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or 
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень")
    ):
        return "Ты выиграл!!!"
    else:
        return "Ты проиграл((("

