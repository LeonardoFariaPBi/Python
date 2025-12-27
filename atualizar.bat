@echo off
REM Script para automatizar comandos do git no Windows
REM Automação dos comandos de atualização do repositório

echo === Script de Atualização do Repositório ===
echo.

REM 1. Verificar status
echo [1/4] Verificando status do repositório...
git status
echo.

REM 2. Adicionar todos os arquivos
echo [2/4] Adicionando arquivos...
git add .
echo Arquivos adicionados
echo.

REM 3. Commit com mensagem
echo [3/4] Criando commit...
if "%~1"=="" (
    set COMMIT_MSG=Add Arquivos
    echo Usando mensagem padrão: 'Add Arquivos'
) else (
    set COMMIT_MSG=%~1
    echo Usando mensagem: '%~1'
)

git commit -a -m "%COMMIT_MSG%"
if %errorlevel% equ 0 (
    echo Commit criado com sucesso
) else (
    echo Erro ao criar commit ou nenhuma alteração para commitar
)
echo.

REM 4. Push para o repositório remoto
echo [4/4] Enviando para o GitHub...
git push
if %errorlevel% equ 0 (
    echo Alterações enviadas com sucesso!
) else (
    echo Erro ao enviar alterações
    exit /b 1
)

echo.
echo === Atualização concluída! ===
pause
