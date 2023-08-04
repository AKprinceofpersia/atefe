print("be barname rasm jadval khosh amadid")
Satr=int(input("addad satr khod ra vared konid: "))
soton=int(input("addad soton khod ra vared konid: "))
def jadval(x):
    y='#*'
    print(x*y)
def jadval2(z):
    p='*#'
    print(z*p)
for i in range(Satr):
    if (i % 2) == 0:
        jadval(soton)
    else:
        jadval2(soton)