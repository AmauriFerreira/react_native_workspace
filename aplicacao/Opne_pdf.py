import xml.etree.ElementTree as ET
import pandas as pd
#import tabula as tb






#import email_module
#import futures_roll_over
#import get_db_data_module


#def Log_path_file():
    #str_1 = r"S:\\Mesa\\Quant\\LogFile\\"
    #str_2 = "roll_over_inner.txt"

    #path_temp = str_1 + str_2
    #return path_temp

def main():


    #check_tb_tbdictionary = (get_db_data_module.tb_tbdictionary())

    #Imprimir conteudo no formato xml
    #tree = ET.parse(r"C:\\Users\\Amauri\\Downloads\\Aquivo.xml")
    #root = tree.getroot()
    #arquivo1 = ET.tostring(root, encoding="utf8").decode("utf8")


    #Trasforma pdf em DataFrame



    ataframe_2 = pd.read_pdf(r"C:/Users/nh4am/Downloads/Arquivo_pdf/Reporte_40.pdf")
    arquivo2 = pd.DataFrame(ataframe_2)

    #Mudar nome das coluna
    #arquivo2.rename(columns={'ProductClass': 'productclass'}, inplace=True)
    #arquivo2.rename(columns={'Product': 'product'}, inplace=True)

    #Pegar trader
    #arquivo2_NomeTrade = arquivo2.loc[arquivo2['Trader'] == 'Antonio Mesquita Junior']


    #arquivo2_NomeTradetbdictionary = pd.merge(arquivo2_NomeTrade,check_tb_tbdictionary,on='productclass', how='left')


    #Se yellowkey estiver vazio pega apenas o produto
    #arquivo2_NomeTradetbdictionary['product'] = arquivo2_NomeTradetbdictionary['product'].str.upper()


    #arquivo2_NomeTradetbdictionary['product'] = np.where(arquivo2_NomeTradetbdictionary['product'].str.contains('CURNCY', 'COMDTY') == True,arquivo2_NomeTradetbdictionary['product'].str[:-7],arquivo2_NomeTradetbdictionary['product'])


    #arquivo2_NomeTradetbdictionary['product'] = np.where(arquivo2_NomeTradetbdictionary['product'].str.contains('INDEX') == True,arquivo2_NomeTradetbdictionary['product'].str[:-6], arquivo2_NomeTradetbdictionary['product'])


    #arquivo2_NomeTradetbdictionary['contract_ticker'] = arquivo2_NomeTradetbdictionary['product']+' '+arquivo2_NomeTradetbdictionary['yellowkey']


    #print(arquivo2_NomeTradetbdictionary2.columns)
    print(arquivo2)
    #print(arquivo2_NomeTrade.Trader)

    #stringlog1 = arquivo2_NomeTradetbdictionary.to_string()

    #arquivo = open(Log_path_file(),'w+')
    #Log_file_path = Log_path_file()

    #arquivo.write('\n\n Tabela roll_over_inner')

    #arquivo.write('\n\n\n Posições compradas:\n\n')
    #arquivo.write(stringlog1)
    #arquivo.close()

    #Subject = 'Tabela roll_over_inner'


    #email_module.send_teste(Log_file_path, Subject)


main()