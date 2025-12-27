#!/bin/bash
# Script para automatizar comandos do git
# Automação dos comandos de atualização do repositório

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== Script de Atualização do Repositório ===${NC}"
echo ""

# 1. Verificar status
echo -e "${YELLOW}[1/4] Verificando status do repositório...${NC}"
git status
echo ""

# 2. Adicionar todos os arquivos
echo -e "${YELLOW}[2/4] Adicionando arquivos...${NC}"
git add .
echo -e "${GREEN}✓ Arquivos adicionados${NC}"
echo ""

# 3. Commit com mensagem
echo -e "${YELLOW}[3/4] Criando commit...${NC}"
if [ -z "$1" ]; then
    # Se nenhuma mensagem for fornecida, usar mensagem padrão
    COMMIT_MSG="Add Arquivos"
    echo -e "${YELLOW}Usando mensagem padrão: '$COMMIT_MSG'${NC}"
else
    # Usar a mensagem fornecida como argumento
    COMMIT_MSG="$1"
    echo -e "${YELLOW}Usando mensagem: '$COMMIT_MSG'${NC}"
fi

git commit -m "$COMMIT_MSG"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Commit criado com sucesso${NC}"
else
    echo -e "${RED}✗ Erro ao criar commit ou nenhuma alteração para commitar${NC}"
fi
echo ""

# 4. Push para o repositório remoto
echo -e "${YELLOW}[4/4] Enviando para o GitHub...${NC}"
git push
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Alterações enviadas com sucesso!${NC}"
else
    echo -e "${RED}✗ Erro ao enviar alterações${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}=== Atualização concluída! ===${NC}"
