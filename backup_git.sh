#!/bin/bash

# =========================
# CONFIGURAÇÕES
# =========================
REPO="/f/Hashtag/Python"
LOG="$REPO/backup.log"

# =========================
# LOG + DEBUG
# =========================
exec >> "$LOG" 2>&1
echo "==============================="
echo "🕒 Execução iniciada em: $(date '+%d/%m/%Y %H:%M:%S')"

# =========================
# VALIDAÇÕES
# =========================
if [ ! -d "$REPO/.git" ]; then
    echo "❌ Repositório não encontrado em $REPO"
    exit 1
fi

cd "$REPO" || {
    echo "❌ Falha ao acessar o diretório"
    exit 1
}

echo "📌 Verificando alterações..."

# =========================
# VERIFICA ALTERAÇÕES
# =========================
if git diff --quiet && git diff --cached --quiet; then
    echo "✅ Nenhuma alteração para backup."
    exit 0
fi

echo "📄 Arquivos alterados:"
git status --short

# =========================
# BACKUP
# =========================
git add .

git commit -m "Backup diário automático - $(date '+%d/%m/%Y %H:%M')" || {
    echo "❌ Erro ao commitar"
    exit 1
}

git push || {
    echo "❌ Erro no git push (verifique autenticação)"
    exit 1
}

echo "🚀 Backup concluído com sucesso!"
echo "==============================="
