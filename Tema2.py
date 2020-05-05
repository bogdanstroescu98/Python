# 1980423410020
cnp = input("Introduceti un CNP:")
s = 0
for x in cnp:
    p=int(x) * int(x)
    s = s + p
valid = True
while valid:
    if 0 < int(cnp[0]) < 10:
        if 0<=int (cnp[1]) <= 9 and 0 <= int(cnp[0]) <= 9:
            if int(cnp[3]) == 1:
                if int(cnp[4]) < 2:
                    if 0 <= int(cnp[5]) <= 9 and 0 <= int(cnp[6]) <= 9:
                        if 0 <= int(cnp[7]) <= 9 and 0 <= int(cnp[8]) <= 9 and 0 <= int(cnp[9]) <= 9:
                            if p % 11 == 10 and int(cnp[12]) == 1:
                                input("CNP-ul est valid")
                                break
                            elif p % 11 != 10 and int(cnp[12]) == p % 11 :
                                input("CNP-ul este valid")
                                break
                            else:input("CNP-ul este invalid")
                            break


                        else:input("CNP-ul este invalid")
                        break

                else:
                    input("CNP-ul este invalid")
                    break
            elif int(cnp[3]) == 0:
                if 0 <= int(cnp[4]) <= 9:
                    if 0 <= int(cnp[5]) <= 9 and 0 <= int(cnp[6]) <= 9:
                        if 0 <= int(cnp[7]) <= 9 and 0 <= int(cnp[8]) <= 9 and 0 <= int(cnp[9]) <= 9:
                            if p % 11 == 10 and int(cnp[12]) == 1:
                                input("CNP-ul est valid")
                                break
                            elif p % 11 != 10 and int(cnp[12]) == p % 11 :
                                input("CNP-ul este valid")
                                break
                            else:input("CNP-ul este invalid")
                            break

                        else:input("CNP-ul este invalid")
                        break

                else:input("CNP-ul este invalid")
                break

            else:input("CNP-ul este invalid")
            break
    else:
        input("CNP-ul este invalid")
        break



