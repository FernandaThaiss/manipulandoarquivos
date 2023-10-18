np=int(input("qual a quantidade de pessoas?"))

for _ in range(np):
    nome=input("qual o nome?")
    n=input("qual o numero?")

    arquivo= open("arquivo.txt","a")
    arquivo.write(f"\n{nome}")
    arquivo.write(f"\n{n}")
    arquivo.close()

arquivo= open("arquivo.txt","r")
for linha in arquivo:
    print(linha, end=" ")