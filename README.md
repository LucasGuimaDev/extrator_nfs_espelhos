## Extrator de nfs e espelhos
### Pacotes e bibliotecas utilizadas
- **Pandas:**
  <sub>Utilizado para salvar as informações extraídas das notas fiscais em um DataFrame para depois fazer o tratamento dos espelhos de frete;</sub>
- **shutil:**
  <sub>Utilizado ao final do código para mover o arquivo do eseplho de frete para a nova pasta;</sub>
- **os:**
  <sub>Utilizado para acessar os arquivos dentro das pastas;</sub>
- **PyPDF2:**
  <sub>Utilizado para trabalhar com arquivos PDF;</sub>
- **PdfReader:**
  <sub>Utilizado para ler e extrair as informações dos arquivos PDF.</sub>

### Projeto


O código presente neste repositório realiza a extração da informação do número de remessa presente nas notas fiscais e nos espelhos, faz a ligação entre eles e salva o espelho de frete com o número da nota fiscal, facilitando a localização futura do arquivo, uma vez que o arquivo original não possuia esse informação e era preciso abrir um por um para identificar.


![espelhos](https://github.com/LucasGuimaDev/extrator_nfs_espelhos/assets/123521555/010d5465-ac6a-4069-89e7-90da42ac1e8c)<br>
<sub>Imagem de como os arquivos de espelho de frete chegam</sub>


A idéia deste código veio a partir de uma dificuldade que percebi em unir uma informação na outra. Os PDFs das notas fiscais chegavam para mim com o número dela no nome do documento, porém o espelho de frete não, portanto era necessário abrir um a um para ver o número da remessa presente no documento e então renomear com o número correspondente.

![notas](https://github.com/LucasGuimaDev/extrator_nfs_espelhos/assets/123521555/fa305f7c-702f-4f0a-aa62-46be3a5562d8)<br>
<sub>Imagem de como os arquivos de notas fiscais chegam, a parte destacada mostra o número da nota fiscal.</sub>


Portanto esse código analisa automaticamente esse número e já salva em uma nova pasta com o nome correto.

![espelhos corrigidos](https://github.com/LucasGuimaDev/extrator_nfs_espelhos/assets/123521555/a3bd5639-54e1-4af0-8805-bd73f7eccc4b)<br>
<sub>Imagem dos arquivos de espelho de frete com o nome corrigido com o número da nota fiscal.</sub>

