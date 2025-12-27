# Confie em Deus e faça o seu melhor!
# Voce sera capaz de realizar grandes feitos!

# Passo a passo do desafio:
# Passo 1: Entrar no sistema da empresa
# Passo 2: Navegar até a seção de relatórios
# Passo 3: Baixar o relatório mensal
# Passo 4: Analisar os dados do relatório
# Passo 5: Calcular os indicadores ( Faturamento e quantidade de produtos vendidos)
# Passo 6: Enviar o resumo para a equipe por e-mail

# Preciso Automatizar o processo de entrar no sistema, baixar o relatório, analisar, calcular e enviar por e-mail
# Para isso, vou utilizar a linguagem Python e algumas bibliotecas específicas para cada tarefa
# Bibliotecas que podem ser utilizadas: pyautogui, pandas, openpyxl, pdfplumber, time, smtplib etc.
# pyautogui -> para automatizar cliques e digitação no sistema
# pandas -> para manipulação e análise de dados
# openpyxl -> para trabalhar com arquivos Excel
# pdfplumber -> para extrair texto de arquivos PDF
# smtplib -> para enviar e-mails automaticamente
# time -> para adicionar pausas entre as ações automatizadas
# O objetivo é economizar tempo e reduzir erros humanos no processo manual

# 1: Abrir o Chrome.
# 2: Digitei o link do sistema.
# 3: Apertei enter e esperei carregar.
# drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

import pyautogui
import time
import pandas as pd

navegador = "Navegador Opera GX"
link = "drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"

pyautogui.PAUSE = 0.5
# Abrir o navegador
pyautogui.press("win")
pyautogui.write(navegador)
pyautogui.press("enter")
time.sleep(3)
# Abrir o link do sistema
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
# Navegar até o relatório e baixar
pyautogui.click(x=868, y=356, clicks=2)  # Clicar na pasta do relatório
time.sleep(3)
pyautogui.rightClick(x=868, y=356)  # Clicar no Excel do relatório
time.sleep(3)
pyautogui.click(x=941, y=422)  # Baixar o relatório
time.sleep(3)
pyautogui.click(x=941, y=422)  # Acessa o relatório
time.sleep(5)
pyautogui.hotkey("alt", "f4")
time.sleep(5)