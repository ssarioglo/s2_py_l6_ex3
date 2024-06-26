print("Введите А и В (А <= В) через Enter")
a = int(input())
b = int(input())
if a > b:
    print("Не выполнено условие А <= В")
    quit()

result = ""
print("Все четные числа на данном отрезке А В:")
for i in range(a, b + 1):
    if (i % 2) == 0:
        result += (str(i)+ ' ')

print(result)