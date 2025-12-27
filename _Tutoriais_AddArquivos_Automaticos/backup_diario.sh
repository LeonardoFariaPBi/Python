#!/bin/bash

echo "📦 Backup diário - Hashtag/Python"

cd /f/Hashtag/Python || exit 1

if git diff --quiet && git diff --cached --quiet; then
    echo "✅ Nenhuma alteração para backup."
    exit 0
fi

git add .
git commit -m "Backup diário - $(date '+%d/%m/%Y %H:%M')"
git push

echo "🚀 Backup concluído com sucesso!"
