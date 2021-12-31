# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
operations = ["+", "-", "*", "/"]


def make_corresponding_operation(first_number, operation, second_number):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    else:
        print("Invalid operation")


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
        return
    else:
        return


memory = 0.0
while True:
    print(msg_0)
    calc = input()
    separated_calc = calc.split()
    x = separated_calc[0]
    oper = separated_calc[1]
    y = separated_calc[2]
    if x == "M" and y == "M":
        x = memory
        y = memory
    elif x == "M":
        x = memory
        try:
            y = float(y)
        except ValueError:
            print(msg_1)
            continue
    elif y == "M":
        y = memory
        try:
            x = float(x)
        except ValueError:
            print(msg_1)
            continue
    else:
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
            continue

    if oper not in operations:
        print(msg_2)
    else:
        check(x, y, oper)
        if oper == "/" and y == 0:
            print(msg_3)
        else:
            result = make_corresponding_operation(x, oper, y)
            print(result)
            while True:
                print(msg_4)
                answer = input()
                if answer == "y":
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            print(msg_[msg_index])
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:
                                    msg_index = msg_index + 1
                                    continue
                                else:
                                    memory = result
                                    break
                            elif answer == "n":
                                break
                            else:
                                continue
                        break
                    else:
                        memory = result
                        break
                elif answer == "n":
                    break
                else:
                    continue

            while True:
                print(msg_5)
                answer = input()
                if answer == "y":
                    break
                elif answer == "n":
                    exit(0)
                else:
                    continue
                break
    continue
