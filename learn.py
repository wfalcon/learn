a = 10
b = 5

if a > b:
    print("A больше B")
    print(a - b)
else:
    print("B больше или равно A")
    print(b - a)

print("Конец")

def open_file(filename):
    print("Чтение файла", filename)
    with open(filename) as f:
        return f.read()
        print("Готово")
