def script():
    vC = [1,3.4, "A" , "IFSC"]
    print(vC)
    input("precione enter para continuar")
    print("inserçao de 50 na posiçao 0")
    vC.insert(0,50)
    print(vC)
    input("precione enter para continuar")
    print("inserçao de B na posiçao 3")
    vC.insert(3,"B")
    print(vC)
    input("inserçao no final do vetor de 11")
    vC.append(11)
    print(vC)
    return vC

def script1():
    vC = [1,3.4, "A" , "IFSC"]
    vC.insert(0,50)
    vC.insert(3,"B")
    vC.append(11)
    vC.append("A")
    return vC

def script2(vetA):
    print ("vetor recebido ",vetA)
    print ("remoçao do valor ",vet[2])
    vetA.remove(3.4)

    print("escolha a remoçao do A:")
    escolha = input("preciona 1 para remover a primeira ocorrencia, outra tecla para todas ")
    if(escolha == "1"):
        vetA.remove("A")
    else:
        while "A" in vetA:
            vetA.remove("A")
        print("valor final: ", vetA)
    print(vetA)

def script3(vetB):
    vetB_copia = vetB.copy()
    print("vetor recebido: ", vetB)
    print("remoçao por del")
    posiçao_inicial = 1
    posiçao_final = 3
    del vetB[posiçao_inicial:posiçao_final]
    print(f"vetor com posiçao[{posiçao_inicial}:{posiçao_final}] removida: ",vetB)
    print("romover por pop: ")

def script4():
    valores = list(range(1,11))
    anos = list(range(2020,2060,10))
    lista_concatenada = valores+anos
    print(valores)
    valores.extend(anos)
    print(valores)
    print(lista_concatenada)

def script5():
    mercado = ["ouro","bitcoin","titulos"]
    print(mercado)
    mercado.sort()
    print(mercado)
    moedas = ["ouro", "bitcoin", "titulos", "dolar", "real"]
    moedas_original = moedas.copy
    moedas.sort(key=str)
    print(moedas)


if __name__ == "__main__":
    #vet = script()
    #script1(vet)
    #script2(vet)
    #script3()
    #script4()
    script5()












































