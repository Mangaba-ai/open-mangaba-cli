# MANGABA CLI

**MANGABA** é uma ferramenta CLI moderna e agnóstica a provedores para criar e gerenciar agentes de LLM com integrações poderosas.

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Versão" />
  <img src="https://img.shields.io/badge/licença-MIT-green.svg" alt="Licença" />
  <img src="https://img.shields.io/badge/python-3.8+-yellow.svg" alt="Python" />
</p>

<p align="center">
  <pre>
    <code style="color: #9370DB;">
╭─────────────────────────────────────────────────────────────────╮
│  ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  █████╗ ██████╗  █████╗  │
│  ████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗ │
│  ██╔████╔██║███████║██╔██╗ ██║██║  ███╗███████║██████╔╝███████║ │
│  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██╔══██╗██╔══██║ │
│  ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║██████╔╝██║  ██║ │
│  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ │
│                                                                 │
│  <i>Ferramenta CLI para Agentes LLM • Inspirada nas Cores Vibrantes da Mangaba</i> │
╰─────────────────────────────────────────────────────────────────╯
    </code>
</pre>
</p>

## ✨ Funcionalidades

- **Agnóstica a Provedores**: Integra-se perfeitamente com várias APIs de MPH (Google Gemini, OpenAI, etc.).
- **Agentes com Ferramentas**: Equipe agentes com ferramentas de Python, Shell, Sistema de Arquivos e Busca na Web.
- **Ferramentas de Criação de Agentes Google**: Suporte especializado para fluxos de trabalho baseados no Google.
- **CLI Intuitiva**: Construída com Click para uma experiência de linha de comando fluida e amigável.
- **Depuração Detalhada**: Logs detalhados para solução de problemas e monitoramento de atividades dos agentes.
- **Tratamento Robusto de Erros**: Validação abrangente e gerenciamento de erros para operação confiável.

## 🚀 Instalação

Comece a usar o MANGABA em poucos passos:

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/your-repo/open-mangaba-cli.git
   cd open-mangaba-cli
   ```

2. **Instalar Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verificar Instalação**:
   ```bash
   python -m src.main --help
   ```

## 🔧 Configuração

Configure suas chaves de API para desbloquear todo o potencial do MANGABA:

- **Google Gemini**:
  ```bash
  python -m src.main config set GOOGLE_API_KEY <sua_chave_api_google>
  ```

- **OpenAI**:
  ```bash
  python -m src.main config set OPENAI_API_KEY <sua_chave_api_openai>
  ```

## 🛠️ Uso

### Gerenciamento de Agentes

- **Criar um Agente**:
  ```bash
  python -m src.main agent create
  ```
  Siga as instruções para especificar o nome do agente e o provedor de MPH (ex.: `google`, `openai`).

- **Listar Agentes**:
  ```barn
  python -m src.main agent list
  ```

- **Excluir um Agente**:
  ```bash
  python -m src.main agent delete <nome_do_agente>
  ```

### Gerenciamento de Tarefas

- **Criar uma Tarefa**:
  ```bash
  python -m src.main task create
  ```
  Forneça o nome da tarefa, nome do agente e prompt durante a configuração interativa.

- **Listar Tarefas**:
  ```bash
  python -m src.main task list
  ```

- **Excluir uma Tarefa**:
  ```bash
  python -m src.main task delete <nome_da_tarefa>
  ```

### Executando Tarefas

Execute uma tarefa com:
```bash
python -m src.main run <nome_da_tarefa>
```

Para saída detalhada, use a flag `--verbose`:
```bash
python -m src.main run <nome_da_tarefa> --verbose
```

#### Exemplo: Tarefa de Busca na Web
1. Crie um agente (ex.: `meu_agente` com provedor `google`).
2. Crie uma tarefa:
   ```bash
   python -m src.main task create
   # Nome da Tarefa: ultimas_noticias_gemini
   # Nome do Agente: meu_agente
   # Prompt: Use a ferramenta web_search para encontrar as últimas notícias sobre Gemini AI e resumi-las.
   ```
3. Execute a tarefa com saída detalhada:
   ```bash
   python -m src.main run ultimas_noticias_gemini --verbose
   ```

## 🧪 Executando Testes

Execute os testes unitários para garantir que tudo está funcionando como esperado:
```bash
python -m unittest discover tests
```

## 🛡️ Solução de Problemas

### Problemas Comuns

1. **Chave de API Ausente**:
   ```
   Erro: GOOGLE_API_KEY não encontrada na configuração
   ```
   **Solução**: Configure a chave de API:
   ```bash
   python -m src.main config set GOOGLE_API_KEY <sua_chave_api_real>
   ```

2. **Erro de Importação**:
   ```
   ModuleNotFoundError: Nenhum módulo chamado 'google.generativeai'
   ```
   **Solução**: Reinstale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. **Nenhum Agente/Tarefa Encontrado**:
   ```
   Erro: Nenhum agente encontrado. Crie um agente primeiro.
   ```
   **Solução**: Crie um agente:
   ```bash
   python -m src.main agent create --name meu_agente --llm-provider google
   ```

### Depuração com Modo Detalhado
Para logs detalhados durante a solução de problemas:
```bash
python -m src.main run <nome_da_tarefa> --verbose
```

## 🌟 Status do Projeto

✅ **Funcionalidades Totalmente Implementadas**:
- Interface CLI baseada em Click
- Gerenciamento de agentes e tarefas
- **Integração com Google Gemini com chamada de função**
- **Integração com OpenAI GPT com chamada de função**
- **Sistema de ferramentas extensível (Python, Shell, FileSystem, WebSearch)**
- **Modo verbose para debugging detalhado**
- **Configuração simples via CLI**
- **Arquitetura modular e extensível**