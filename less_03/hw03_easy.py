# ------------------------------
# Lessons 03
# __autor__ - Турчин Богдан П.
#-------------------------------

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*       hw03_easy.py        *")
print("*         Задача 1          *")
print("*---------------------------*")

def my_round(number, ndigits):
    return round(number, ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(4.1023967, 5))
print(my_round(5.9999937, 5))
print(my_round(5.9999957, 5))
print("*---------------------------*")
print()

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*       hw03_easy.py        *")
print("*         Задача 2          *")
print("*---------------------------*")

def lucky_ticket(ticket_number):
    str_num = str(ticket_number)
    number = [int(n) for n in str_num]
    if sum(number[:3]) == sum(number[-3:]):
        return('Счастливый билет')
    else:
        return ('Несчастливый билет')

print('№ 123006 - ',lucky_ticket(123006))
print('№ 123210 - ',lucky_ticket(123210))
print('№ 436751 - ',lucky_ticket(436751))
print('№ 436751 - ',lucky_ticket(356751))
print('№ 436751 - ',lucky_ticket(936756))
