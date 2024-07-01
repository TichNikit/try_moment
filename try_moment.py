def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        summ_ = personal_sum(numbers)
        summ = summ_[0]
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        mid = summ / (len(numbers)-summ_[1])
    except ZeroDivisionError:
        return 0

    return mid

x = (1, 2, 3, 4, 5)
print(calculate_average(x))
x = (1, 2, 3, 4, '5')
print(calculate_average(x))
x = 1
print(calculate_average(x))
x = [10, 10, '10', '10']
print(calculate_average(x))
x = ['10', '10']
print(calculate_average(x))