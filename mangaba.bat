@echo off
REM ========================================
REM  MANGABA CLI - Script de Execução
REM ========================================
REM 
REM Para usar globalmente (comando 'mangaba' em qualquer lugar):
REM 1. Copie este arquivo para C:\Windows\System32\ (requer admin)
REM 2. OU copie para %USERPROFILE%\bin\ e adicione ao PATH
REM 3. OU adicione esta pasta ao PATH do sistema
REM 
REM Uso: mangaba [opções]
REM   mangaba           - Jornada completa
REM   mangaba --quick   - Comandos rápidos
REM   mangaba --examples - Exemplos práticos
REM ========================================

REM Detecta o diretório do script
set SCRIPT_DIR=%~dp0

REM Executa o script Python
python "%SCRIPT_DIR%mangaba.py" %*

REM Verifica se houve erro
if %ERRORLEVEL% neq 0 (
    echo.
    echo ❌ Erro ao executar mangaba.py
    echo 💡 Verifique se o Python está instalado e no PATH
    echo 📁 Diretório atual: %SCRIPT_DIR%
    pause
)