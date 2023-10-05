def ubah_huruf(sentence):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    penggantian = 'KLMNOPQRSTUVWXYZABCDEFGHIJ'

    pattern = ""
    for karakter in sentence:
        if karakter.isalpha():
            if karakter.islower():
                indeks = alphabet.index(karakter.upper())
                karakter_terenkripsi = penggantian[indeks].lower()
            else:
                indeks = alphabet.index(karakter)
                karakter_terenkripsi = penggantian[indeks]
        else:
            karakter_terenkripsi = karakter
        pattern += karakter_terenkripsi    

    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB
