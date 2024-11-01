def prog5():
    print("digite alguns inteiros, cada um seguido de enter, digite somente para sair. ")

    soma = 0
    contador = 0
    while True:
        try:
            linha = input("digite um inteiro: ")
            if linha == "":
                break
            else: 
                numero_int = int(linha)
                soma=soma+numero_int
                contador+=1
        except ValueError as VErr:
            print("conversao impossivel")
            print("resposta: ", VErr)
            while True:
                print("é para digitar inteiro")
                print("dgite novamente")
                try:
                    linha2=input()
                    numero_int2=int(linha2)
                except:
                    pass
                else:
                    numero_int = numero_int2
                    soma=soma+numero_int
                    contador+=1
                    break



    if(contador):
        print(f"soma = {soma} e media = {soma/contador}")
    else:
        print("nao ha dado para calcular")

    print("quantidade de numeros digirados: ", contador)
    print(f"soma = {soma} e media = {soma/contador}")

def prog7():
    soma = 0
    contador = 0
    while True:
        try:
            linha = input()
            if linha == "":
                break
            else: 
                numero_int = int(linha)
                soma=soma+numero_int
                contador+=1
        except EOFError:
            break
        except ValueErrora as VErr:
            print("conversao impossivel")
            print("resposta: ", VErr)
            while True:
                print("é para digitar inteiro")
                print("digite novamente")
                try:
                    linha2=input()
                    numero_int2=int(linha2)
                except:
                    pass
                else:
                    numero_int = numero_int2
                    soma=soma+numero_int
                    contador+=1
                    break



    if(contador):
        print(f"soma = {soma} e media = {soma/contador}")
    else:
        print("nao ha dado para calcular")











































if __name__ =="__main__" :
    prog5()