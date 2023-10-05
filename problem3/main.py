def cetak_table_perkalian(number):
    if number < 1 or number > 30:
        return "Error: Input harus 1 sampai 30"

    pattern = ""  
    atur_jarak = len(str(number * number))
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            result = i * j
            pattern += f"{result:>{atur_jarak}} "
        pattern += '\n'  
    
    return pattern
if __name__ == '__main__':
    result=cetak_table_perkalian(9)
    print(result)
    """
    1  2  3  4  5  6  7  8  9 
    2  4  6  8 10 12 14 16 18 
    3  6  9 12 15 18 21 24 27 
    4  8 12 16 20 24 28 32 36 
    5 10 15 20 25 30 35 40 45 
    6 12 18 24 30 36 42 48 54 
    7 14 21 28 35 42 49 56 63 
    8 16 24 32 40 48 56 64 72 
    9 18 27 36 45 54 63 72 81 
# #     """
