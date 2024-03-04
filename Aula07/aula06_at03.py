import openpyxl

def criar_planilha(arquivo,dados):
    try:
        excel               = openpyxl.Workbook()
        planilha            = excel.active          # primeira aba ativa
        v_filename          = arquivo

        for linha in dados:
            planilha.append(linha)           # adicionar mais informacoes

        excel.save(v_filename)

        print(f'Dados salvos com sucesso no arquivo {v_filename}')
    except PermissionError:
        print('arquivo ja aberto')
    except Exception as ex:
        print(f'Ocorreu o erro {ex}')


arquivo_excel   = 'minhas_series.xlsx'
dados           = [
                    ['Doctor Who','1960'],
                    ['Doctor Who Versao 2','1965'],
                    ['Doctor Who Versao 3','1970'],
                    ['Doctor Who Versao 4','1975'],
                    ['Doctor Who Versao 5','1980'],
                    ['Doctor Who Versao 6','1985'],
                    ['Doctor Who Versao 7','1990'],                    
                    ['Doctor Who Versao 8','1995']
]


criar_planilha(arquivo_excel,dados)