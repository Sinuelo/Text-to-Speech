import PyPDF2
import pyttsx3
import os
import customtkinter as ctk
from customtkinter import filedialog


# Essa função, além de abrir o arquivo, já lê e transforma para mp3
def abrir_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title='Selecionar Arquivo PDF', filetypes=[('Arquivos PDF', '*.pdf')])
    leitor_pdf = PyPDF2.PdfReader(caminho_arquivo)  # Le o arquivo pdf
    speaker = pyttsx3.init()           # Inicia o 'text-to-speech'
    speaker.setProperty('rate', 150)
    arquivo = os.path.basename(caminho_arquivo)
    nome_sem_extensao = os.path.splitext(arquivo)[0]  # Pega o nome do arquivo para salvar depois como mp3

    texto_completo = ''  # Variável que armazena o texto de todas as páginas

    for pagina in range(len(leitor_pdf.pages)):
        texto = leitor_pdf.pages[pagina].extract_text()
        texto_limpo = texto.strip().replace('\n', ' ')
        texto_completo += texto_limpo + ' '  # Concatena o texto de todas as páginas

    speaker.save_to_file(texto_completo, f'{nome_sem_extensao}.mp3')
    speaker.say(texto_completo)
    speaker.runAndWait()
    speaker.stop()


janela = ctk.CTk()  # Criar a janela
janela.title('PDF para MP3')    # Mudar o título da janela
janela.resizable(width=False, height=False)


lbl_msg = ctk.CTkLabel(janela,text='Selecione o arquivo em PDF que gostaria de transformar para mp3')
lbl_msg.grid(row=0, column=0, pady=10, padx=10)


btn_arquivo = ctk.CTkButton(master=janela, command=abrir_arquivo, text='Selecionar Arquivo')
btn_arquivo.grid(row=1, column=0, columnspan=2)


janela.mainloop()