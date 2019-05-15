""" ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi """


def post_code_generator(p_code1, p_code2):
    p_code1 = int(p_code1.replace('-', ''))
    p_code2 = int(p_code2.replace('-', ''))

    return ["%02d-%03d" % divmod(x, 1000) for x in range(p_code1 + 1, p_code2)]


print(post_code_generator("79-900", "80-155"))
