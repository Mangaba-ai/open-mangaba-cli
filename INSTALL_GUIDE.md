# 🚀 Guia de Instalação Global - Comando MANGABA

Este guia mostra como configurar o comando `mangaba` para funcionar diretamente no terminal, exibindo o banner colorido e a jornada completa do usuário.

## ⚡ Solução Rápida

**Se o comando `mangaba` não funcionar, use sempre:**
```bash
# No diretório do projeto
.\mangaba.bat          # Windows
./mangaba.sh           # Linux/Mac
python mangaba.py      # Qualquer sistema
```

📄 **Para mais soluções:** Veja <mcfile name="QUICK_FIX.md" path="d:\open-mangaba-cli\open-mangaba-cli\QUICK_FIX.md"></mcfile>

## 🪟 Windows

### Método 1: Script Batch Global (Recomendado)
1. **Copie o arquivo `mangaba.bat` para uma pasta no PATH:**
   ```cmd
   # Opção A: Pasta do sistema (requer admin)
   copy mangaba.bat C:\Windows\System32\
   
   # Opção B: Pasta do usuário
   copy mangaba.bat %USERPROFILE%\bin\
   ```

2. **Se usar pasta personalizada, adicione ao PATH:**
   ```cmd
   # Temporário (sessão atual)
   set PATH=%PATH%;%USERPROFILE%\bin
   
   # Permanente
   setx PATH "%PATH%;%USERPROFILE%\bin"
   ```

### Método 2: Alias no PowerShell
1. **Abra o perfil do PowerShell:**
   ```powershell
   # Verificar se existe
   Test-Path $PROFILE
   
   # Criar se não existir
   New-Item -ItemType File -Path $PROFILE -Force
   
   # Editar
   notepad $PROFILE
   ```

2. **Adicione a função (substitua o caminho):**
   ```powershell
   function mangaba { 
       python "D:\open-mangaba-cli\open-mangaba-cli\mangaba.py" $args 
   }
   ```

3. **Recarregue o perfil:**
   ```powershell
   . $PROFILE
   ```

### Método 3: Doskey (CMD)
1. **Crie um arquivo `autorun.cmd`:**
   ```cmd
   @echo off
   doskey mangaba=python "D:\open-mangaba-cli\open-mangaba-cli\mangaba.py" $*
   ```

2. **Configure execução automática via registro:**
   ```cmd
   reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /t REG_SZ /d "C:\caminho\para\autorun.cmd"
   ```

## 🐧 Linux / 🍎 macOS

### Método 1: Instalação Global (Recomendado)

1. **Torne o script executável:**
   ```bash
   chmod +x mangaba.sh
   ```

2. **Copie para diretório global:**
   ```bash
   sudo cp mangaba.sh /usr/local/bin/mangaba
   ```

3. **Teste a instalação:**
   ```bash
   mangaba
   ```

### Método 2: Usando Alias

1. **Adicione ao seu shell profile (~/.bashrc, ~/.zshrc, etc.):**
   ```bash
   alias mangaba='python3 /caminho/para/open-mangaba-cli/mangaba.py'
   ```

2. **Recarregue o profile:**
   ```bash
   source ~/.bashrc  # ou ~/.zshrc
   ```

### Método 3: Link Simbólico

```bash
sudo ln -s /caminho/para/open-mangaba-cli/mangaba.sh /usr/local/bin/mangaba
```

## 🎯 Comandos Disponíveis

Após a instalação, você pode usar:

```bash
# Jornada completa do usuário (padrão)
mangaba

# Apenas comandos rápidos
mangaba --quick

# Apenas exemplos práticos
mangaba --examples

# Apenas ajuda de debug
mangaba --help-debug

# Sem banner
mangaba --no-banner

# Ajuda completa
mangaba --help
```

## 🔧 Verificação da Instalação

### Teste Básico
```bash
mangaba --quick
```

### Teste com Banner
```bash
mangaba --no-banner
```

### Teste de Cores
```bash
mangaba
```

## 🎨 Personalização

### Modificar o Banner
Edite o arquivo `show_banner.py` para personalizar as cores ou o design.

### Adicionar Comandos Personalizados
Edite o arquivo `mangaba.py` para adicionar novas opções ou funcionalidades.

### Configurar Alias Personalizados
```bash
# Exemplos de aliases úteis
alias m='mangaba --quick'
alias mex='mangaba --examples'
alias mdebug='mangaba --help-debug'
```

## 🐛 Solução de Problemas

### ❌ "Comando não encontrado"

**Windows:**
- Verifique se o diretório está no PATH
- Use o caminho completo: `d:\open-mangaba-cli\open-mangaba-cli\mangaba.bat`

**Linux/Mac:**
- Verifique permissões: `chmod +x mangaba.sh`
- Verifique se está em `/usr/local/bin/`
- Use o caminho completo: `./mangaba.sh`

### ❌ "Python não encontrado"

**Solução:**
- Instale Python 3.7+
- Verifique se está no PATH: `python --version`
- No Linux/Mac, use `python3` em vez de `python`

### ❌ "Módulo não encontrado"

**Solução:**
```bash
# Instale dependências
pip install -r requirements.txt

# Ou instale manualmente
pip install click colorama
```

### ❌ "Banner sem cores"

**Soluções:**
1. **Use terminal moderno** (Windows Terminal, iTerm2, etc.)
2. **Instale colorama:**
   ```bash
   pip install colorama
   ```
3. **Force cores:**
   ```bash
   export FORCE_COLOR=1  # Linux/Mac
   set FORCE_COLOR=1     # Windows
   ```

## 📁 Estrutura de Arquivos

Após a instalação, você terá:

```
open-mangaba-cli/
├── mangaba.py          # Script principal
├── mangaba.bat         # Script Windows
├── mangaba.sh          # Script Linux/Mac
├── show_banner.py      # Funções do banner
├── INSTALL_GUIDE.md    # Este guia
└── src/                # Código fonte do CLI
```

## 🌟 Recursos Incluídos

### 🎨 Banner Colorido
- Cores da fruta mangaba (roxo/violeta)
- Detecção automática de suporte a cores
- Fallback para terminais simples

### 📖 Jornada do Usuário
- Guia passo a passo completo
- Configuração inicial
- Criação de agentes e tarefas
- Exemplos práticos
- Solução de problemas

### ⚡ Comandos Rápidos
- Lista de comandos essenciais
- Atalhos para operações comuns
- Dicas de depuração

### 💡 Exemplos Práticos
- Análise de dados
- Pesquisa web
- Organização de arquivos
- Automação de tarefas

## 🚀 Próximos Passos

1. **Execute o comando:**
   ```bash
   mangaba
   ```

2. **Configure sua API key:**
   ```bash
   python -m src.main config set GOOGLE_API_KEY <sua_chave>
   ```

3. **Crie seu primeiro agente:**
   ```bash
   python -m src.main agent create
   ```

4. **Explore os exemplos:**
   ```bash
   mangaba --examples
   ```

---

**🎉 Parabéns! O comando 'mangaba' está configurado e pronto para uso!**

Para suporte adicional, consulte:
- 📚 `docs/index.md` - Documentação completa
- 🎨 `BANNER_GUIDE.md` - Guia do banner
- 💻 `example_integration.py` - Exemplos de código