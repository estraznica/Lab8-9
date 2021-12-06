print("Координаты фигур на шахматной доске в данном случае определяются двумя цифрами:\n"
      "первая цифра - значение по вертикали, вторая по горизонтали;\nотсчет идет слева направо и снизу вверх соответственно;"
      "\nшахматная доска формата 8х8 клеток")

print("Введите координаты двух фигур")
while True:  # Проверка ввода
    try:
        k=int(input("Введите координату 1 первой фигуры: "))
        if k>8 or k<1:  #проверка входит ли в диапазон
            print("Координата должна быть числом от 1 до 8")
        else:
            break
    except ValueError:
        print("Некорректный ввод")
        pass
while True:  # Проверка ввода
    try:
        l=int(input("Введите координату 2 первой фигуры: "))
        if l>8 or l<1:  #проверка входит ли в диапазон
            print("Координата должна быть числом от 1 до 8")
        else:
            break
    except ValueError:
        print("Некорректный ввод")
        pass
while True:  # Проверка ввода
    try:
        m=int(input("Введите координату 1 второй фигуры: "))
        if m>8 or m<1:  #проверка входит ли в диапазон
            print("Координата должна быть числом от 1 до 8")
        else:
            break
    except ValueError:
        print("Некорректный ввод")
        pass

while True:  # Проверка ввода
    try:
        n = int(input("Введите координату 2 второй фигуры: "))
        if n>8 or n<1:  #проверка входит ли в диапазон
            print("Координата должна быть числом от 1 до 8")
        else:
            break
    except ValueError:
        print("Некорректный ввод")
        pass

#проверка на цвет клеток
if k % 2 == 0 and l % 2 ==0 or k % 2 == 1 and l % 2 ==1:
    color1=0
if k % 2 == 1 and l % 2 ==0 or k % 2 == 0 and l % 2 ==1:
    color1=1
if m % 2 == 0 and n % 2 ==0 or m % 2 == 1 and n % 2 ==1:
    color2=0
if m % 2 == 1 and n % 2 ==0 or m % 2 == 0 and n % 2 ==1:
    color2=1

if color1==color2: #проверка совпадают ли цвета фигур
    print("Фигуры находятся на полях одного цвета")
if color1!=color2:
    print("Фигуры находятся на полях разного цвета")

def ladya(k,l,m,n): #функция проверки угрожает ли ладья
    global l_ugroza
    if k==m or l==n:
        l_ugroza=1
    else:
        l_ugroza=0

def l_output(l_ugroza): #функция вывода результатов для ладьи
    if l_ugroza==1:
        print("Фигура 1 (ладья) угрожает фигуре 2")
    else:
        print("Фигура 1 (ладья) не угрожает фигуре 2")

def slon(k, l, m,n): #функция проверки угрожает ли слон
    global s_ugroza
    if abs(k-m) == abs(l-n):
        s_ugroza = 1
    else:
        s_ugroza = 0

def s_output(s_ugroza): #функция вывода результатов для слона
    if s_ugroza == 1:
        print("Фигура 1 (слон) угрожает фигуре 2")
    else:
        print("Фигура 1 (слон) не угрожает фигуре 2")


def ferz(k,l,m,n): #функция проверки угрожает ли ферзь
    global f_ugroza

    if k==m or l==n:
        f1_ugroza=1
    else:
        f1_ugroza=0

    if abs(k - m) == abs(l - n):
        f2_ugroza = 1
    else:
        f2_ugroza = 0

    if f1_ugroza==1 or f2_ugroza==1:
        f_ugroza = 1
    else:
        f_ugroza = 0

def f_output(f_ugroza): #функция вывода результатов для ферзя
    if f_ugroza ==1:
        print("Фигура 1 (ферзь) угрожает фигуре 2")
    else:
        print("Фигура 1 (ферзь) не угрожает фигуре 2")

def kon(k,l,m,n): #функция проверки угрожает ли конь
    global k_ugroza
    if abs(k - m) * abs(l - n)==2:
        k_ugroza = 1
    else:
        k_ugroza = 0

def k_output(k_ugroza): #функция вывода результатов для коня
    if k_ugroza ==1:
        print("Фигура 1 (конь) угрожает фигуре 2")
    else:
        print("Фигура 1 (конь) не угрожает фигуре 2")

#Выбор фигуры
print("Выберите фигуру 1")
while True:  # Проверка ввода
    try:
        figura=int(input("Чтобы выбрать ладью нажмите 1, слона - 2, ферзя - 3, коня - 4: "))
        if figura>4 or figura<1:  #проверка входит ли в диапазон
            print("Такой фигуры нет")
        else:
            break
    except ValueError:
        print("Некорректный ввод")
        pass

if figura==1: #если ладья
    ladya(k, l, m, n)
    l_output(l_ugroza)
    if l_ugroza==1:
        print("С поля фигуры 1 (ладья) можно попасть на поле фигуры 2 за один ход")
    else:
        k_new=m
        l_new=n
        print("С поля фигуры 1 (ладья) нельзя попасть на поле фигуры 2 за один ход.\n"
              "Чтобы попасть на него можно сделать первый ход фигурой 1 на поле (", k_new, ":", l, ") или на поле (", k, ":",l_new,")" )
if figura==2: #если слон
    slon(k, l, m, n)
    s_output(s_ugroza)
    if s_ugroza==1:
        print("С поля фигуры 1 (слон) можно попасть на поле фигуры 2 за один ход")
    if color1==color2:
        if l<n:
            while True:
                k = k - 1
                l = l + 1
                if abs(k - m) == abs(l - n):
                    k_new = k
                    l_new = l
                    print("С поля фигуры 1 (слон) нельзя попасть на поле фигуры 2 за один ход.\n"
                          "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                          ")")
                    break
        if l>n:
            while True:
                k = k + 1
                l = l - 1
                if abs(k - m) == abs(l - n):
                    k_new = k
                    l_new = l
                    print("С поля фигуры 1 (слон) нельзя попасть на поле фигуры 2 за один ход.\n"
                          "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                          ")")
                    break
    else:
        print("Фигура 1 не сможет попасть на поле фигуры 2, т.к фигуры находятся на полях разного цвета")

if figura==3: #если ферзь
    ferz(k,l,m,n)
    f_output(f_ugroza)
    if f_ugroza==1:
        print("С поля фигуры 1 (ферзь) можно попасть на поле фигуры 2 за один ход")
    else:
        if color1 == color2:
            if l < n:
                while True:
                    k = k - 1
                    l = l + 1
                    if abs(k - m) == abs(l - n):
                        k_new = k
                        l_new = l
                        print("С поля фигуры 1 (ферзь) нельзя попасть на поле фигуры 2 за один ход.\n"
                              "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                              ")")
                        break
            if l > n:
                while True:
                    k = k + 1
                    l = l - 1
                    if abs(k - m) == abs(l - n):
                        k_new = k
                        l_new = l
                        print("С поля фигуры 1 (ферзь) нельзя попасть на поле фигуры 2 за один ход.\n"
                              "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                              ")")
                        break
        else:
            k_new = m
            l_new = n
            print("С поля фигуры 1 (ферзь) нельзя попасть на поле фигуры 2 за один ход.\n"
                  "Чтобы попасть на него можно сделать первый ход фигурой 1 на поле (", k_new, ":", l,
                  ") или на поле (", k, ":", l_new, ")")
if figura==4: #если конь
    kon(k, l, m, n)
    k_output(k_ugroza)
      
x=input("Нажмите любую клавишу чтобы завершить программу ")      
