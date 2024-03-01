from random import randint
print("=========================")
print("   STREAMING DE VIDEO    ")
print("=========================")

filmes = ["Bastardos Inglorios","Ilha Do Medo","Lobo De Wallstreet","Psicopata Americano"]
series = ["dexter","vikings","breaking bad","peaky blinders"]

print("[1] - Filmes")
print("[2] - Séries")
print("[3] - Sair")
try:
    op = int(input("Digite a opção desejada:"))
    if op==1:
        #filmes
        a = 0
        while a<=3:
            for x in filmes:
                print("[",a,"] - ",x," - ",randint(50,100)," R$")
                a+=1
    elif op==2:
        #series
        a = 0
        while a<=3:
            for x in series:
                print("[",a,"] - ",x," - ",randint(50,100)," R$")
                a+=1
    elif op==3:
        print("Programa Encerrado")
    else:
        print("Opção Inválida")
except:
    print("Insira um número válido!")







