import re
s = 0
cnp = input("Introduceti un CNP:\n")
numar = "279146358279"
valid = re.search("^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-3]\d|4[0-6]|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",cnp)
for i in range(len(cnp)-1):
   s =s + int(cnp[i])*int(numar[i])
rest= s % 11
if (valid):
  if (rest == 10 and int(cnp[-1])== 1) or (rest < 10 and rest == int(cnp[-1])):
    print("CNP-ul este valid!")
  else:
     print("CNP-ul este invalid!")
else:
  print("CNP-ul este invalid!")