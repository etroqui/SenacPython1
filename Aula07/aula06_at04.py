import openpyxl
from os import system
system('cls')

def ler_planilha(p_arquivoCSV):
    try:
        v_filename          = p_arquivoCSV
        v_lista_csv_total   = []

        dados = open(file=v_filename,mode='r',encoding='utf-8')

        for linha in dados:
            colunas = linha.strip().split(';')
            v_lista_csv_total.append(colunas)

        print(f'Dados lidos com sucesso do arquivo CSV "{v_filename}"')
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

v_filename_in_csv           = input('Digite o nome do arquivo CSV de Entrada, sem a extensão ===> ')
v_filename_in_csv           += '.csv'
v_file_carregado_csv        = ler_planilha(v_filename_in_csv)

v_filename_out_excel        = input('\nDigite o nome do arquivo Excel de Saída, sem a extensão ===> ')
v_filename_out_excel        += '.xlsx'
criar_planilha(v_filename_out_excel, v_file_carregado_csv)