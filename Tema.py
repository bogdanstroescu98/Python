# #Exercitiul 1
# text = input("Introduceti textul :")
# if len(text) > 0:
#     if text[0] == "-":
#         text = text[1:]
#         ceva = None
#     if text.isdigit():
#         print("Sirul de numere a fost gasit de Bogdan")
#     elif "." in text and len(ceva := text.split(".")) == 2 and ceva[0].isdigit() and ceva[1].isdigit():
#         print("Sirul de numere a fost gasit de Bogdan")
#     else:
#         print("Sirul de caractere a fost gasit de Bogdan")

# #Exercitiul 2
# nr = input("Introduceti un numar:")
# if len(nr) > 0:
#     if nr[0] == "-":
#         nr = nr[1:]
#     if nr.isdigit():
#         nr = int(nr)
#         if nr % 2 == 0:
#             print("Numarul introdus este par.")
#         else: print("Numarul introdus este impar.")
#     else: print("Nu ati introdus un numar.")

# #Exercitiul 3
# an =input("Introduceti un an:")
# if len(an) > 0:
#     if an[0] == "-":
#         print("Ati introdus o valoare eronata.")
#     elif an.isdigit():
#         an = int(an)
#         if an % 4 == 0:
#             print("Acest an este bisect.")
#         else: print("Acesta nu este un an bisect.")
#     else: print("Nu ati introdus un an.")

# #Exercitiul 4
# n = input("Introduceti un numar:")
# if len(n) > 0:
#     if n[0] == "-":
#         n = float(n[1:])
#         print("Numarul este ",n)
#     elif n == "0":
#         print("Numarul este 0")
#     else:
#         if float(n) < 10:
#             print("Numarul este pozitiv si mai mic decat 10")
#         else:print("Niciuna dintre conditii nu este indeplinita")

# #Exercitiul 5
# print("1 - Afisare lista de cumparaturi \n2 - Adaugare element\n3 - Stergere element\n4 - Stergere lista de cumparaturi\n5 - Cautare lista de cumparaturi")
# comanda = int(input())
# if comanda == 1:
#      print("Afisare lista de cumparaturi")
# elif comanda == 2:
#      print("Adaugare element")
# elif comanda == 3:
#     print("Stergere element")
# elif comanda == 4:
#     print("Stergere lista de cumparaturi")
# elif comanda == 5:
#     print("Cautare lista de cumparaturi")
# elif comanda == 0:
#     print("Iesire din aplicatie.Multumim ca ati utilizat serciciile noastre!")






