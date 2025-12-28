#!/bin/bash

# =========================
# CONFIGURAÇÕES
# =========================
REPO="/f/Hashtag/Python"
LOG="$REPO/backup.log"
BRANCH="main"

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

# =========================
# STASH AUTOMÁTICO (SE NECESSÁRIO)
# =========================
STASH_APLICADO=false

if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "📦 Alterações locais detectadas — salvando stash..."
    git stash push -u -m "stash-backup-$(date '+%Y%m%d-%H%M%S')" || {
        echo "❌ Erro ao criar stash"
        exit 1
    }
    STASH_APLICADO=true
fi

# =========================
# ATUALIZA DO REMOTO
# =========================
echo "🔄 Atualizando repositório remoto..."
git pull --rebase origin "$BRANCH" || {
    echo "❌ Erro no git pull --rebase"
    exit 1
}

# =========================
# RESTAURA STASH (SE USADO)
# =========================
if [ "$STASH_APLICADO" = true ]; then
    echo "📤 Restaurando alterações locais..."
    git stash pop || {
        echo "⚠️ Conflito ao restaurar stash — resolva manualmente"
        exit 1
    }
fi

# =========================
# VERIFICA ALTERAÇÕES
# =========================
echo "📌 Verificando alterações para backup..."

if git diff --quiet && git diff --cached --quiet; then
    echo "✅ Nenhuma alteração para backup."
    echo "==============================="
    exit 0
fi

echo "📄 Arquivos alterados:"
git status --short

# =========================
# COMMIT + PUSH
# =========================
git add .

git commit -m "Backup diário automático - $(date '+%d/%m/%Y %H:%M')" || {
    echo "❌ Erro ao commitar"
    exit 1
}

git push origin "$BRANCH" || {
    echo "❌ Erro no git push"
    exit 1
}

echo "🚀 Backup concluído com sucesso!"
echo "==============================="
