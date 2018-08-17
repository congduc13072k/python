#nhap 3 canh cua tam giac hay cho biet tam giac gi
a = input('canh 1 = ')
b = input('canh 2 = ')
c = input('canh 3 = ')
import math 
if int(a) - (int(b) + int(c)) > 0 or int(b) - (int(a) + int(c)) > 0 or int(c) - (int(a) + int(b)) > 0 :
    print('ko la tam giac')
elif a == b and b == c and a == c :
    print('la tam giac deu')
    chuvi = int(a) + int(b) + int(c)
    print('chu vi tam giac =' + str(chuvi))
    p = chuvi/2
    dt = math.sqrt(p*(p - int(a))*(p - int(b))*(p - int(c)))
    print('dien tich la =' + str(dt))
elif a == b or b == c or c == a :
    print('la tam giac can')
    chuvi = int(a) + int(b) + int(c)
    print('chu vi tam giac =' + str(chuvi))
    p = chuvi/2
    dt = math.sqrt(p*(p - int(a))*(p - int(b))*(p - int(c)))
    print('dien tich la =' + str(dt))
elif int(a)*int(a) + int(b)*int(b) == int(c)*int(c) or int(b)*int(b) + int(c)*int(c) == int(a)*int(a) or int(c)*int(c) + int(a)*int(a) == int(b)*int(b) :
    print('la tam giac vuong')
    chuvi = int(a) + int(b) + int(c)
    print('chu vi tam giac =' + str(chuvi))
    p = chuvi/2
    dt = math.sqrt(p*(p - int(a))*(p - int(b))*(p - int(c)))
    print('dien tich la =' + str(dt))
else :
    print('la tam giac thuong')
    chuvi = int(a) + int(b) + int(c)
    print('chu vi tam giac =' + str(chuvi))
    p = chuvi/2
    dt = math.sqrt(p*(p - int(a))*(p - int(b))*(p - int(c)))
    print('dien tich la =' + str(dt))
