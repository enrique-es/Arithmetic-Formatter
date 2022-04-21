def arithmetic_arranger(list_number):
  for i in list_number:
    plus = i.find("+")
    minus = i.find("-")
    sig = ""
    if plus>0:
      first_s = i[:plus]
      first_s_len = len(first_s)
      first = int(first_s)
      second_s = i[plus+1:]
      second_s_len = len(second_s)
      second = int(second_s)
      sum = first+second
      if second_s_len >= first_s_len:
        print(second_s.rjust(second_s_len +2))
        print("+",first_s.rjust(second_s_len +3 - first_s_len))
        print(sig.rjust(second_s_len, "-"))
        print(sum) 
      else:
        print(first_s.rjust(first_s_len +2))
        print("+",second_s.rjust(first_s_len +3 - second_s_len))
        print(sig.rjust(first_s_len, "-"))
        print(sum)  
    print("") 
list_number = ["123456789 + 123","32 + 68", "567 + 756"]
arithmetic_arranger(list_number)