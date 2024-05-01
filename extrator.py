#Pacotes e bibliotecas utilizados
import PyPDF2
import os
import pandas as pd
import shutil
from PyPDF2 import PdfReader

def extrair_texto_pdf(caminho_arquivo): #Funçãoo para extrair todo o texto contido no PDF e salvar na variável texto em formato str
    texto = ""
    with open(caminho_arquivo, "rb") as arquivo_pdf: 
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf) 
        for pagina in range(len(leitor_pdf.pages)):
            texto += leitor_pdf.pages[pagina].extract_text()
    return texto

def remessa_notas(arquivo): #Função para obter o número da remessa contido dentro do PDF da nota fiscal
    remessa = arquivo[-7].split()[-5]
    if remessa.isdigit(): #Verifica se o valor encontrado é um número, caso contrário ele retorna o numero 0
        return remessa
    else:
        return 0
    
def remessa_espelhos(arquivo): #Função para obter o número da remessa contido dentro do PDF do espelho de frete 
    if len(arquivo) > 29:
        remessa = arquivo[29]
        remessa = remessa.split()[-2]
        if remessa.isdigit(): #Nessa parte da funcao ele, novamente, verifica se o valor encontrado é um número, caso constrário ele me retorna o valor 0
            return remessa
    return 0
    
def n_nota(arquivo): #Função para obter o número da nota fiscal
    nota = arquivo[4].split('E')[1]
    if nota.isdigit(): #Novamente verifica se é um número válido, caso contrário retorna o valor 0
        return nota
    else:
        return 0

def valor(arquivo): #Função para extrair o valor da nota fiscal para uma segunda comparação caso seja necessário
    valor = arquivo[41]
    valor = float(valor.replace('.', '').replace(',', '.'))
    return valor

pasta_notas = r"C:\Users\sonia\Desktop\Lucas Geral\leitor de nfs\NFS filial"

resultados_notas = []

#Esse laço de repetição itera sobre todos os arquivos presentes na pasta de notas fiscais e aplica as funções acima em cada um deles, salvando as informações num dict e em seguida em uma lista

for arquivo_nome in os.listdir(pasta_notas):  
    if arquivo_nome.lower().endswith(".pdf"):
        caminho_nota = os.path.join(pasta_notas, arquivo_nome)
        texto_pdf = extrair_texto_pdf(caminho_nota)
        linhas = texto_pdf.splitlines()
        resultado = {
            "Remessa": remessa_notas(linhas),
            "N_Nota": n_nota(linhas),
            "Valor": valor(linhas)
        }
        resultados_notas.append(resultado)


df_notas = pd.DataFrame(resultados_notas)

#print(df_notas)

#df_notas.to_csv(r'C:\Users\sonia\Desktop\Lucas Geral\leitor de nfs\resultados.csv', index=False)

pasta_espelhos = r"C:\Users\sonia\Desktop\Lucas Geral\leitor de nfs\ESPELHOS filial"
pasta_destino = r"C:\Users\sonia\Desktop\Lucas Geral\leitor de nfs\Espelhos corrigidos"

# Verifique se a pasta de destino existe, se não, crie-a
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

#O laço de repetição abaixo basicamente lê os arquivos de espelho de frete presente na pasta e aplica a função que extrai o dado de remessa dele
for arquivo in os.listdir(pasta_espelhos): 
    if arquivo.lower().endswith('.pdf'):
        caminho_espelho = os.path.join(pasta_espelhos, arquivo)
        with open(caminho_espelho, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            linhas_de_texto = []
            for page in reader.pages:
              texto = page.extract_text()
        linhas_de_texto.extend(texto.splitlines())
        
        remessa = remessa_espelhos(linhas_de_texto)
        
# Após a extração da informação de Remessa, ele verifica se esse valor está presente do data frame que contém as informações sobre a nota fiscal, caso esteja presente então ele salva o espelho de frete com o numero da nota fiscal correspondente em uma nova pasta    
        if remessa in df_notas["Remessa"].values:
            n_nota_correspondente = df_notas.loc[df_notas["Remessa"] == remessa, "N_Nota"].iloc[0]
            
            novo_nome_arquivo = f"Espelho_{n_nota_correspondente}.pdf"
            
            caminho_destino = os.path.join(pasta_destino, novo_nome_arquivo)
            
            shutil.copy(caminho_espelho, caminho_destino)
                        
print("Todos os arquivos foram copiados")