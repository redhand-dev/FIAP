from math import factorial
import pandas as pd

minutos = int(input("Digite os minutos atuais que estão na canto inferior da tela de seu computador: "))

factorial = 1

if minutos <= 59 :
    for i in range (1, minutos + 1):
        factorial = factorial * 1
    print(f"A senha para desbloqueio é LIBERDADE{factorial}")

exit()