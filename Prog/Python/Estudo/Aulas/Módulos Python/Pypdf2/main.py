import PyPDF2
import os

caminho_pdf = 'pdf'

"""
pdf_gerado = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_pdf):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        pdf_gerado.append(arquivo_pdf)

with open(f'{caminho_pdf}/novo_arquivo_pdf.pdf', 'wb') as meu_novo_pdf:
    pdf_gerado.write(meu_novo_pdf)


"""

"""

with open('pdf/novo_arquivo_pdf.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()
    print(num_paginas)
    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
"""
