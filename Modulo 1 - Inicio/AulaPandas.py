import pyautogui
import time
import pandas as pd

caminho = r"C:\Users\Gaming\Downloads\Vendas - Dez.xlsx"
tabela = pd.read_excel(caminho)

print(tabela)

faturamento = tabela["Valor Final"].sum()
qntd_produtos = tabela["Quantidade"].sum()

print(f"O faturamento foi de R${float(faturamento)}")
print(f"A quantidade de produtos vendidos foi de {float(qntd_produtos)}")
print("Fim da análise.")

# Exportar a base de dados para pdf
# ajustar os valores de faturamento e qntd_produtos para float com 2 casas decimais

faturamento = float(faturamento)
qntd_produtos = float(qntd_produtos)
faturamento = "{:.2f}".format(faturamento)
qntd_produtos = "{:.2f}".format(qntd_produtos)
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Relatório de Vendas - Dezembro", ln=True, align='C') # type: ignore
pdf.cell(200, 10, txt=f"Faturamento: R${faturamento}", ln=True, align='L') # type: ignore
pdf.cell(200, 10, txt=f"Quantidade de Produtos Vendidos: {qntd_produtos}", ln=True, align='L') # type: ignore
pdf_output_path = r"C:\Users\Gaming\Downloads\Relatorio_Vendas_Dezembro.pdf"
pdf.output(pdf_output_path)