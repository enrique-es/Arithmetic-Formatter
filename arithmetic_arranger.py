from tabulate import tabulate
import re
import sys


def arithmetic_arranger(problems,printResult = None):
    #Inicialize empty strings   
    list1 = [] #For first argument of each string
    list2 = [] #For second argument of each string
    list3 = [] #For spaces between columns
    list4 = [] #For the results of operations
    mystr = "-"

    #From given list of string, check if there are less 5 items as maximum, if not, program will finish
    if len(problems) > 5:
        return("Error: Too many problems.")    

    #Start to analize the strings of given list
    for i in problems:
        simbolo = re.findall('(\s[+-/*]\s)',i)
        operador = str(simbolo[0])
        if operador[1] == '/' or operador[1] == '*':
            return("Error: Operator must be '+' or '-'.")
        #check if string should be an addition, then separate sting in arguments to operate
        elif operador[1] == "+":
            simbol = i.find("+")
            num1 = i[:simbol-1]            
            num2AndOp = i[simbol:]
            num2 = i[simbol+2:]                         
            try:
                numerador1 = int(num1)
                numerador2 = int(num2)                
            except:
                return("Error: Numbers must only contain digits.")
            if len(num1) > 4 or len(num2) > 4:
                return("Error: Numbers cannot be more than four digits.")
            else: 
                adicion = numerador1+numerador2
                list4.append(adicion)
                list4.append("")
        #check if string should be an subtraction, then separate sting in arguments to operate
        elif operador[1] == "-":
            simbol = i.find("-")
            num1 = i[:simbol-1]            
            num2AndOp = i[simbol:]
            num2 = i[simbol+2:]
            try:
                numerador1 = int(num1)
                numerador2 = int(num2)
            except:
                return("Error: Numbers must only contain digits.")
            if len(num1) > 4 or len(num2) > 4:
                return("Error: Numbers cannot be more than four digits.")
            else:
                resta = numerador1-numerador2
                list4.append(resta)
                list4.append("")
        #Format of output   
        if len(num1) > len(num2):
            num2AndOp = num2AndOp.replace(" "," "*(len(num1)-len(num2AndOp)+3),1)
            my_str = mystr.replace("-","-"*(len(num1)+2),1)
        my_str = mystr.replace("-","-"*(len(num2AndOp)),1)
        list1.append(num1)
        list1.append("")
        list2.append(num2AndOp)
        list2.append("")    
        list3.append(my_str)
        list3.append("")
        
    listsum = [list1,list2,list3]
    listsum2 = [list1,list2,list3,list4]
    if printResult:
        tablita = tabulate(listsum2, stralign="right", tablefmt="plain")
    else :
        tablita = tabulate(listsum, stralign="right", tablefmt="plain")
    return tablita

