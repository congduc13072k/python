# tinh tong 1+2+3...+n
n = int(input("nhap n = "))
tong = 0
if n%2 == 0:
    tong = 0 + n/2 * (n + 1)
else:
    tong = 0 + (n//2 + 1) + n//2 * (n + 1)
print("tong day so tu 1 den n  = ",tong)