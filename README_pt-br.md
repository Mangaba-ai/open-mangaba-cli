# MANGABA

**MANGABA** é uma ferramenta CLI para criar e gerenciar agentes de LLM com várias APIs.

## Funcionalidades

*   Agnóstico ao provedor de API de LLM.
*   Criação de agentes com ferramentas (Python, Shell, Sistema de Arquivos, Busca na Web).
*   Ferramentas de criação de agentes Google.
*   Tudo via CLI.

## Banner

```
\u001b[38;2;147;112;219m╭─────────────────────────────────────────────────────────────────╮\u001b[0m
\u001b[38;2;138;43;226m│  \u001b[1m\u001b[38;2;186;85;211m███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  █████╗ ██████╗  █████╗\u001b[0m\u001b[38;2;138;43;226m  │\u001b[0m
\u001b[38;2;138;43;226m│  \u001b[1m\u001b[38;2;147;112;219m████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗\u001b[0m\u001b[38;2;138;43;226m  │\u001b[0m
\u001b[38;2;138;43;226m│  \u001b[1m\u001b[38;2;186;85;211m██╔████╔██║███████║██╔██╗ ██║██║  ███╗███████║██████╔╝███████║\u001b[0m\u001b[38;2;138;43;226m  │\u001b[0m
\u001b[38;2;138;43;226m│  \u001b[1m\u001b[38;2;147;112;219m██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██╔══██╗██╔══██║\u001b[0m\u001b[38;2;138;43;226m  │\u001b[0m
\u001b[38;2;138;43;226m│  \u001b[1m\u001b[38;2;186;85;211m██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║██████╔╝██║  ██║\u001b[0m\u001b[38;2;138;43;226m  │\u001b[0m
\u001b[38;2;138;43;226m│  \u001b[1m\u001b[38;2;147;112;219m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝\u001b[0m\u001b[38;2;138;43;226m  │\u001b[0m
\u001b[38;2;147;112;219m│                                                                 │\u001b[0m
\u001b[38;2;147;112;219m│  \u001b[3m\u001b[38;2;221;160;221mFerramenta CLI para Agentes LLM • Inspirado nas Cores da Mangaba\u001b[0m\u001b[38;2;147;112;219m  │\u001b[0m
\u001b[38;2;147;112;219m╰─────────────────────────────────────────────────────────────────╯\u001b[0m
```

## Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/your-repo/open-mangaba-cli.git
    cd open-mangaba-cli
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Verifique a instalação:
    ```bash
    python -m src.main --help
    ```

## Configuração

Defina suas chaves de API usando o comando `config`. Para Google Gemini:

```bash
python -m src.main config set GOOGLE_API_KEY SUA_CHAVE_API_GOOGLE
```

Para OpenAI (se você planeja usá-lo):

```bash
python -m src.main config set OPENAI_API_KEY SUA_CHAVE_API_OPENAI
```

## Uso

### Gerenciamento de Agentes

*   **Criar um agente:**
    ```bash
    python -m src.main agent create
    # Siga as instruções para o nome do agente e provedor LLM (ex: google, openai)
    ```
*   **Listar agentes:**
    ```bash
    python -m src.main agent list
    ```
*   **Excluir um agente:**
    ```bash
    python -m src.main agent delete <nome_do_agente>
    ```

### Gerenciamento de Tarefas

*   **Criar uma tarefa:**
    ```bash
    python -m src.main task create
    # Siga as instruções para o nome da tarefa, nome do agente e prompt
    ```
*   **Listar tarefas:**
    ```bash
    python -m src.main task list
    ```
*   **Excluir uma tarefa:**
    ```bash
    python -m src.main task delete <nome_da_tarefa>
    ```

### Executando Tarefas

Para executar uma tarefa, use o comando `run`:

```bash
python -m src.main run <nome_da_tarefa>
```

**Saída Detalhada (Verbose):**

Para ver a atividade detalhada do agente e suas ferramentas, use a flag `--verbose`:

```bash
python -m src.main run <nome_da_tarefa> --verbose
```

**Exemplo com Ferramenta de Busca na Web (Detalhado):**

1.  Crie um agente (ex: `meu_agente` usando o provedor LLM `google`).
2.  Crie uma tarefa que use a busca na web:
    ```bash
    python -m src.main task create
    # Nome da tarefa: ultimas_noticias_gemini
    # Nome do agente: meu_agente
    # Prompt: Use a ferramenta web_search para encontrar as últimas notícias sobre Gemini AI e resuma-as.
    ```
3.  Execute a tarefa com saída detalhada:
    ```bash
    python -m src.main run ultimas_noticias_gemini --verbose
    ```

## Executando Testes

Para executar os testes de unidade, navegue até a raiz do projeto e execute:

```bash
python -m unittest discover tests
```

## Solução de Problemas

### Problemas Comuns

1.  **Chaves de API Ausentes**
    ```
    Error: GOOGLE_API_KEY not found in config
    ```
    Solução: Configure sua chave de API usando:
    ```bash
    python -m src.main config set GOOGLE_API_KEY sua_chave_api_real
    ```

2.  **Erros de Importação**
    ```
    ModuleNotFoundError: No module named 'google.generativeai'
    ```
    Solução: Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Nenhum Agente/Tarefa Encontrado**
    ```
    Error: No agents found. Create an agent first.
    ```
    Solução: Crie um agente antes de criar tarefas:
    ```bash
    python -m src.main agent create --name meu_agente --llm-provider google
    ```

### Modo Detalhado (Verbose)

Para depuração, sempre use a flag `--verbose`:
```bash
python -m src.main run minha_tarefa --verbose
```

## Status do Projeto

✅ **Funcionalidades Totalmente Implementadas:**
- Interface CLI com Click
- Gerenciamento de agentes e tarefas
- Integração Google Gemini com chamada de função
- Integração OpenAI GPT com chamada de função
- Ferramentas Python, Shell, Sistema de Arquivos e Busca na Web
- Tratamento de erros robusto e validação
- Gerenciamento de configuração
- Testes de unidade

## Compatibilidade de API

- **Google Gemini**: Usa `google-generativeai` v0.3.0+ com chamada de função
- **OpenAI**: Usa `openai` v1.0.0+ com a nova API de chat completions

## Contribuição

O projeto agora está totalmente funcional com tratamento de erros adequado, implementações de API modernas e integração abrangente de ferramentas.