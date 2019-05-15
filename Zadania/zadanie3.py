""" ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5,
DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL. """


from decimal import Decimal


def number_generator():
    return [Decimal(x / 2) for x in range(4, 12)]


print(number_generator())
