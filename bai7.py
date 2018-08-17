#cho pt ax^2 + bx + c = 0 tim nghiem pt 
a = input('a = ')
b = input('b = ')
c = input('c = ')
d = (float(b)*float(b) - 4*float(a)*float(c))
print('d :' + str(d))
from math import *
if d > 0 :
    x1 = (- float(b) + sqrt(d)) / 2*float(a)
    x2 = (- float(b) - sqrt(d)) / 2*float(a)
    print('co 2 nghiem' + str(x1) + str(x2))
elif d == 0 :
    x = - float(b) / 2*float(a)
    print('1 nghiem kep = ' + str(x))
else:
    print('vo nghiem')



