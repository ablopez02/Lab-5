#Abbie and Anastacia
#Note: this file has A-C and PyL51 at the bottom!
#A
x=2
if x < 3:
    print("Small")

x=5
if x < 3:
    print("Small")

score = 8
if score > 6:
    print("Nice work!")

for i in range(1,16):
    if i % 3 == 0:
        print(i, "is divisible by 3.")

#B
x=2
if x < 3:
    print("small")
else:
    print("large")

x = 5
if x < 3 :
    print("small")
else:
    print("large")

score = 8
if score < 6:
    print("needs improvement")
elif score < 9 :
    print("nice work!")
else:
    print("excellent!")
#else statements produce another answer if the if statement is not true, similar with the elif
#not every if statement needs an else statement if the if statement is true
for i in range(-2,3):
    if i < 0:
        print(i, "is negative.")
    elif i == 0:
        print(i, " is zero.")
    else:
        print(i, "is positive.")

x=12
if x%2 == 0:
    print("even")
else:
    print("odd")

#C
print(3 < 4 )
print(4 > 2)
type(True)

if True:
    print("this text will always appear.")
if False:
    print("this text will not appear.")
#the value result of the expression 3<4 is True
#True is a boolean
type(False)
print(3==5)

#L51
import turtle
abbie = turtle.Turtle()
abbie.width(5)
abbie.speed(0)
def draw_star(color):
    for side in range(5):
        abbie.forward(100)
        abbie.right(144)
        abbie.color(color)
draw_star("hot pink")#im extra happy today hahaha so i made it hot pink






        
        

    
