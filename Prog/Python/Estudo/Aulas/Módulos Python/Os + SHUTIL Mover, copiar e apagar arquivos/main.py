import os
import shutil

caminho_original = '/home/alvaro/Desktop/Python_3_do_Basico_Ao_Avancado_com_projetos_reais_Atualizado_2022_2'
caminho_novo = '/home/alvaro/Desktop/Python_3_do_Basico_Ao_Avancado_com_projetos_reais_Atualizado_2022_10'

# try:
#     os.mkdir(caminho_novo)
# except FileExistsError as e:
#     print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root,file)
        new_file_path = os.path.join(caminho_novo, file)
        

        if '.html' in file:
            os.remove(new_file_path)