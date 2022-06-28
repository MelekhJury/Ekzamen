
def polindrom(slovo):
    if len(slovo) <= 1:
        return True
    if slovo[0] != slovo[-1]:
        return False
    return polindrom(slovo[1:-1])
print(polindrom("шалаш"))