# #easy_version:

# print("hello user! im very happy you are using my project!\n\nthis is a calculator projct in which you can use the following operations:\n(+ add)\n(- subtract)\n(* multiply)\n(/ divide)\n(** power)\nbe careful to calculate liegal expressions\n\n and of course dont try to be funny and try to combine words\nenjoy ny friend!!!\n\n")
# print("chose an operation:\n1 = add\n2 = subtract\n3 = multiply\n4 = divide\n5 = power")
# continue1 = True
# while continue1==True:
#   operation = input()
#   if operation =="1":
#     num1 = input("add your first num\n")
#     num2 = input("add your second num\n")
#     print("the answer is:",float(num1)+float(num2))
#   elif operation =="2":
#     num1 = input("add your first num\n")
#     num2 = input("add your second num\n")
#     print("the answer is:",float(num1)-float(num2))
#   elif operation =="3":
#     num1 = input("add your first num\n")
#     num2 = input("add your second num\n")
#     print("the answer is:",float(num1)*float(num2))
#   elif operation =="4":
#     num1 = input("add your first num\n")
#     num2 = input("add your second num\n")
#     print("the answer is:",float(num1)/float(num2))
#   elif operation =="5":
#     num1 = input("add your first num\n")
#     num2 = input("add your second num\n")
#     print("the answer is:",float(num1)**float(num2))
#   else :
#     print("ERROR!!!\nWRONG INPUT")
#   con = input("calculate again?(yes/no)")
#   if con =="no":
#     continue1=False

# #turtle_version_3_numbers:

# import turtle
# turtle.bgcolor("red")
# wb= turtle.Screen()
# wb.setup(700, 450)
# turtle.setposition(0,-150)
# turtle.write("hello user! im very happy you are using my project!\n\nthis is a calculator projct in which you can use the following operations:\n(+ add)\n(- subtract)\n(* multiply)\n(/ divide)\n(** power)\nmake sure you use space between every full number be\n careful to calculate liegal expressions\n\n and of course dont try to be funny and try to combine words\nenjoy ny friend!!!\n\n",font=("calibri", 10, "bold"), align = "center")
# try:
#   continue1 = True
#   history = {}
#   while continue1==True:
#     txt = input()
#     x = txt.split()
#     if x[1]=="+" and x[3]=="-":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[0])+int(x[2])-int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])+int(x[2]-int(x[4]))
#     elif x[1]=="+" and x[3]=="+":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[0])+int(x[2])+int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])+int(x[2]+int(x[4]))
#     elif x[1]=="+" and x[3]=="**":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[2])**int(x[4]+int(x[0])),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])+int(x[2]**int(x[4]))
#     elif x[1]=="+" and x[3]=="*":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[2])*int(x[4])+int(x[0]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])+int(x[2]*int(x[4]))
#     elif x[1]=="+" and x[3]=="/":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[2])/int(x[4])+int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])+int(x[2]/int(x[4]))
#     elif x[1]=="-" and x[3]=="-":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])-int(x[2])-int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])-int(x[2]-int(x[4]))
#     elif x[1]=="-" and x[3]=="+":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])-int(x[2])+int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])-int(x[2])+int(x[4])
#     elif x[1]=="-" and x[3]=="*":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[2])*int(x[4])-int(x[0]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])-int(x[2])*int(x[4])
#     elif x[1]=="-" and x[3]=="/":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])-int(x[2])/int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])-int(x[2])/int(x[4])
#     elif x[1]=="-" and x[3]=="**":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[0])-int(x[2])**int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])-int(x[2]**int(x[4]))
#     elif x[1]=="*" and x[3]=="+":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])*int(x[2])+int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])*int(x[2])+int(x[4])
#     elif x[1]=="*" and x[3]=="-":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])*int(x[2])-int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])*int(x[2])-int(x[4])
#     elif x[1]=="*" and x[3]=="*":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])*int(x[2])*int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])*int(x[2])*int(x[4])
#     elif x[1]=="*" and x[3]=="/":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])*int(x[2])/int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])*int(x[2])/int(x[4])
#     elif x[1]=="*" and x[3]=="**":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[0])*int(x[2])**int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])*int(x[2]**int(x[4]))
#     elif x[1]=="/" and x[3]=="+":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])/int(x[2])+int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])/int(x[2])+int(x[4])
#     elif x[1]=="/" and x[3]=="-":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])/int(x[2])-int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])/int(x[2])-int(x[4])
#     elif x[1]=="/" and x[3]=="*":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])/int(x[2])*int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])/int(x[2])*int(x[4])
#     elif x[1]=="/" and x[3]=="/":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])/int(x[2])/int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])/int(x[2])/int(x[4])
#     elif x[1]=="/" and x[3]=="**":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[0])/int(x[2])**int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])/int(x[2]**int(x[4]))
#     elif x[1]=="**" and x[3]=="+":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])**int(x[2])+int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])**int(x[2])+int(x[4])
#     elif x[1]=="**" and x[3]=="-":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])**int(x[2])-int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])**int(x[2])-int(x[4])
#     elif x[1]=="**" and x[3]=="*":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])**int(x[2])*int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])**int(x[2])*int(x[4])
#     elif x[1]=="**" and x[3]=="/":
#       turtle.clear()
#       turtle.setposition(0,-150)
#       turtle.write(int(x[0])**int(x[2])/int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])**int(x[2])/int(x[4])
#     elif x[1]=="**" and x[3]=="**":
#       turtle.clear()
#       turtle.setposition(0,0)
#       turtle.write(int(x[0])**int(x[2])**int(x[4]),font=("calibri", 20, "bold"), align = "center")
#       history[txt] = int(x[0])+int(x[2]+int(x[4]))
#     elif x[1 or 3 or 5 or 7 or 9]!='+' or '-' or '*' or '/' or '**':
#       turtle.write("ERROR!!!")
#       turtle.clear()
#     else:
#       turtle.clear()
#       turtle.write("ERROR!!!")
#     print("history:")
#     for key ,value in history.items():
#       print(key,"=",value)
#     con = input("calculate again?(yes/no)")
#     if con =="no":
#       continue1=False
#       turtle.bgcolor("green")
#       turtle.write("thank you for using said's calculator",font=("calibri", 20, "bold"), align = "center")
# except:
#   print("ERROR!")

#final_version:

#Menu
import turtle

turtle.bgcolor("red")
wb = turtle.Screen()
wb.setup(700, 450)
turtle.setposition(0, -150)
turtle.write(
    "hello user! im very happy you are using my project!\n\nthis is a calculator projct in which you can use the following operations:\n(+ add)\n(- subtract)\n(* multiply)\n(/ divide)\n(** power)\nmake sure you use space between every full number be\n careful to calculate liegal expressions\n\n and of course dont try to be funny and try to combine words\nenjoy ny friend!!!\n\n",
    font=("calibri", 10, "bold"),
    align="center")

#Basic Values
equation = 0
history = []
result = 0
running = True


#Functions
def check_symbol(element):
    if element == "+" or element == "-" or element == "" or element == "/" or element == "^" or element == "*" or element == "history":
        return True
    else:
        return False


#Base
while running == True:
    equation = (input("What should I calculate? "))
    equation = equation.split()
    if equation[0] == "stop":
        print("Stopped Mr.Calc...")
        break
    #history
    elif equation[0] == "history" or equation[0] == "History":
        print(history)
    for element in equation:
        #Strings
        if element.isdigit() == False and check_symbol(element) == False:
            print(
                "I don't know how to calculate this: " + element +
                " didn't you read the rules?? use only numbers and functions!")
            break
        #Additios
        elif element == "+":
            try:
                if equation[3] == "+":
                    result = float(equation[0]) + float(equation[2]) + float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "-":
                    result = float(equation[0]) + float(equation[2]) - float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "*":
                    result = float(
                        equation[0]) + float(equation[2]) * float(equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "/":
                    if equation[4] == "0":
                        print(
                            "Sorry, dividing by 0 is illegal, stop or I will call the police!"
                        )
                        break
                    else:
                        result = float(equation[0]) + float(
                            equation[2]) / float(equation[4])
                        history.append(result)
                        print(result)
                        break
                elif equation[3] == "**" or equation[3] == "^":
                    result = float(equation[0]) + float(equation[2])**float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
            except:
                result = float(equation[0]) + float(equation[2])
                history.append(result)
                print(result)
        #Subtraction
        elif element == "-":
            try:
                if equation[3] == "+":
                    result = float(equation[0]) - float(equation[2]) + float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "-":
                    result = float(equation[0]) - float(equation[2]) - float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "*":
                    result = float(
                        equation[0]) - float(equation[2]) * float(equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "/":
                    if equation[4] == "0":
                        print(
                            "Sorry, dividing by 0 is illegal, stop or I will call the police!"
                        )
                        break
                    else:
                        result = float(equation[0]) - float(
                            equation[2]) / float(equation[4])
                        history.append(result)
                        print(result)
                        break
                elif equation[3] == "**" or equation[3] == "^":
                    result = float(equation[0]) - float(equation[2])**float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
            except:
                result = float(equation[0]) - float(equation[2])
                history.append(result)
                print(result)
        #Multiplication
        elif element == "*":
            try:
                if equation[3] == "+":
                    result = float(equation[0]) * float(equation[2]) + float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "-":
                    result = float(equation[0]) * float(equation[2]) - float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "*":
                    result = float(equation[0]) * float(equation[2]) * float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "/":
                    if equation[4] == "0":
                        print(
                            "Sorry, dividing by 0 is illegal, stop or I will call the police!"
                        )
                        break
                    else:
                        result = float(equation[0]) * float(
                            equation[2]) / float(equation[4])
                        history.append(result)
                        print(result)
                        break
                elif equation[3] == "**" or equation[3] == "^":
                    result = float(equation[0]) * float(equation[2])**float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
            except:
                result = float(equation[0]) * float(equation[2])
                history.append(result)
                print(result)
        #Division
        elif element == "/":
            if equation[2] == "0":
                print(
                    "Sorry, dividing by 0 is illegal, stop or I will call the police!"
                )
            else:
                try:
                    if equation[3] == "+":
                        result = float(equation[0]) / float(
                            equation[2]) + float(equation[4])
                        history.append(result)
                        print(result)
                        break
                    elif equation[3] == "-":
                        result = float(equation[0]) / float(
                            equation[2]) - float(equation[4])
                        history.append(result)
                        print(result)
                        break
                    elif equation[3] == "*":
                        result = float(equation[0]) / float(
                            equation[2]) * float(equation[4])
                        history.append(result)
                        print(result)
                        break
                    elif equation[3] == "/":
                        if equation[4] == "0":
                            print(
                                "Sorry, dividing by 0 is illegal, stop or I will call the police!"
                            )
                            break
                        else:
                            result = float(equation[0]) / float(
                                equation[2]) / float(equation[4])
                            history.append(result)
                            print(result)
                            break
                    elif equation[3] == "**" or equation[3] == "^":
                        result = float(equation[0]) / float(
                            equation[2])**float(equation[4])
                        history.append(result)
                        print(result)
                        break
                except:
                    result = float(equation[0]) / float(equation[2])
                    history.append(result)
                    print(result)
        #Exponents
        elif element == "^" or element == "**":
            try:
                if equation[3] == "+":
                    result = float(equation[0])**float(equation[2]) + float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "-":
                    result = float(equation[0])**float(equation[2]) - float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "*":
                    result = float(equation[0])**float(equation[2]) * float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
                elif equation[3] == "/":
                    if equation[4] == "0":
                        print(
                            "Sorry, dividing by 0 is illegal, stop or I will call the police!"
                        )
                        break
                    else:
                        result = float(equation[0])**float(
                            equation[2]) / float(equation[4])
                        history.append(result)
                        print(result)
                        break
                elif equation[3] == "**" or equation[3] == "^":
                    result = float(equation[0]) * float(equation[2]) * float(
                        equation[4])
                    history.append(result)
                    print(result)
                    break
            except:
                result = float(equation[0])**float(equation[2])
                history.append(result)
                print(result)
