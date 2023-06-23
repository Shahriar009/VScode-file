

'''n=3.14159
R=float(input())
A=n*R**2
print(f"A={A:.4f}")

A=int(input())
B=int(input())
SOMA = A+B
print(f"SOMA = {SOMA}")

x=int(input())
y=int(input())
PROD=x*y
print(f"PROD = {PROD}")

A=float(input())*2
B=float(input())*3
C=float(input())*5
sum=A+B+C
MEDIA=sum/10
print(f"MEDIA = {MEDIA:.1f}")

A=float(input())*3.5
B=float(input())*7.5
sum=A+B
MEDIA=sum/11
print(f"MEDIA = {MEDIA:.5f}")
'''
'''
A=int(input())
B=int(input())
C=int(input())
D=int(input())
Portuguese=(A*B-C*D)
print(f"DIFFERENCE = {Portuguese}")

first_name=str(input())
salary=float(input())
total_sold=float(input())
bonous=total_sold*(15/100)
total_salary=salary+bonous
print(f"TOTAL = R$ {total_salary:.2f}")

line1=input().split(" ")
line2=input().split(" ")
code1,unit_product1,price_product1=line1
code2,unit_product2,price_product2=line2
total=(int(unit_product1)*float(price_product1))+(int(unit_product2)*float(price_product2))
print(f"VALOR A PAGAR: R$ {total:.2f}")


R=float(input())
pi=3.14159
volume=(4/3)*pi*R**3
print(f"VOLUME = {volume:.3f}")

A,B,C=list(map(float,input().split()))
triangle=0.5*A*C
circle=3.14159*C*C
trapezium=(A+B)/2.0*C
square=B*B
rectangle=A*B
print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
'''


'''
import math
a,b=input().split(" ")
MaiorAB=(a+b+abs(a-b))/2
print(f"{MaiorAB} eh o maior")
'''


'''
distancia = int(input())
combustivel = float(input())
consumo = distancia / combustivel
print(f'{consumo:.3f} km/l')




X=int(input())
Y=float(input())
consumption=X / Y
print(f'{consumption:.3f} km/l')

import math
x1,y1=list(map(float,input().split()))
x2,y2=list(map(float,input().split()))
distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print(f'{distance:0.4f}')
'''
'''



import math
x1,y1=list(map(float,input().split()))
x2,y2=list(map(float,input().split()))
distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print(f'{distance:0.4f}')


time=int(input())
av_speed=int(input())
litters=(av_speed*time)/12
print(f"{litters:.3f}")







notes = int(input())
print(notes)
print("{} nota(s) de R$ 100,00".format(int(notes/100)))
aux = (notes%100)
print("{} nota(s) de R$ 50,00".format(int(aux/50)))
aux = (aux%50)
print("{} nota(s) de R$ 20,00".format(int(aux/20)))
aux = (aux%20)
print("{} nota(s) de R$ 10,00".format(int(aux/10)))
aux = (aux%10)
print("{} nota(s) de R$ 5,00".format(int(aux/5)))
aux = (aux%5)
print("{} nota(s) de R$ 2,00".format(int(aux/2)))
aux = (aux%2)
print("{} nota(s) de R$ 1,00".format(int(aux/1)))






seconds = int(input())
minutes = int(seconds/60)
seconds -= minutes*60
hours = int(minutes/60)
minutes -= hours*60
print(f"{hours}:{minutes}:{seconds}")

'''

class list():
    def __init__(self):
        pass
    def upper(self):
        pass
    def lower(self):
        pass
a=list()
b=list()