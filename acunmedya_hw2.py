def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} bir asal sayı değildir."
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return f"{sayi} bir asal sayı değildir."
    return f"{sayi} bir asal sayıdır."


def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == '-':
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == '*':
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    elif islem == '/':
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü!"

# Örnek Kullanım
print(asal_mi(7))  # Çıktı: 7 bir asal sayıdır.
print(asal_mi(10)) # Çıktı: 10 bir asal sayı değildir.

print(hesap_makinesi(5, 3, '+'))  # Çıktı: 5 + 3 = 8
print(hesap_makinesi(10, 2, '/'))  # Çıktı: 10 / 2 = 5.0
print(hesap_makinesi(4, 0, '/'))   # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
print(hesap_makinesi(6, 2, '%'))   # Çıktı: Geçersiz işlem türü!
