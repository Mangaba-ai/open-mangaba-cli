# 🚀 Solução Rápida - Comando 'mangaba' não encontrado

## ❌ Problema
```
mangaba : O termo 'mangaba' não é reconhecido como nome de cmdlet...
```

## ✅ Soluções Imediatas

### 1. **Uso Direto (Funciona Sempre)**
```bash
# No diretório do projeto
.\mangaba.bat

# Ou com Python diretamente
python mangaba.py
```

### 2. **PowerShell - Alias Temporário**
```powershell
# Criar alias para a sessão atual
Set-Alias mangaba "D:\open-mangaba-cli\open-mangaba-cli\mangaba.bat"

# Testar
mangaba
```

### 3. **PowerShell - Função Permanente**
```powershell
# Abrir perfil do PowerShell
notepad $PROFILE

# Adicionar esta linha (substitua o caminho):
function mangaba { & "D:\open-mangaba-cli\open-mangaba-cli\mangaba.bat" $args }

# Recarregar perfil
. $PROFILE
```

### 4. **CMD - Doskey**
```cmd
# Criar alias temporário
doskey mangaba="D:\open-mangaba-cli\open-mangaba-cli\mangaba.bat" $*

# Testar
mangaba
```

### 5. **Adicionar ao PATH (Permanente)**
```cmd
# Método 1: Via comando
setx PATH "%PATH%;D:\open-mangaba-cli\open-mangaba-cli"

# Método 2: Via interface gráfica
# 1. Win + R → sysdm.cpl
# 2. Avançado → Variáveis de Ambiente
# 3. PATH → Editar → Novo
# 4. Adicionar: D:\open-mangaba-cli\open-mangaba-cli
```

## 🔧 Verificação

```bash
# Verificar se PATH foi atualizado
echo $env:PATH

# Verificar se arquivo existe
Test-Path "D:\open-mangaba-cli\open-mangaba-cli\mangaba.bat"

# Testar execução direta
& "D:\open-mangaba-cli\open-mangaba-cli\mangaba.bat"
```

## 💡 Dicas

- **Reinicie o terminal** após alterar o PATH
- **Use aspas** se o caminho tiver espaços
- **Verifique o caminho** - substitua pelo seu caminho real
- **PowerShell vs CMD** - métodos diferentes para cada um

## 🎯 Teste Rápido

```bash
# Se nada funcionar, use sempre:
cd "D:\open-mangaba-cli\open-mangaba-cli"
.\mangaba.bat
```

---
**✨ Depois de configurar, você poderá usar `mangaba` de qualquer lugar!**