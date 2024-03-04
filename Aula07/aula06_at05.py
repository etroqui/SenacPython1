import openpyxl
from os import system
system('cls')

#ler os arquivos csv de entrada... categorias.csv e produtos.csv
def ler_arquivo_in(p_arquivo_1_csv, p_arquivo_2_csv):
    
    try:
        v_filename_1_csv    = p_arquivo_1_csv
        v_filename_2_csv    = p_arquivo_2_csv
        #array para guardar o arquivo
        v_lista_csv_total   = []

        #o encoding é pra nao ter problemas com acentuacao
        dados_1_csv = open(file=v_filename_1_csv, mode='r', encoding='utf-8')
        for linha_1 in dados_1_csv:
            colunas_1 = linha_1.strip().split(';')
            dados_2_csv = open(file=v_filename_2_csv, mode='r', encoding='utf-8')
            for linha_2 in dados_2_csv:
                colunas_2 = linha_2.strip().split(';')
                if int(colunas_1[2]) == int(colunas_2[0]):
                    colunas_final = colunas_1 + colunas_2
                    v_lista_csv_total.append(colunas_final)

        print(f'Dados carregados com sucesso dos arquivos CSV "{v_filename_1_csv}" e "{v_filename_2_csv}"')
        return v_lista_csv_total

    except PermissionError:
        print('arquivo ja aberto')
    except FileNotFoundError:
        print('Arquivo CSV de Entrada não encontrado')
    except Exception as ex:
        print(f'Ocorreu o erro {ex}')

def criar_planilha(p_filename_XLSX, p_file_carregado_CSV):

    try:
        excel               = openpyxl.Workbook()
        planilha            = excel.active          # primeira aba ativa
        v_filename_XLSX     = p_filename_XLSX

        for linha in p_file_carregado_CSV:
            planilha.append(linha)           # adicionar mais informacoes

        excel.save(v_filename_XLSX)

        print(f'Dados gravados com sucesso no arquivo EXCEL "{v_filename_XLSX}"\n')
    except PermissionError:
        print('arquivo ja aberto')
    except Exception as ex:
        print(f'Ocorreu o erro {ex}')


v_arquivo_1_in_csv = 'produtos.csv'
v_arquivo_2_in_csv = 'categorias.csv'
v_arquivo_out_excel = 'resultado.xlsx'

v_arquivo_final_csv = ler_arquivo_in(v_arquivo_1_in_csv,v_arquivo_2_in_csv)
criar_planilha(v_arquivo_out_excel, v_arquivo_final_csv)

