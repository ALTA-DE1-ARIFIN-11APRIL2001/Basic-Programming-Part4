def play_with_asterisk(n):
    pattern = ""
    for i in range(1, n + 1):
        spasi_kiri = ' ' * (n - i)
        asterisk = '* ' * i
        baris = spasi_kiri + asterisk
        pattern += baris + '\n'
    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
