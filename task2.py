# Попросить пользователя ввести слова через пробел. Отсортировать слова по количеству
# символов и вывести на экран результат.

text =  str(input("Введите текст: "))
# print(text)
l = text.split()
q=""
for i in sorted(l,key=lambda a: len(a)):
    q = q + " " + i
print(q)