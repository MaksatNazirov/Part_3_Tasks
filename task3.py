# "Аналог шифра цезаря ". Программа должна запрашивать элементы списка через
# пробел. После чего пользователь должен ввести значение для сдвига элементов списка.
# Значение может быть как положительным, так и отрицательным. Если значение
# положительное, элементы списка должны сдвигаться вправо, если отрицательное -
# влево. Результат необходимо вывести на экран:


numbers =  input("your numbers: ")
steps = int(input("write step: "))
split_numbers = numbers.split()

if steps > 0:
    steps = abs(steps)
    for num in range(steps):
        split_numbers.append(split_numbers.pop(0))

    print(" ".join(split_numbers))
else:
    for num in range(steps):
        split_numbers.insert(0, split_numbers.pop())

    print(" ".join(split_numbers))
print(type(split_numbers))
