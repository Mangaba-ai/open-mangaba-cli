# 🥭 Guia Completo do Banner MANGABA

## 🎨 Como Exibir o Banner MANGABA

### 1. 📋 Método Mais Simples

**Execute o script dedicado:**
```bash
python show_banner.py
```

### 2. 🐍 No Seu Código Python

```python
# Importar as funções
from show_banner import show_mangaba_banner, show_simple_banner, check_color_support

# Exibir banner com detecção automática de cores
if check_color_support():
    show_mangaba_banner()  # Banner colorido
else:
    show_simple_banner()   # Banner sem cores
```

### 3. 💻 Diretamente no Terminal

**Banner colorido (copie e cole):**
```bash
echo -e "\033[38;2;147;112;219m╭─────────────────────────────────────────────────────────────────╮\033[0m"
echo -e "\033[38;2;138;43;226m│  \033[1m\033[38;2;186;85;211m███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  █████╗ ██████╗  █████╗\033[0m\033[38;2;138;43;226m  │\033[0m"
echo -e "\033[38;2;138;43;226m│  \033[1m\033[38;2;147;112;219m████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗\033[0m\033[38;2;138;43;226m  │\033[0m"
echo -e "\033[38;2;138;43;226m│  \033[1m\033[38;2;186;85;211m██╔████╔██║███████║██╔██╗ ██║██║  ███╗███████║██████╔╝███████║\033[0m\033[38;2;138;43;226m  │\033[0m"
echo -e "\033[38;2;138;43;226m│  \033[1m\033[38;2;147;112;219m██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██╔══██╗██╔══██║\033[0m\033[38;2;138;43;226m  │\033[0m"
echo -e "\033[38;2;138;43;226m│  \033[1m\033[38;2;186;85;211m██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║██████╔╝██║  ██║\033[0m\033[38;2;138;43;226m  │\033[0m"
echo -e "\033[38;2;138;43;226m│  \033[1m\033[38;2;147;112;219m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝\033[0m\033[38;2;138;43;226m  │\033[0m"
echo -e "\033[38;2;147;112;219m│                                                                 │\033[0m"
echo -e "\033[38;2;147;112;219m│  \033[3m\033[38;2;221;160;221mCLI Tool for LLM Agents • Inspired by Mangaba Fruit Colors\033[0m\033[38;2;147;112;219m     │\033[0m"
echo -e "\033[38;2;147;112;219m╰─────────────────────────────────────────────────────────────────╯\033[0m"
```

**Banner simples (sem cores):**
```
╭─────────────────────────────────────────────────────────────────╮
│  ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  █████╗ ██████╗  █████╗  │
│  ████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗  │
│  ██╔████╔██║███████║██╔██╗ ██║██║  ███╗███████║██████╔╝███████║  │
│  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██╔══██╗██╔══██║  │
│  ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║██████╔╝██║  ██║  │
│  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝  │
│                                                                 │
│     CLI Tool for LLM Agents • Inspired by Mangaba Fruit Colors  │
╰─────────────────────────────────────────────────────────────────╯
```

### 4. 📄 No README ou Documentação

O banner já está incluído nos arquivos:
- `README.md` (linha 15)
- `README_pt-br.md` (linha 15)

### 5. 🎯 Integração no CLI Principal

**Para adicionar o banner ao comando principal:**

```python
# No arquivo src/main.py, adicione:
from show_banner import show_mangaba_banner, check_color_support

@click.group()
def cli():
    """MANGABA CLI - LLM Agent Management Tool"""
    if check_color_support():
        show_mangaba_banner()
    else:
        click.echo("MANGABA CLI - LLM Agent Management Tool")
```

## 🎨 Detalhes das Cores

### 🇧🇷 Paleta de Cores da Bandeira do Brasil

| Cor | RGB | Hex | Uso |
|-----|-----|-----|-----|
| Verde | `0,151,57` | `#009739` | Borda e estrutura |
| Amarelo | `254,221,0` | `#FEDD00` | Texto MANGABA (linhas ímpares) |
| Azul | `1,33,105` | `#012169` | Texto MANGABA (linhas pares) |
| Branco | `255,255,255` | `#FFFFFF` | Descrição e contraste |

### 🔧 Códigos ANSI Utilizados

- `\033[38;2;R;G;Bm` - Cor RGB do texto
- `\033[1m` - Texto em negrito
- `\033[3m` - Texto em itálico
- `\033[0m` - Reset das formatações

## 🖥️ Compatibilidade de Terminais

### ✅ Terminais com Suporte Completo
- Windows Terminal
- PowerShell 7+
- Git Bash
- WSL
- Terminal do VS Code
- iTerm2 (Mac)
- GNOME Terminal (Linux)

### ⚠️ Terminais com Suporte Limitado
- CMD tradicional do Windows
- PowerShell 5.1 (sem colorama)
- Alguns terminais antigos

### 🔧 Para Habilitar Cores no Windows

**Instale colorama (opcional):**
```bash
pip install colorama
```

**Ou use Windows Terminal moderno:**
- Baixe da Microsoft Store
- Configure como terminal padrão

## 🚀 Exemplos de Uso

### 📱 Script de Boas-vindas

```python
#!/usr/bin/env python3
from show_banner import show_mangaba_banner

def welcome():
    show_mangaba_banner()
    print("\n🎉 Bem-vindo ao MANGABA CLI!")
    print("\n🚀 Comandos disponíveis:")
    print("   • python -m src.main agent create")
    print("   • python -m src.main task create")
    print("   • python -m src.main run <task_name>")
    print("\n📚 Para ajuda: python -m src.main --help")

if __name__ == "__main__":
    welcome()
```

### 🎨 Banner Personalizado

```python
def show_custom_banner(message="CLI Tool for LLM Agents"):
    """Exibe banner com mensagem personalizada"""
    # ... código do banner ...
    # Substitua a linha da mensagem por:
    print(f"\033[38;2;147;112;219m│  \033[3m\033[38;2;221;160;221m{message.center(63)}\033[0m\033[38;2;147;112;219m     │\033[0m")
```

## 🔍 Troubleshooting

### ❌ Banner não aparece colorido

**Solução 1 - Verificar suporte:**
```python
from show_banner import check_color_support
print(f"Suporte a cores: {check_color_support()}")
```

**Solução 2 - Forçar cores:**
```bash
# Linux/Mac
export FORCE_COLOR=1

# Windows
set FORCE_COLOR=1
```

**Solução 3 - Usar banner simples:**
```python
from show_banner import show_simple_banner
show_simple_banner()
```

### ❌ Caracteres estranhos no terminal

**Causa:** Terminal não suporta Unicode

**Solução:** Use versão ASCII:
```
+---------------------------------------------------------------+
|  M   M   A   A  N   N  G   G   A   A  B   B   A   A         |
|  MM MM  A   A  NN  N  G       A   A  B   B  A   A         |
|  M M M  AAAAA  N N N  G  GG   AAAAA  BBBB   AAAAA         |
|  M   M  A   A  N  NN  G   G   A   A  B   B  A   A         |
|  M   M  A   A  N   N   GGG    A   A  BBBB   A   A         |
|                                                           |
|           CLI Tool for LLM Agents                         |
+---------------------------------------------------------------+
```

## 📝 Notas Importantes

- 🎨 O banner usa cores inspiradas na fruta mangaba (roxo/violeta)
- 🔧 Detecção automática de suporte a cores
- 📱 Responsivo para diferentes larguras de terminal
- 🌍 Compatível com Windows, Linux e macOS
- ⚡ Performance otimizada para carregamento rápido

---

**💡 Dica:** Para usar o banner em seus próprios projetos, copie o arquivo `show_banner.py` e importe as funções necessárias!