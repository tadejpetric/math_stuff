import math


def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))):
        if not num % i:
            return False
    return True


def field_in():
    field = int(input("input the size of field Z: "))
    if not is_prime(field):
        print("this is not a field")
    return field


def polynomial_in():
    polynomial = input("Enter polynomial F[x,y]: ")
    polynomial = polynomial.replace(' ', "")
    polynomial = polynomial.replace('-', "+-")
    polynomial = polynomial.split('+')
    result = []
    for term in polynomial:
        if len(term) == 0:
            continue
        temp = {'num': 0, 'x': 0, 'y': 0}
        prev = 0  # 0 for num, 1 x, 2 y
        number = ""
        x = "0"
        y = "0"
        for character in term:
            if character == '^':
                if prev == 1:
                    x = ""
                else:
                    y = ""
                continue
            if character == '-':
                continue
            if prev == 0:
                if character != 'x' and character != 'y':
                    number += character
                else:
                    if character == 'x':
                        prev = 1
                        x = "1"
                    elif character == 'y':
                        prev = 2
                        y = "1"
            elif prev == 1:
                if character != 'y':
                    x += character
                else:
                    prev = 2
                    y = "1"
            elif prev == 2:
                if character != 'x':
                    y += character
                else:
                    prev = 1
                    x = "1"
        try:
            temp['num'] = int(number)
            if term[0] == '-':
                temp['num'] *= -1
        except ValueError:
            temp['num'] = 1 if term[0] != '-' else -1
        temp['x'] = int(x)
        temp['y'] = int(y)
        result.append(temp)
    return result


def calculate(poly, x, y, field):
    result = 0
    for term in poly:
        result += term['num'] * x**term['x'] * y**term['y']
    return result % field


def display(polynomial, field):
    for row in range(field - 1, -1, -1):
        print("{0:2}".format(row)+'|', end="")
        for column in range(field):
            value = calculate(polynomial, column, row, field)
            if value == 0:
                print(u"\u2588\u2588", end="")
            else:
                print('  ', end="")
        print()
    print('-' * (2*(field+3)))
    print('  |', end="")
    for i in range(field):
        print(str(i)[0]+(" "), end="")
    print('\n   ', end="")
    for i in range(field):
        if i > 9:
            print(i % 10, end=" ")
        else:
            print('  ', end="")
    print()


def ui_loop():
    field = field_in()
    polynomial = polynomial_in()
    while True:
        display(polynomial, field)
        option = input("Q quit, F new field, P new polynomial, A new everything: ")
        if option.upper() == 'Q':
            break
        if option.upper() == 'F':
            field = field_in()
        if option.upper() == 'P':
            polynomial = polynomial_in()
        if option.upper() == 'A':
            field = field_in()
            polynomial = polynomial_in()


if __name__ == '__main__':
    ui_loop()
