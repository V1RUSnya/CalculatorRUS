from colorama import Fore, Back, Style
from colorama import init as it
import math
it()
print("Здравствуй! Это первый калькулятор on PYTON")
print("Ver 1.5 beta! Поддержка Сложения(+), Вычитания(-), Умножения(*), Деления(/)")
print("А так же - Возведение в степень(**), Косинус первого числа(cs), Синус первого числа(sn) и Тангенс первого числа(tg)")
First = float(input("Введите число "))
what = input("Введите действие ")
if what == "**":
    Second = float(input("Введите второе число "))
    print( Back.RED )
    answer = str(First ** Second)
    print("Ваш ответ - " + answer)
else:
    if what == "cs":
        print( Back.RED )
        answer = str(math.cos(math.radians(First)))
        print("Ваш ответ - " + answer)
    else:
        if what == "sn":
            print( Back.RED )
            answer = str(math.sin(math.radians(First)))
            print("Ваш ответ - " + answer)
        else:
            if what == "tg":
                print( Back.RED )
                answer = str(math.tan(math.radians(First)))
                print("Ваш ответ - " + answer)
            else:
                Second = float(input("Введите второе число "))
                print( Back.RED )
                if what == "+":
                    answer = str(First + Second)
                    print("Ваш ответ - " + answer)
                else:
                    if what == "-":
                        answer = str(First - Second)
                        print("Ваш ответ - " + answer)
                    else:
                        if what == "*":
                            answer = str(First * Second)
                            print("Ваш ответ - " + answer)
                        else:
                            if what == "/":
                                answer = str(First / Second)
                                print("Ваш ответ - " + answer)
                            else:
                                print("Ошибка")
                    
