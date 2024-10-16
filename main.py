import functions as f

if __name__ == "__main__":
    """Questão 1"""
    print('Questão#####1\n')
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    print(f.soma_pares(lista))

    """Questão 2"""
    print('\nQuestão#####2\n')
    lista_palavras = ["engenharia", "dados", "python", "engenharia", "dados", "engenharia","produção", "engenharia"]
    palavra = "engenharia"
    count = f.contar_palavra(lista_palavras, palavra)
    print(f"A palavra {palavra} aparece {count} vezes.")

    """Questão 3"""
    print('\nQuestão#####3\n')
    lista_maior_10 = [4, 11, 7, 15, 20, 3, 9, 6, 8, 16, 20]
    print(f.filtrar_maiores(lista_maior_10))

    """Questão 4"""
    print('\nQuestão#####4\n')
    lista_grupos = ["dados", "engenharia", "desenvolvimento", "python", "processos", "data", "pipeline"]
    print(f.agrupar_por_primeira_letra(lista_grupos))

    """Questão 5"""
    print('\nQuestão#####5\n')
    numero = 5
    print(f.fatorial(numero))

    """Questão 6"""
    print('\nQuestão#####6\n')
    data = "2021-09-11"
    print(f.converter_data(data))

    """Questão 7"""
    print('\nQuestão#####7\n')
    polindromo = "arara"
    print(f.verificar_palindromo(polindromo))

    """Questão 7"""
    print('\nQuestão#####7\n')
    arquivo = "arquivo.txt"
    print(f.contar_linhas(arquivo))

