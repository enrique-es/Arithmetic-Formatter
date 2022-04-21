# list1 = [1121,4324,564]
# list2 = [9789,976,534]
# listsum = [list1,list2]
# print(listsum)


from tabulate import tabulate
import re

list_number = ["2 + 756","55 + 22", "123456 + 1"]
list1 = []
list2 = []
list3 = []
mystr = "-"
for i in list_number:
    simbol = i.find("+")
    #simbolo = re.findall('\s([+-])\s',i)
    #simbol = i.find(simbolo)
    num1 = i[:simbol-1]
    num2 = i[simbol:]
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
print (tabulate(listsum, colalign=("right","right","right"), tablefmt="plain"))


