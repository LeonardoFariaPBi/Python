#!/bin/bash

echo "📌 Repositório: Hashtag/Python"

if git diff --quiet && git diff --cached --quiet; then
    echo "✅ Nenhuma alteração para enviar."
    exit 0
fi

git add .
git commit -m "Update automático"
git push

echo "🚀 Push finalizado!"
