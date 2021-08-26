import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
from regression import *
import time

def changes_1(e):
    global load_img_gp_e
    #Botão para gerar o gráfico resultante.
    img_gp_e = Image.open("../images/sgh.png")
    load_img_gp_e = resize_button_img(img_gp_e)
    bt_generate_graphic.config(image=load_img_gp_e)
    label_info["text"] = "Generate a graphic using the entry datas"

def changes_2(e):
    global load_img_ge_e
    #Botão para calcular o erro global.
    img_ge_e = Image.open("../images/sgeh.png")
    load_img_ge_e = resize_button_img(img_ge_e)
    bt_calculate_error.config(image=load_img_ge_e)
    label_info["text"] = "Calculates and shows the global error of linear regression"

def changes_3(e):
    global load_img_gd_e
    #Botão para calcular o grau de dependência entre os pontos.
    img_gd_e = Image.open("../images/sddh.png")
    load_img_gd_e = resize_button_img(img_gd_e)
    bt_degree_dependence.config(image=load_img_gd_e)
    label_info["text"] = "Calculates and shows the degree dependence of linear regression"

def changes_4(e):
    global load_img_gm_e
    #Botão para calcular o modelo matemático.
    img_gm_e = Image.open("../images/smh.png")
    load_img_gm_e = resize_button_img(img_gm_e)
    bt_calculate_model.config(image=load_img_gm_e)
    label_info["text"] = "Calculates and shows the mathematical model of linear straight"
    
def changes_5(e):
    bt_open.config(fg="white")
    bt_open.configure({"background":"#4087e3"})
    label_info["text"] = "Selection of the data file for treatment"

def changes_back_1(e):
    global load_img_gp_l
    #Botão para gerar o gráfico resultante.
    img_gp_l = Image.open("../images/sg.png")
    load_img_gp_l = resize_button_img(img_gp_l)
    bt_generate_graphic.config(image=load_img_gp_l)
    label_info["text"] = " "

def changes_back_2(e):
    global load_img_ge_l
    #Botão para calcular o erro global.
    img_ge_l = Image.open("../images/sge.png")
    load_img_ge_l = resize_button_img(img_ge_l)
    bt_calculate_error.config(image=load_img_ge_l)
    label_info["text"] = " "

def changes_back_3(e):
    global load_img_gd_l
    #Botão para calcular o grau de dependência entre os pontos.
    img_gd_l = Image.open("../images/sdd.png")
    load_img_gd_l = resize_button_img(img_gd_l)
    bt_degree_dependence.config(image=load_img_gd_l)
    label_info["text"] = " "

def changes_back_4(e):
    global load_img_gm_l
    #Botão para calcular o modelo matemático.
    img_gm_l = Image.open("../images/sm.png")
    load_img_gm_l = resize_button_img(img_gm_l)
    bt_calculate_model.config(image=load_img_gm_l)
    label_info["text"] = " "
    
def changes_back_5(e):
    bt_open.config(fg="white")
    bt_open.config(bg="#5f9ae8")
    label_info["text"] = " "

def popup_error():
    """
        Esta função gera uma mensagem/popup de erro caso o usuário tente clicar em um dos botões antes da passagem do arquivo para cálculo.
    """
    tk.messagebox.showerror("FILE ERROR", "No file reported, please select a file for data collection.")

def resize_img(image):
    """
        Função padroniza o tamanho das imagens que aparecem quando os dados estão sendo processados e após seu termino.
    """
    resized = image.resize((25,25), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized)

def resize_button_img(image):
    """
        Função padroniza o tamanho das imagens dos botões do menu.
    """
    resized = image.resize((200,40), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized)

def open_file():
    """
        Função será chamada após a passagem de um arquivo.
    """
    global load_img, check_img, label_status_check_img, label_status_check_text

    #Recebe o caminho do arquivo passado pelo usuário.
    window.filename = filedialog.askopenfilename(title="Select a data file", filetypes=(("CSV files (.csv)", "*.csv"),("Text files (.txt)", "*.txt")))

    #verifica se o arquivo é válido.
    if len(window.filename) > 4:
        #Caso a label de check já exista (não seja o primeiro arquivo), destroi a mesma antes de colocar a label de processando.
        if bt_open["text"] != " Select a file ":
            label_status_check_text.destroy()
            label_status_check_img.destroy()
        bt_open["text"] = window.filename

        #Cria a Label no frame mid, essa label irá contêr o texto e a imagem de carregamento.
        img = Image.open("../images/loading.png")
        load_img = resize_img(img)
        label_status_load_img = tk.Label(mid, bg="#D0DBE8", image=load_img)
        label_status_load_text = tk.Label(mid, text="The entry is being processed...", bg="#D0DBE8", font="Arial 12")

        #Arruma a localização das labels no frame.
        label_status_load_img.grid(row=2, column=0, sticky=tk.W)
        label_status_load_text.grid(row=2, column=1, sticky=tk.W)
        mid.update()

        #Processamento dos dados
        data = pd.read_csv(window.filename, delimiter=",", sep="\n")
        #Regressão dos dados
        model = stat_regression(data)

        #Atribui as funções aos botões (gerar gráfico e etc...)
        bt_generate_graphic.config(command=model.show_graphic)
        bt_calculate_error.config(command=model.show_error)
        bt_degree_dependence.config(command=model.show_degree_dep)
        bt_calculate_model.config(command=model.show_mathematical_model)

        #Cria a Label no frame mid, essa label irá contêr o texto e a imagem de conclusão.
        img = Image.open("../images/check.png")
        check_img = resize_img(img)
        label_status_check_img = tk.Label(mid, bg="#D0DBE8", image=check_img)
        label_status_check_text = tk.Label(mid, text="Data successfully loaded!", bg="#D0DBE8", font="Arial 12")

        #Destroi a label de carregamento (para colocar a de check).
        label_status_load_img.destroy()
        label_status_load_text.destroy()
        #Arruma a localização das labels no frame.
        label_status_check_img.grid(row=2, column=0, sticky=tk.W)
        label_status_check_text.grid(row=2, column=1, sticky=tk.W)
        
#Criação da janela principal, definição de cor e tamanho (da janela).
window = tk.Tk()
window.title('Menu')
window.geometry("700x350+600+250")
window.minsize(700,350)
window.maxsize(700,350)
window.config(bg="#D0DBE8")

#Criação de um frame superior da janela principal, onde estará contido o título do menu e a caixa de seleção do arquivo.
top = tk.Frame(window, bg="#D0DBE8")
top.place(relx="0.025", rely="0.025", relwidth="0.95", relheight="0.3")

#Titulo da janela principal.
label_title = tk.Label(top, text="StatisticalTool  |  Linear Regression", font="Arial 12", bg="#D0DBE8", height="2", fg="black")
#Botão onde será passado o arquivo.
bt_open = tk.Button(top, text=" Select a file ", font="Arial 12", fg="white", bg="#5f9ae8", bd=0, width="70", command=open_file)
label_info = tk.Label(window, bg="#D0DBE8", fg="black", text=" ", relief=tk.SUNKEN, anchor=tk.E, bd=0)

#Localização dos elementos no frame superior.
label_title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
bt_open.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label_info.pack(side=tk.BOTTOM, ipady=8, ipadx=2)

#Criação de um frame no meio da janela principal, onde estará a label de carregamento/check de dados.
mid = tk.Frame(window, bg="#D0DBE8")
mid.place(relx="0.025", rely="0.25", relwidth="0.95", relheight="0.08")

#Criação de um frame inferior da janela principal, onde estarão contidos os botões de respostas.
down = tk.Frame(window, bg="#D0DBE8")
down.place(relx="0.025", rely="0.42", relwidth="0.95", relheight="0.5")

bt1 = tk.Frame(down, bg="#D0DBE8")
bt1.place(relx="0.025", rely="0.025", relwidth="0.45", relheight="0.4")

bt2 = tk.Frame(down, bg="#D0DBE8")
bt2.place(relx="0.025", rely="0.5", relwidth="0.45", relheight="0.4")

bt3 = tk.Frame(down, bg="#D0DBE8")
bt3.place(relx="0.5", rely="0.5", relwidth="0.45", relheight="0.4")

bt4 = tk.Frame(down, bg="#D0DBE8")
bt4.place(relx="0.5", rely="0.025", relwidth="0.45", relheight="0.4")

#Botão para gerar o gráfico resultante.
img_button_gp = Image.open("../images/sg.png")
load_img_button_gp = resize_button_img(img_button_gp)
bt_generate_graphic = tk.Button(bt1, image=load_img_button_gp, bd=0, bg="#D0DBE8", command=popup_error)

#Botão para calcular o erro global.
img_button_ge = Image.open("../images/sge.png")
load_img_button_ge = resize_button_img(img_button_ge)
bt_calculate_error = tk.Button(bt2, image=load_img_button_ge, bd=0, bg="#D0DBE8", command=popup_error)

#Botão para calcular o grau de dependência entre os pontos.
img_button_gd = Image.open("../images/sdd.png")
load_img_button_gd = resize_button_img(img_button_gd)
bt_degree_dependence = tk.Button(bt3, image=load_img_button_gd, bd=0, bg="#D0DBE8", command=popup_error)

#Botão para calcular o modelo matemático.
img_button_gm = Image.open("../images/sm.png")
load_img_button_gm = resize_button_img(img_button_gm)
bt_calculate_model = tk.Button(bt4, image=load_img_button_gm, bd=0, bg="#D0DBE8", command=popup_error)

bt_generate_graphic.bind("<Enter>", changes_1)
bt_calculate_error.bind("<Enter>", changes_2)
bt_degree_dependence.bind("<Enter>", changes_3)
bt_calculate_model.bind("<Enter>", changes_4)
bt_open.bind("<Enter>", changes_5)

bt_generate_graphic.bind("<Leave>", changes_back_1)
bt_calculate_error.bind("<Leave>", changes_back_2)
bt_degree_dependence.bind("<Leave>", changes_back_3)
bt_calculate_model.bind("<Leave>", changes_back_4)
bt_open.bind("<Leave>", changes_back_5)

#Arruma a localização dos botões em seu frame (e os apresenta).
bt_generate_graphic.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
bt_calculate_error.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
bt_degree_dependence.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
bt_calculate_model.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

#Loop da janela principal.
window.mainloop()
