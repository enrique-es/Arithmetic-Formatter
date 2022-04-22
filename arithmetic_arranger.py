from ast import operator
from tabulate import tabulate
import re

def arithmetic_arranger(list_number):
    if len(list_number) > 5:
        print("Error: Too many problems")
        exit()   
    list1 = []
    list2 = []
    list3 = []
    mystr = "-"
    for i in list_number:
        simbolo = re.findall('(\s[+-]\s)',i)
        try :
            operador = str(simbolo[0])
        except:
            print("Error: Operator must be '+' or '-'")
            exit()
        
        if operador[1] == "+":
            simbol = i.find("+")
            num1 = i[:simbol-1]            
            num2 = i[simbol:]
            num3 = i[simbol+2:]                
            #print("suma")
            try:
                numerador1 = int(num1)
                numerador2 = int(num3)
                adicion = numerador1+numerador2
                print(adicion)
            except:
                print("Error: Numbers must only contain digits.")
                exit()
        elif operador[1] == "-":
            simbol = i.find("-")
            num1 = i[:simbol-1]            
            num2 = i[simbol:]
            num3 = i[simbol+2:]
            #print("resta")
            try:
                numerador1 = int(num1)
                numerador2 = int(num3)
                resta = numerador1-numerador2
                print(resta)
            except:
                print("Error: Numbers must only contain digits.")
                exit()
            
        #simbol = i.find(simbolo)
        
        if len(num1) > len(num2):
            num2 = num2.replace(" "," "*(len(num1)-len(num2)+3),1)
            my_str = mystr.replace("-","-"*(len(num1)+2),1)
        my_str = mystr.replace("-","-"*(len(num2)),1)
        list1.append(num1)
        list2.append(num2)
        list3.append(my_str)
        
    listsum = [list1,list2,list3]

    print(list1)
    print(list2)
    print(list3)
    print (tabulate(listsum, stralign="right", tablefmt="plain"))

list_number = ["25 + 756","55 + 22", "123 + 1","55 + 232"]
arithmetic_arranger(list_number)

# def suma(num1, num3):
#     try:
#         numerador1 = int(num1)
#         numerador2 = int(num3)
#         adicion = numerador1+numerador2
#         return adicion
#     except:
#         print("Error: Numbers must only contain digits.")
#         exit()
