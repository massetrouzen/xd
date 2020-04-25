flag = True
while flag:
    number1 = float(input("Первое число:"))
    number2 = float(input("Второе число:"))

    command = input("Выберите операцию(+,-,/,*):")

    if command == '+' :
        result = number1 + number2
    elif command == '-' :
        result = number1 - number2
    elif command == '*' :
        result = number1 * number2
    elif command == '/' :
            result = number1 / number2
    else:
        print("Выбрана неправильная операция, попробуйте снова")
        continue
    print (result)

    input_errors = 0
    res = ''
    while flag:
        res = input("Хотите начать сначала? (да/нет)")
        if res.lower() == 'да':
            flag = True
            break
        if input_errors >= 2:
            res = 'нет'
            flag = False
            break
        if not (res.lower() == 'да' or res.lower() == 'нет'):
            input_errors += 1
            print("Некорректное значение")
            continue
        break

    if res.lower() == 'да':
        continue
    if res.lower() == 'нет':
        break