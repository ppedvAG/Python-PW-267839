# # While Schleife
# # kopfgesteuert
# # break beendet die Schleife
# # continue überspringt den Rest des Schleifenkörpers
# # i = 0
# # while i<100000:
# #     if i == 97: # Schleife wird frühzeitig beendet
# #         break
# #     i += 1
# #     if i % 10 == 0:
# #         continue # wenn i durch 10 teilbar ist, wird i nicht ausgegeben
# #     print(i)
# from _pyrepl import readline
#
# from Grundlagen2 import teilnehmerEmails
#
# # while True:
# #     print("hallo")
#
#
# # i = 0
# # while i<3:
# #     print("gib eine zahl ein")
# #     zahl1 = int(input())
# #     print("gib eine zweite zahl ein")
# #     zahl2 = int(input())
# #     print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
# #     print("Wiederholen? (J/N)")
# #     eingabe = input()
# #     i+=1
# #     if eingabe == "N" or eingabe == "n":
# #        break
#
# # for Schleife für Listen, Strings, Sets, Tupels und Dictionarys
# teilnehmerEmails = {
#     "Laura": "laura@email.com",
#     "Sarah": "sarah@email.com",
#     "Dominik": "dominikemail.com"
# }
# for teilnehmer in teilnehmerEmails:
#     print(teilnehmer+": "+teilnehmerEmails[teilnehmer])
#     if not ("@" in teilnehmerEmails[teilnehmer]):
#         print(f"Emailadresse von {teilnehmer} ist nicht korrekt: {teilnehmerEmails[teilnehmer]}")
#
# print (teilnehmerEmails)
#
# # listen erzeugen (List Comprehension)
#
# l = list(range(1,11))
#
# # anstatt while-scheife zum zählen von 1-100
# i = 1
# while i < 101:
#     print(i)
#     i += 1
# # for mit range ist kürzer
# for i in range(1,101):
#     print(i)
#
# for i in range(11, 21):
#     l.append(i)
#

buzzList = [i for i in range(1, 101) if not i%3 ==0 and not i%5 ==0]
print(buzzList)

buzzList = []
for i in range(1,101):
    if not i%3 ==0 and not i%5 ==0: buzzList.append(i)
print(buzzList)
