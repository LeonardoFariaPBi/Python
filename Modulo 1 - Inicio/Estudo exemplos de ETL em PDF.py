import pdfplumber
import pandas as pd
import re

# --- Função para extrair dados do PDF ---
def extract_bank_pdf(path):
    records = []
    agency = ""
    account = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = text.splitlines()

            # Detecta agência e conta
            for line in lines:
                if "Agência" in line and "Conta" in line:
                    match = re.search(r"Agência:\s*(\d+)\s*Conta:\s*([\d\-]+)", line)
                    if match:
                        agency, account = match.groups()

            # Detecta transações
            for line in lines:
                # Exemplo de regex para capturar Data, Histórico, Valor, Saldo
                match = re.match(r"(\d{2}/\d{2}/\d{4})\s+(.+?)\s+([\-]?\d+,\d{2})\s+(\d+,\d{2})", line)
                if match:
                    date, history, value, balance = match.groups()
                    records.append({
                        "Agência": agency,
                        "Conta": account,
                        "Data": date,
                        "Histórico": history.strip(),
                        "Valor": value,
                        "Saldo": balance
                    })

    return pd.DataFrame(records)

# --- Executa ETL ---
df = extract_bank_pdf("extrato_bancario.pdf")

# Salva em CSV e SQLite
df.to_csv("extrato.csv", index=False, encoding="utf-8")

print(df)