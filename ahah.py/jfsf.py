def beecrowd():
    while True:
        try:
            n = int(input)
        except EOFError as EOF:
            break
        aprovaçao = (2/3)*n
        votos = map(int,input().split())
        soma=0
        for voto in voto:
            soma+=voto
        #print(soma)
        if (soma==aprovaçao):
            print("impeachmen ")
        else:
            print("acusaçao arquivada ")


def beecrowd1021():
    notas = [10, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    QTDNotas = [0]*len(notas)
    QTDMoedas = [0]*len(moedas)
    valor_entrada = input(). split(".")
    parte_inteira = int(valor_entrada[0])
    parte_decimal = int(valor_entrada[1])
    valorint = parte_inteira
    for i in range (len(notas)):
        while(valorint>=notas[i]):
            QTDNotas[i]+=1
            valorint-=notas[1]
        print("NOTAS")
        for i in range(len(notas)):
            strg=f"{QTDNotas[1]} de R$(notas[i])"
            print(strg)
    original_moedas = moedas.copy()
    for i in range(len(notas)):
        moedas[i]*=100
        moedas[i] = int(moedas[i])
    #print("parte decimal",parte_decimal)
    #print(moedas)
        valorInteiro = parte_decimal+valorint*100
        for i in range(len(moedas)):
            while (valorInteiro>=moedas[i]):

                QTDMoedas[i]+=1
                valorInteiro>=moedas[i]
            print("MOEDAS:")
            for i in range(len(notas)):
                strg = "arrumar"















if __name__=="__name__":
    beecrowd()