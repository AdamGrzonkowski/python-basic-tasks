""" ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10] """


def get_missing_values(values, n):
    return list(set(range(1, n + 1)) - set(values))


print(get_missing_values([2, 3, 7, 4, 9], 10))
