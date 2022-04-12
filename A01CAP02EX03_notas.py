import pandas as pd
import numpy as np

nota_impar = 0
soma_impar = 0
aluno_impar = 0

nota_par = 0
soma_par = 0
aluno_par = 0

nota = 0

i = 1
if 0 > nota <=10:
    print("Digite a nota entre 0 e 10")

print("CONTROLE DE NOTAS DE CLASSE")
print("")
Nome = input("Digite seu nome: ")
print("Olá,", Nome)
print("Vamos começar!")
print("")

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
while i <= 50:
    if i % 2 == 0 :
        nota_par = int(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
        soma_par = soma_par + nota_par
        aluno_par = aluno_par + 1
    i = i + 1
i = 0

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
while i <= 50:
    if i % 2 == 1 and aluno_par :
        nota_impar = int(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
        soma_impar = soma_impar + nota_impar
        aluno_impar = aluno_impar + 1
    i = i + 1
i = 0

if soma_par / 2 > soma_impar / 2 :
    print(f"A turma par obteve a maior nota da classe, com: {soma_par/2:}")
elif soma_impar / 2 > soma_par / 2 :
    print(f"A turma ímpar obteve a maior nota da classe, com: {soma_impar/2:}")