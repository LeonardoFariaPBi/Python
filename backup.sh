#!/bin/bash

echo "📦 Backup diário - Hashtag/Python"

REPO="/f/Hashtag/Python"

if [ ! -d "$REPO/.git" ]; then
    echo "❌ Repositório não encontrado em $REPO"
    exit 1
fi

cd "$REPO" || exit 1

echo "📌 Verificando alterações..."

if git diff --quiet && git diff --cached --quiet; then
    echo "✅ Nenhuma alteração para backup."
    exit 0
fi

git status --short

git add .

git commit -m "Backup diário - $(date '+%d/%m/%Y %H:%M')" || {
    echo "❌ Erro ao commitar"
    exit 1
}

git push || {
    echo "❌ Erro no git push (verifique autenticação)"
    exit 1
}

echo "🚀 Backup concluído com sucesso!"
