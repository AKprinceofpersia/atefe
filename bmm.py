import math
print("be barname mohasebe bmm khos omadid")
num1=int(input("addad aval ra vared konid: "))
num2=int(input("addad dovom ra vared konid: "))
bmm=math.gcd(num1,num2)
gcd = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("Bmm ", num1, "va", num2, gcd,"hast")
print (bmm)