import math
print("be barname mohasebe kmm khos omadid")
num1=int(input("addad aval ra vared konid: "))
num2=int(input("addad dovom ra vared konid: "))
kmm=math.lcm(num1,num2)
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        x = i
        break
print(" kmm ", num1, "va", num2, x,"hast")
print (kmm)