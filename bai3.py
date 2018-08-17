#nhap nam sinh vao in ra so tuoi va cho biet da du tuoi thi bang lai chua 
namsinh = input('ban sinh nam bn ')
tuoi = 2018 - int(namsinh)
print('tuoi :' + str(tuoi) )
if tuoi >= 18:
    print('da du tuoi thi bang lai')
else : 
    print('chua du tuoi thi bang lai')

if int(namsinh) % 4 == 0:
    print('nam nhuan')