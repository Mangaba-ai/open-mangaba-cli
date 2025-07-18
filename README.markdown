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
   git clone https://github.com/Mangaba-ai/open-mangaba-cli.git
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

### Configuração das APIs

O sistema utiliza um arquivo de configuração JSON localizado em `~/.mangaba/config.json` para armazenar as chaves das APIs de forma segura.

#### Google Gemini API
1. **Obter a chave:** Acesse [Google AI Studio](https://makersuite.google.com/app/apikey) e crie uma nova chave de API
2. **Configurar no sistema:**
```bash
python -m src.main config set GOOGLE_API_KEY sua_chave_aqui
```
3. **Verificar configuração:**
```bash
python -m src.main config get GOOGLE_API_KEY
```

#### OpenAI API
1. **Obter a chave:** Acesse [OpenAI API Keys](https://platform.openai.com/api-keys) e crie uma nova chave de API
2. **Configurar no sistema:**
```bash
python -m src.main config set OPENAI_API_KEY sua_chave_aqui
```
3. **Verificar configuração:**
```bash
python -m src.main config get OPENAI_API_KEY
```

#### Validação Automática
O sistema valida automaticamente as chaves de API antes da execução das tarefas:
- ✅ Verifica se a chave está configurada para o provedor selecionado
- ✅ Exibe mensagens de erro claras se a configuração estiver ausente
- ✅ Suporta múltiplos provedores simultaneamente

#### Estrutura do Arquivo de Configuração
O arquivo `~/.mangaba/config.json` terá o formato:
```json
{
  "GOOGLE_API_KEY": "sua_chave_google_aqui",
  "OPENAI_API_KEY": "sua_chave_openai_aqui"
}
```

### ✅ Verificando Configuração
```bash
# Verificar se a chave foi configurada
python -m src.main config get GOOGLE_API_KEY

# Listar todas as configurações
python -m src.main config list
```

## 🛠️ Uso

### Gerenciamento de Agentes

- **Criar um Agente**:
  ```bash
  python -m src.main agent create
  ```
  Siga as instruções para especificar o nome do agente e o provedor de MPH (ex.: `google`, `openai`).

- **Listar Agentes**:
  ```bash
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