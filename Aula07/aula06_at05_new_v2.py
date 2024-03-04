import openpyxl
'''
Atividade: juntar 2 planilhas produtos e categorias... e gerar uma terceira com a junçao
    - abrir o primeiro arquivo
    - guardar a info do arquivo
    - abrir o segundo arquivo
    - guardar a info do segundo arquivo
    - mesclar/tratar as info com os valores correspondentes
    - manter somente as info necessarias
    - converter as informações para o arquivo xlsx
'''
def CarregarArquivoCSV(nome_arquivo):
    dados_arquivo = open(file=nome_arquivo + '.csv', mode='r', encoding='utf-8')
    lista_info = [] #array vazio
    for linha in dados_arquivo:
        colunas = linha.strip().split(';')
        lista_info.append(colunas)
    return lista_info

def ConcatenarArquivoCSV(categoriasCSV, produtosCSV):
    dados_csv = [] #array vazio
    for produto in produtosCSV:
        index = int(produto[2])-1
        #dados_csv.append([*produto, *categoriasCSV[index]])
        dados_csv.append([
            produto[0],
            produto[1],
            produto[4],
            produto[8],
            produto[9],
            categoriasCSV[index][0],
            categoriasCSV[index][1]            
        ])
    return dados_csv

def GravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook() # -> criando o excel
        planilha = excel.active # -> a primeira aba ativa

        for linha in dados:
            planilha.append(linha) # -> adicionar mais infomações
        excel.save(nome_arquivo + '.xlsx') # -> fecho a conexão e dou o nome para o arquivo

        print('Dados salvo com sucesso no arquivo {}'.format(nome_arquivo))

    except Exception as ex:
        print('Ocorreu um erro {}'.format(ex))


dados_categoria = CarregarArquivoCSV('categorias')
dados_produto = CarregarArquivoCSV('produtos')
dados_concatenados = ConcatenarArquivoCSV(dados_categoria,dados_produto)

GravarArquivoXLSX(dados_concatenados,'info_tratadas')

#print(dados_categoria)
#print(dados_produto)

