# pip install pyautogui

import pyautogui
import time

# pip install pandas openpyxl
import pandas

pyautogui.PAUSE = 1

# pytogui.click -> clicar
# pytogui.press -> precionar uma tecla
# pytogui.write -> escrever
# pytogui.hotkey -> atalho de teclado, exemplo: (ctrl, C)

# Passo 1: Abrir o sistema da empresa

# abrir o google chrome
# apertar a tecla (win)
pyautogui.press("win")

# digitar o texto chrome
pyautogui.write("opera")

# apertar ENTER
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter") # entrar no link apertando ENTER

# pedir para o computador esperar 3 segundos
time.sleep(3)


# Passo 2: Fazer Login
pyautogui.click(x=311, y=383)

# escrever o email
pyautogui.write("thiagolink500@gmail.com")

# apertar TAB para selecionar a senha
pyautogui.press("tab")

# escrever a senha
pyautogui.write("BNWT6raP")
pyautogui.press("tab")

# apertar ENTER
pyautogui.press("enter")


# Passo 3: Importar a base de dados dos produtos

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(5)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=313, y=279)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter") # enviar produto

# Passo 5: Repetir o passo 4 até acabar todos os produtos