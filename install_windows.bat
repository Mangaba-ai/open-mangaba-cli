@echo off
REM ========================================
REM  MANGABA CLI - Instalador para Windows
REM ========================================
REM Este script configura o comando 'mangaba' globalmente

echo.
echo 🥭 MANGABA CLI - Instalador para Windows
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ❌ Python não encontrado!
    echo 💡 Instale o Python primeiro: https://python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Opções de instalação
echo Escolha o método de instalação:
echo.
echo 1. Pasta do usuário (%USERPROFILE%\bin) - Recomendado
echo 2. Pasta do sistema (C:\Windows\System32) - Requer admin
echo 3. Adicionar pasta atual ao PATH
echo 4. Criar alias no PowerShell
echo.
set /p choice="Digite sua escolha (1-4): "

if "%choice%"=="1" goto install_user
if "%choice%"=="2" goto install_system
if "%choice%"=="3" goto install_path
if "%choice%"=="4" goto install_powershell

echo ❌ Opção inválida!
pause
exit /b 1

:install_user
echo.
echo 📁 Instalando na pasta do usuário...
if not exist "%USERPROFILE%\bin" mkdir "%USERPROFILE%\bin"
copy "mangaba.bat" "%USERPROFILE%\bin\" >nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Erro ao copiar arquivo!
    pause
    exit /b 1
)

REM Adiciona ao PATH do usuário
echo 🔧 Adicionando ao PATH...
setx PATH "%PATH%;%USERPROFILE%\bin" >nul
echo.
echo ✅ Instalação concluída!
echo 💡 Reinicie o terminal e digite 'mangaba' para testar
goto end

:install_system
echo.
echo 🔐 Instalando na pasta do sistema (requer admin)...
net session >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ❌ Este método requer privilégios de administrador!
    echo 💡 Execute como administrador ou escolha outra opção
    pause
    exit /b 1
)

copy "mangaba.bat" "C:\Windows\System32\" >nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Erro ao copiar arquivo!
    pause
    exit /b 1
)

echo ✅ Instalação concluída!
echo 💡 Digite 'mangaba' em qualquer terminal para testar
goto end

:install_path
echo.
echo 🔧 Adicionando pasta atual ao PATH...
set CURRENT_DIR=%cd%
setx PATH "%PATH%;%CURRENT_DIR%" >nul
echo.
echo ✅ Instalação concluída!
echo 💡 Reinicie o terminal e digite 'mangaba' para testar
echo 📁 Pasta adicionada: %CURRENT_DIR%
goto end

:install_powershell
echo.
echo 🔧 Criando alias no PowerShell...
set CURRENT_DIR=%cd%
set PROFILE_PATH=%USERPROFILE%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

REM Cria diretório se não existir
if not exist "%USERPROFILE%\Documents\WindowsPowerShell" mkdir "%USERPROFILE%\Documents\WindowsPowerShell"

REM Adiciona função ao perfil
echo. >> "%PROFILE_PATH%"
echo # MANGABA CLI >> "%PROFILE_PATH%"
echo function mangaba { python "%CURRENT_DIR%\mangaba.py" $args } >> "%PROFILE_PATH%"

echo ✅ Alias criado no PowerShell!
echo 💡 Reinicie o PowerShell e digite 'mangaba' para testar
echo 📄 Perfil: %PROFILE_PATH%
goto end

:end
echo.
echo 🎉 Instalação finalizada!
echo.
echo 📋 Comandos disponíveis:
echo   mangaba           - Jornada completa
echo   mangaba --quick   - Comandos rápidos
echo   mangaba --examples - Exemplos práticos
echo.
echo 🔍 Para testar: abra um novo terminal e digite 'mangaba'
echo.
pause