#tinh tong 1 + 2 + 3 + ... + n = ?
a = int(input(' nhap a = '))
tong = 0
i = 1 
while i <= a :
    tong = tong + i
    i = i + 1 
    print('tong = ' + str(tong))