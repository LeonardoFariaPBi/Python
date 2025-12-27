# Automação de Comandos Git

Este repositório contém scripts para automatizar os comandos git de atualização.

## Scripts Disponíveis

### 1. atualizar.sh (Linux/Mac)
Script bash para sistemas Unix-like (Linux, Mac, WSL).

**Uso:**
```bash
# Com mensagem padrão "Add Arquivos"
./atualizar.sh

# Com mensagem personalizada
./atualizar.sh "Sua mensagem de commit"
```

### 2. atualizar.bat (Windows)
Script batch para Windows.

**Uso:**
```batch
# Com mensagem padrão "Add Arquivos"
atualizar.bat

# Com mensagem personalizada
atualizar.bat "Sua mensagem de commit"
```

## O que os scripts fazem?

Os scripts automatizam os seguintes comandos git:

1. `git status` - Mostra o status atual do repositório
2. `git add .` - Adiciona todos os arquivos modificados
3. `git commit -m "mensagem"` - Cria um commit com a mensagem especificada
4. `git push` - Envia as alterações para o GitHub

## Exemplos de Uso

```bash
# Adicionar novos exercícios
./atualizar.sh "Adiciona exercícios do módulo 8"

# Corrigir erros
./atualizar.sh "Corrige typo no README"

# Atualizar tutorial
./atualizar.sh "Atualiza tutorial de strings"
```

## Pré-requisitos

- Git instalado e configurado
- Autenticação configurada para o GitHub (SSH ou HTTPS)
- Permissões de escrita no repositório

## Solução de Problemas

### Erro de permissão (Linux/Mac)
Se você receber um erro de permissão ao executar o script, torne-o executável:
```bash
chmod +x atualizar.sh
```

### Erro de autenticação
Se você receber um erro de autenticação ao fazer push:
- Configure suas credenciais do Git
- Use SSH keys ou GitHub token para autenticação

## Comandos Manuais

Se preferir executar os comandos manualmente, consulte `_Tutoriais/Atualizar.txt`.
