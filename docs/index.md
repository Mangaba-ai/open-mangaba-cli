# Documentação do open-mangaba-cli

Bem-vindo à documentação do **open-mangaba-cli**! Este projeto visa fornecer uma ferramenta de linha de comando (CLI) flexível e poderosa para criar e gerenciar agentes de Large Language Models (LLMs) de forma agnóstica a diferentes provedores de API.

## 🚀 Jornada do Usuário - Guia Completo

### 📋 Sumário da Jornada

1.  [🎯 O que é o open-mangaba-cli?](#o-que-e)
2.  [⚡ Início Rápido (5 minutos)](#inicio-rapido)
3.  [🔧 Configuração Detalhada](#configuracao-detalhada)
4.  [👨‍💻 Seu Primeiro Agente](#primeiro-agente)
5.  [📝 Sua Primeira Tarefa](#primeira-tarefa)
6.  [🎮 Executando e Testando](#executando-testando)
7.  [🛠️ Ferramentas Avançadas](#ferramentas-avancadas)
8.  [🔍 Depuração e Solução de Problemas](#depuracao)
9.  [🚀 Casos de Uso Práticos](#casos-de-uso)
10. [🏗️ Arquitetura e Extensões](#arquitetura)
11. [🤝 Contribuição](#contribuicao)

---

## 🎯 O que é o open-mangaba-cli?

O **open-mangaba-cli** é sua ferramenta definitiva para criar **agentes de IA inteligentes** que podem:

✅ **Executar código Python** para análises e cálculos  
✅ **Navegar e manipular arquivos** no seu sistema  
✅ **Executar comandos de terminal** automaticamente  
✅ **Buscar informações na web** em tempo real  
✅ **Trabalhar com qualquer LLM** (Google Gemini, OpenAI, etc.)  

### 💡 Por que usar?

**Imagine poder dizer para seu computador:**
- "Analise este arquivo CSV e me dê um relatório"
- "Monitore as últimas notícias sobre IA e salve em um arquivo"
- "Execute meus testes e me avise se passou"
- "Baixe dados da web e processe com Python"

**E ele simplesmente faz!** 🤖

### 🌟 Diferenciais

- **🔄 Multi-LLM:** Troque entre Google Gemini, OpenAI e outros sem reescrever código
- **🛠️ Ferramentas Integradas:** Python, Shell, FileSystem e WebSearch prontos para usar
- **📱 CLI Simples:** Sem servidores complexos, apenas comandos diretos
- **🔍 Modo Debug:** Veja exatamente o que seu agente está fazendo
- **⚡ Rápido:** De zero a agente funcionando em 5 minutos

## ⚡ Início Rápido (5 minutos)

### 🎬 Demonstração Prática

Vamos criar seu primeiro agente que analisa um arquivo CSV! Siga estes passos:

#### Passo 1: Instalação Express
```bash
# Clone e instale
git clone https://github.com/your-repo/open-mangaba-cli.git
cd open-mangaba-cli
pip install -r requirements.txt

# Teste se funcionou
python -m src.main --help
```

#### Passo 2: Configure sua API (escolha uma)
```bash
# Para Google Gemini (recomendado)
python -m src.main config set GOOGLE_API_KEY sua_chave_aqui

# OU para OpenAI
python -m src.main config set OPENAI_API_KEY sua_chave_aqui
```

#### Passo 3: Crie seu primeiro agente
```bash
python -m src.main agent create
# Nome: analista
# Provedor: google (ou openai)
```

#### Passo 4: Crie um arquivo de teste
```bash
echo "nome,idade,salario\nJoão,25,5000\nMaria,30,6000\nPedro,35,7000" > dados.csv
```

#### Passo 5: Crie uma tarefa
```bash
python -m src.main task create
# Nome: analisar_dados
# Agente: analista
# Prompt: Leia o arquivo 'dados.csv', calcule a média salarial e salve o resultado em 'relatorio.txt'
```

#### Passo 6: Execute e veja a mágica! ✨
```bash
python -m src.main run analisar_dados --verbose
```

**🎉 Parabéns!** Você acabou de criar um agente que:
1. Leu um arquivo CSV
2. Processou os dados com Python
3. Calculou estatísticas
4. Salvou o resultado em um arquivo

---

## 🔧 Configuração Detalhada

### 🔑 Configuração de Chaves de API

O sistema utiliza um arquivo de configuração JSON localizado em `~/.mangaba/config.json` para armazenar as chaves das APIs de forma segura.

#### Google Gemini API (Recomendado)
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

#### Como Funciona a Configuração

**Localização do arquivo:** `~/.mangaba/config.json`

**Estrutura do arquivo:**
```json
{
  "GOOGLE_API_KEY": "sua_chave_google_aqui",
  "OPENAI_API_KEY": "sua_chave_openai_aqui"
}
```

**Validação automática:**
- ✅ O sistema verifica se a chave está configurada antes da execução
- ✅ Exibe mensagens de erro claras se a configuração estiver ausente
- ✅ Suporta múltiplos provedores simultaneamente
- ✅ Cada agente pode usar um provedor diferente

#### Detalhes Técnicos da Implementação

**Google Gemini:**
- Utiliza o SDK `google.generativeai`
- Modelo padrão: `gemini-2.5-flash`
- Configuração via `genai.configure(api_key=api_key)`
- Suporte a ferramentas via prompt enhancement

**OpenAI:**
- Utiliza o SDK oficial `openai`
- Modelo padrão: `gpt-3.5-turbo`
- Suporte nativo a function calling
- Integração avançada com ferramentas

**Fluxo de Validação:**
```python
# Exemplo do código de validação
config = load_config()
if llm_provider == 'google' and not config.get('GOOGLE_API_KEY'):
    click.echo("Error: GOOGLE_API_KEY not configured...")
elif llm_provider == 'openai' and not config.get('OPENAI_API_KEY'):
    click.echo("Error: OPENAI_API_KEY not configured...")
```

### 🔍 Verificando Configuração
```bash
# Listar todas as configurações
python -m src.main config list

# Verificar chave específica
python -m src.main config get GOOGLE_API_KEY

# Testar conexão
python -m src.main agent list
```

## 👨‍💻 Seu Primeiro Agente

### 🤖 Tipos de Agentes Recomendados

#### 📊 Agente Analista (Para dados e relatórios)
```bash
python -m src.main agent create
# Nome: analista
# Provedor: google
```
**Ideal para:** Análise de CSVs, cálculos, relatórios

#### 🌐 Agente Pesquisador (Para busca web)
```bash
python -m src.main agent create
# Nome: pesquisador
# Provedor: google
```
**Ideal para:** Buscar notícias, pesquisar informações, monitoramento

#### 🔧 Agente DevOps (Para automação)
```bash
python -m src.main agent create
# Nome: devops
# Provedor: google
```
**Ideal para:** Executar testes, deploy, monitoramento de sistema

### 📋 Comandos de Gerenciamento
```bash
# Listar agentes
python -m src.main agent list

# Deletar agente
python -m src.main agent delete nome_agente
```

---

## 📝 Sua Primeira Tarefa

### 🎯 Templates de Tarefas Prontas

#### 📈 Análise de Dados
```bash
python -m src.main task create
# Nome: analisar_vendas
# Agente: analista
# Prompt: Leia o arquivo 'vendas.csv', calcule o total de vendas por mês, identifique o mês com maior venda e salve um relatório em 'relatorio_vendas.txt' com gráfico ASCII.
```

#### 🔍 Monitoramento Web
```bash
python -m src.main task create
# Nome: noticias_ia
# Agente: pesquisador
# Prompt: Use web_search para buscar 'inteligência artificial notícias hoje'. Resuma as 3 principais notícias e salve em 'noticias_ia.md' com links.
```

#### 🧪 Automação de Testes
```bash
python -m src.main task create
# Nome: executar_testes
# Agente: devops
# Prompt: Execute 'python -m unittest discover tests' usando shell. Se os testes passarem, crie arquivo 'build_success.txt'. Se falharem, salve os erros em 'build_errors.txt'.
```

#### 🔄 Backup Inteligente
```bash
python -m src.main task create
# Nome: backup_smart
# Agente: devops
# Prompt: Liste todos os arquivos .py modificados hoje, copie para pasta 'backup/' e crie um log em 'backup_log.txt' com timestamp.
```

### 📋 Comandos de Gerenciamento
```bash
# Listar tarefas
python -m src.main task list

# Deletar tarefa
python -m src.main task delete nome_tarefa
```

---

## 🎮 Executando e Testando

### 🚀 Execução Básica
```bash
# Execução simples
python -m src.main run nome_da_tarefa

# Execução com debug (RECOMENDADO)
python -m src.main run nome_da_tarefa --verbose
```

### 🔍 Entendendo o Modo Verbose

O modo `--verbose` mostra **exatamente** o que seu agente está fazendo:

```
🤖 Agente: Vou analisar o arquivo CSV...
🛠️  Ferramenta: filesystem - Lendo arquivo 'dados.csv'
📄 Resultado: nome,idade,salario\nJoão,25,5000...
🤖 Agente: Agora vou calcular a média...
🛠️  Ferramenta: python - Executando código de análise
📊 Resultado: Média salarial: R$ 6000
🤖 Agente: Salvando relatório...
🛠️  Ferramenta: filesystem - Criando 'relatorio.txt'
✅ Tarefa concluída!
```

### 🎯 Exemplo Prático Completo

**Cenário:** Analisar dados de vendas e gerar relatório

1. **Crie dados de teste:**
```bash
echo "produto,vendas,mes\nNotebook,10,Jan\nMouse,50,Jan\nNotebook,15,Fev\nMouse,45,Fev" > vendas.csv
```

2. **Execute a análise:**
```bash
python -m src.main run analisar_vendas --verbose
```

3. **Veja os resultados:**
```bash
cat relatorio_vendas.txt
```

### ⚡ Dicas de Execução

- **Sempre use `--verbose`** na primeira execução
- **Teste com dados pequenos** primeiro
- **Verifique os arquivos gerados** após cada execução
- **Use nomes descritivos** para tarefas e agentes

## 🛠️ Ferramentas Avançadas

### 🧰 Arsenal Completo de Ferramentas

Seu agente tem acesso a 4 ferramentas poderosas que podem ser combinadas para tarefas complexas:

#### 🐍 PythonTool
**O que faz:** Executa código Python completo

**Exemplos de uso:**
- Análise de dados com pandas
- Cálculos matemáticos complexos
- Processamento de imagens
- Machine learning básico
- Gráficos e visualizações

**Prompt exemplo:**
```
"Use Python para ler o CSV, calcular estatísticas descritivas e criar um gráfico de barras ASCII"
```

#### 💻 ShellTool
**O que faz:** Executa comandos do terminal/cmd

**Exemplos de uso:**
- Executar testes automatizados
- Fazer backup de arquivos
- Monitorar processos do sistema
- Instalar dependências
- Operações Git

**Prompt exemplo:**
```
"Execute os testes com pytest e se passarem, faça commit das mudanças no Git"
```

#### 📁 FileSystemTool
**O que faz:** Manipula arquivos e pastas

**Exemplos de uso:**
- Ler/escrever arquivos de qualquer formato
- Criar estruturas de diretórios
- Fazer backup seletivo
- Organizar arquivos por data/tipo
- Gerar relatórios em múltiplos formatos

**Prompt exemplo:**
```
"Leia todos os logs de erro da pasta 'logs/', analise os padrões e crie um relatório resumido"
```

#### 🌐 WebSearchTool
**O que faz:** Busca informações na internet

**Exemplos de uso:**
- Monitorar notícias sobre tópicos específicos
- Pesquisar preços de produtos
- Verificar status de serviços online
- Coletar dados para pesquisa
- Monitorar concorrência

**Prompt exemplo:**
```
"Busque as últimas notícias sobre Python 3.12 e resuma as principais novidades"
```

### 🔗 Combinando Ferramentas

**Exemplo Avançado - Monitor de Preços:**
```bash
python -m src.main task create
# Nome: monitor_precos
# Agente: pesquisador
# Prompt: Use web_search para buscar preço do 'iPhone 15' em 3 sites diferentes. Use Python para comparar os preços e calcular a média. Salve um relatório em 'precos_iphone.json' com timestamp.
```

**Exemplo Avançado - Análise de Logs:**
```bash
python -m src.main task create
# Nome: analisar_logs
# Agente: devops
# Prompt: Leia todos os arquivos .log da pasta 'logs/', use Python para contar erros por tipo, identifique os 5 erros mais frequentes e gere um dashboard em HTML.
```

## 🏗️ Arquitetura Inteligente

### 📁 Estrutura do Projeto

```
open-mangaba-cli/
├── 🚀 main.py              # Ponto de entrada - seu comando principal
├── ⚙️ config.py            # Gerenciador de configurações e chaves API
├── 🧠 llm.py               # Interface abstrata para LLMs
├── 🔗 google.py            # Implementação Google Gemini
├── 🔗 openai.py            # Implementação OpenAI GPT
├── 🤖 agents.py            # Fábrica e gerenciamento de agentes
├── 🛠️ tools.py             # Arsenal de ferramentas dos agentes
├── 💾 data/                # Dados persistentes (agents.json, tasks.json)
└── 🧪 tests/              # Testes automatizados
```

### 🔄 Como Funciona (Fluxo Simplificado)

```
1. 👤 Você cria um AGENTE
   ↓
2. 📝 Você define uma TAREFA
   ↓
3. 🤖 O agente "pensa" sobre a tarefa
   ↓
4. 🛠️ O agente escolhe e usa FERRAMENTAS
   ↓
5. ✅ Você recebe o RESULTADO
```

### 🎭 Tipos de Agentes Recomendados

| Tipo | Especialidade | Ferramentas Preferidas |
|------|---------------|------------------------|
| 📊 **Analista** | Dados, relatórios, estatísticas | Python + FileSystem |
| 🔍 **Pesquisador** | Busca, coleta, investigação | WebSearch + FileSystem |
| ⚙️ **DevOps** | Automação, deploy, monitoramento | Shell + Python |
| 🎨 **Criativo** | Conteúdo, design, escrita | WebSearch + FileSystem |
| 🔧 **Técnico** | Desenvolvimento, debug, testes | Python + Shell |

### 🚀 Fluxo de Execução Detalhado

1. **🎯 Criação de Agente:** Você define nome, provedor LLM e especialização
2. **📝 Criação de Tarefa:** Você associa uma tarefa específica ao agente
3. **🧠 Processamento:** O agente analisa a tarefa usando o LLM
4. **🛠️ Seleção de Ferramentas:** O agente escolhe as ferramentas necessárias
5. **⚡ Execução:** As ferramentas são executadas em sequência inteligente
6. **📊 Resultado:** O resultado final é entregue e logado

## 🤝 Desenvolvimento e Contribuição

### 🚀 Como Contribuir

Contribuições são **muito bem-vindas**! Aqui está seu guia completo:

#### 🔧 Setup de Desenvolvimento
```bash
# 1. Fork e clone
git clone https://github.com/seu-usuario/open-mangaba-cli.git
cd open-mangaba-cli

# 2. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instale dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Se existir

# 4. Configure para desenvolvimento
export PYTHONPATH=$PWD/src  # Linux/Mac
# ou
set PYTHONPATH=%CD%\src     # Windows
```

#### 🌟 Fluxo de Contribuição

1. **🍴 Fork o repositório**
2. **🌿 Crie uma branch descritiva:**
   ```bash
   git checkout -b feature/nova-ferramenta-email
   # ou
   git checkout -b fix/corrige-bug-filesystem
   ```
3. **💻 Desenvolva sua funcionalidade**
4. **🧪 Escreva testes:**
   ```bash
   # Teste específico
   python -m unittest tests.test_tools.TestEmailTool
   
   # Todos os testes
   python -m unittest discover tests
   ```
5. **✅ Verifique qualidade:**
   ```bash
   # Linting (se configurado)
   flake8 src/
   
   # Formatação (se usando black)
   black src/
   ```
6. **📝 Commit com mensagem clara:**
   ```bash
   git commit -m "feat: adiciona EmailTool para envio de notificações"
   ```
7. **🚀 Push e Pull Request:**
   ```bash
   git push origin feature/nova-ferramenta-email
   ```

#### 🎯 Tipos de Contribuição Desejadas

- **🛠️ Novas Ferramentas:** EmailTool, DatabaseTool, APITool
- **🔗 Novos Provedores LLM:** Anthropic Claude, Cohere, etc.
- **📚 Documentação:** Exemplos, tutoriais, casos de uso
- **🐛 Correções de Bugs:** Sempre bem-vindas!
- **⚡ Melhorias de Performance:** Otimizações e refatorações
- **🧪 Testes:** Aumentar cobertura de testes

#### 📋 Padrões de Código

- **Nomes descritivos** para variáveis e funções
- **Docstrings** para classes e métodos públicos
- **Type hints** quando possível
- **Testes unitários** para novas funcionalidades
- **Comentários** para lógica complexa

## 🔍 Depuração e Solução de Problemas
### 🚨 Problemas Mais Comuns

#### ❌ "Chave de API não configurada"

**🔍 Diagnóstico:**
```bash
# Verifique se a chave existe
python -m src.main config get GOOGLE_API_KEY

# Se retornar vazio, configure:
python -m src.main config set GOOGLE_API_KEY SUA_CHAVE_AQUI

# Teste a conexão
python -m src.main agent create
# Nome: teste_api
# Provedor: google
```

**💡 Dica:** Mantenha suas chaves em um gerenciador de senhas!

---

#### ❌ "Agente/Tarefa não encontrado"

**🔍 Diagnóstico:**
```bash
# Liste todos os agentes
python -m src.main agent list

# Liste todas as tarefas
python -m src.main task list

# Se estiver vazio, você precisa criar primeiro!
```

**🔧 Solução Rápida:**
```bash
# Crie um agente básico
python -m src.main agent create
# Nome: assistente
# Provedor: google

# Crie uma tarefa simples
python -m src.main task create
# Nome: teste
# Agente: assistente
# Prompt: Diga olá e explique o que você pode fazer
```

---

#### ❌ "Erro de conexão com API"

**🔍 Possíveis Causas:**
- 🌐 Sem internet
- 🔑 Chave inválida/expirada
- 💰 Cota excedida
- ⏰ Timeout temporário

**🔧 Soluções:**
```bash
# 1. Teste sua conexão
ping google.com

# 2. Verifique sua chave
python -m src.main config get GOOGLE_API_KEY

# 3. Teste com tarefa simples
python -m src.main task create
# Nome: teste_conexao
# Agente: assistente
# Prompt: Responda apenas 'OK'

python -m src.main run teste_conexao --verbose
```

---

#### ❌ "Ferramenta não funciona"

**🔍 Diagnóstico com Verbose:**
```bash
# SEMPRE use --verbose para debug
python -m src.main run NOME_DA_TAREFA --verbose
```

**🛠️ Teste Individual de Ferramentas:**

**Python:**
```bash
python -m src.main task create
# Nome: teste_python
# Agente: assistente
# Prompt: Use Python para calcular 2+2 e mostrar o resultado
```

**FileSystem:**
```bash
python -m src.main task create
# Nome: teste_arquivo
# Agente: assistente
# Prompt: Crie um arquivo 'teste.txt' com o conteúdo 'Hello World'
```

**Shell:**
```bash
python -m src.main task create
# Nome: teste_shell
# Agente: assistente
# Prompt: Use shell para listar os arquivos do diretório atual
```

**WebSearch:**
```bash
python -m src.main task create
# Nome: teste_web
# Agente: assistente
# Prompt: Busque na web 'Python 3.12 novidades' e resuma em 3 linhas
```

### 🛠️ Kit de Ferramentas de Debug

#### 🔍 Comando de Diagnóstico Completo
```bash
# Crie este script para diagnóstico rápido
echo "=== DIAGNÓSTICO MANGABA ===" && \
echo "1. Configurações:" && \
python -m src.main config get GOOGLE_API_KEY && \
echo "2. Agentes:" && \
python -m src.main agent list && \
echo "3. Tarefas:" && \
python -m src.main task list && \
echo "=== FIM DIAGNÓSTICO ==="
```

#### 📊 Teste de Performance
```bash
# Crie uma tarefa de benchmark
python -m src.main task create
# Nome: benchmark
# Agente: assistente
# Prompt: Use Python para medir o tempo de execução de um loop de 1000 iterações que calcula números primos até 100

# Execute com verbose para ver timing
python -m src.main run benchmark --verbose
```

### 🆘 Quando Pedir Ajuda

Se ainda estiver com problemas, abra uma **issue** no GitHub com:

1. **🖥️ Sistema operacional** (Windows/Linux/Mac)
2. **🐍 Versão do Python** (`python --version`)
3. **📋 Comando exato** que você executou
4. **❌ Mensagem de erro completa**
5. **📝 Output do modo verbose** (`--verbose`)
6. **⚙️ Suas configurações** (sem expor chaves!):
   ```bash
   python -m src.main config get GOOGLE_API_KEY | head -c 10
   ```

### 💡 Dicas de Ouro

- ✅ **Sempre comece simples** - teste com tarefas básicas primeiro
- 🔍 **Use --verbose** - é seu melhor amigo para debug
- 📝 **Nomes descritivos** - facilita identificar problemas
- 🔄 **Teste incremental** - adicione complexidade aos poucos
- 💾 **Backup das configurações** - salve seus agentes e tarefas importantes

## 8. Casos de Uso Avançados

Esta seção apresenta exemplos de como o **open-mangaba-cli** pode ser utilizado para automatizar tarefas complexas, combinando as capacidades dos agentes LLM com as ferramentas disponíveis. Esses cenários demonstram o poder da orquestração de ferramentas para resolver problemas do mundo real.

### Caso de Uso 1: Análise de Dados e Geração de Relatórios

**Cenário:** Você precisa analisar um arquivo CSV local, extrair informações específicas (e.g., média, soma de uma coluna) e gerar um relatório em um novo arquivo de texto.

**Como o Agente Atua:**
1.  O agente usa a `FileSystemTool` para ler o conteúdo do arquivo CSV.
2.  Em seguida, ele utiliza a `PythonTool` para processar os dados lidos (e.g., carregar com `pandas`, realizar cálculos estatísticos).
3.  Finalmente, o agente usa a `FileSystemTool` novamente para escrever os resultados da análise em um novo arquivo de relatório.

**Exemplo de Prompt para a Tarefa:**
```
Leia o arquivo 'dados.csv', calcule a média da coluna 'valor' e salve o resultado em 'relatorio.txt'.
```

**Passos para Configurar (Exemplo):**
1.  Crie um arquivo `dados.csv` na raiz do projeto com algum conteúdo, por exemplo:
    ```csv
    item,valor
    A,10
    B,20
    C,30
    ```
2.  Crie um agente (e.g., `analista_dados` com provedor `google`).
3.  Crie uma tarefa:
    ```bash
    python -m src.main task create
    # Nome da tarefa: analisar_relatorio
    # Agente: analista_dados
    # Prompt: Leia o arquivo 'dados.csv', calcule a média da coluna 'valor' usando Python e salve o resultado formatado em 'relatorio.txt'.
    ```
4.  Execute a tarefa (com `--verbose` para ver os detalhes):
    ```bash
    python -m src.main run analisar_relatorio --verbose
    ```

### Caso de Uso 2: Monitoramento de Conteúdo Web e Notificações

**Cenário:** Você deseja monitorar uma página web para novas informações (e.g., notícias, atualizações de produtos) e ser notificado quando houver mudanças significativas.

**Como o Agente Atua:**
1.  O agente usa a `WebSearchTool` para buscar informações ou a `ShellTool` (com `curl` ou `wget`) para baixar o conteúdo de uma URL específica.
2.  Ele pode usar a `FileSystemTool` para salvar o conteúdo baixado e compará-lo com uma versão anterior.
3.  Se uma mudança for detectada, o agente pode usar a `PythonTool` para simular o envio de uma notificação (e.g., imprimir uma mensagem de alerta, ou em uma implementação real, integrar com um serviço de notificação).

**Exemplo de Prompt para a Tarefa:**
```
Verifique as últimas notícias sobre 'inteligência artificial' na web. Se houver algo novo e relevante, registre no arquivo 'novas_noticias.txt'.
```

**Passos para Configurar (Exemplo):**
1.  Crie um agente (e.g., `monitor_web` com provedor `google`).
2.  Crie uma tarefa:
    ```bash
    python -m src.main task create
    # Nome da tarefa: monitorar_ia
    # Agente: monitor_web
    # Prompt: Use a web_search tool para buscar por 'inteligência artificial últimas notícias'. Se encontrar algo relevante, escreva os 3 primeiros links no arquivo 'novas_noticias.txt'.
    ```
3.  Execute a tarefa:
    ```bash
    python -m src.main run monitorar_ia --verbose
    ```

### Caso de Uso 3: Automação de Tarefas de Desenvolvimento (CI/CD Simplificado)

**Cenário:** Um desenvolvedor quer automatizar um fluxo de trabalho simples de CI/CD, onde o agente verifica o status de um repositório, executa testes e, se tudo estiver ok, simula um deploy.

**Como o Agente Atua:**
1.  O agente usa a `ShellTool` para executar comandos Git (e.g., `git status`, `git pull`).
2.  Ele pode usar a `ShellTool` para executar comandos de teste (e.g., `pytest`, `npm test`).
3.  Se os testes passarem, ele pode usar a `ShellTool` para simular um comando de deploy ou a `FileSystemTool` para atualizar um arquivo de status de deploy.

**Exemplo de Prompt para a Tarefa:**
```
Verifique o status do repositório Git, execute os testes Python e, se passarem, crie um arquivo 'deploy_ok.txt'.
```

**Passos para Configurar (Exemplo):**
1.  Crie um agente (e.g., `dev_ops_bot` com provedor `google`).
2.  Crie uma tarefa:
    ```bash
    python -m src.main task create
    # Nome da tarefa: automacao_ci
    # Agente: dev_ops_bot
    # Prompt: Use a shell tool para executar 'git status'. Em seguida, use a shell tool para executar 'python -m unittest discover tests'. Se o comando de teste retornar sucesso, use a filesystem tool para criar um arquivo chamado 'deploy_ok.txt' com o conteúdo 'Deploy bem-sucedido!'.
    ```
3.  Execute a tarefa:
    ```bash
    python -m src.main run automacao_ci --verbose
    ```

Estes exemplos ilustram como a combinação inteligente das ferramentas e a capacidade de raciocínio do LLM podem transformar o **open-mangaba-cli** em uma poderosa plataforma de automação e assistência inteligente.

## 9. Diferenciais para Outros Frameworks CLI de Agentes

O **open-mangaba-cli** se destaca no cenário de frameworks CLI de agentes por algumas características fundamentais que o tornam uma escolha poderosa e flexível para desenvolvedores:

### 1. Agnosticismo de Provedor de LLM

Enquanto muitos frameworks são construídos em torno de um provedor de LLM específico (e.g., OpenAI, Anthropic), o **open-mangaba-cli** foi projetado desde o início para ser **agnóstico**. Isso significa:

*   **Flexibilidade:** Você pode facilmente alternar entre diferentes modelos e provedores de LLM (Google Gemini, OpenAI GPT, etc.) configurando apenas uma chave de API, sem a necessidade de reescrever a lógica do seu agente.
*   **Resistência ao Futuro:** À medida que novos e melhores LLMs surgem, o `open-mangaba-cli` permite que você os integre rapidamente, protegendo seu investimento em lógica de agente.
*   **Otimização de Custos:** Permite que você escolha o provedor de LLM mais custo-efetivo ou com melhor desempenho para cada tarefa específica.

### 2. Abordagem CLI-First e Simplicidade

Ao contrário de frameworks mais complexos que podem exigir a configuração de servidores web, APIs REST ou interfaces gráficas, o `open-mangaba-cli` foca em uma experiência **CLI-first**:

*   **Leveza:** Não há sobrecarga de dependências desnecessárias ou infraestrutura complexa. É ideal para automação de scripts, tarefas de desenvolvimento e integração em fluxos de trabalho existentes.
*   **Fácil de Usar:** A interação é direta via linha de comando, tornando-o acessível para desenvolvedores que preferem um ambiente de terminal.
*   **Rápida Prototipagem:** Permite que você crie e teste agentes rapidamente, sem a curva de aprendizado associada a ecossistemas maiores.

### 3. Extensibilidade e Modularidade de Ferramentas

O design do `open-mangaba-cli` enfatiza a facilidade de adicionar novas ferramentas e estender as existentes:

*   **Ferramentas Integradas Essenciais:** Já vem com ferramentas prontas para uso (Python, Shell, FileSystem, WebSearch) que cobrem uma ampla gama de necessidades de automação.
*   **Criação de Ferramentas Personalizadas:** A arquitetura modular facilita a criação de ferramentas personalizadas para interagir com sistemas internos, APIs proprietárias ou qualquer recurso externo que seu agente precise acessar.
*   **Transparência:** O modo verbose (`--verbose`) oferece uma visibilidade sem precedentes sobre como o agente está utilizando cada ferramenta, o que é crucial para depuração e compreensão do comportamento do LLM.

### 4. Foco em Casos de Uso Práticos

Os exemplos e a estrutura do `open-mangaba-cli` são orientados para a resolução de problemas práticos e a automação de tarefas do dia a dia de desenvolvedores e usuários avançados:

*   **Automação de Fluxos de Trabalho:** Desde a análise de dados e geração de relatórios até o monitoramento web e automação de CI/CD simplificada, o framework é construído para ser uma ferramenta de automação inteligente.
*   **Assistente Pessoal Programável:** Pode ser adaptado para funcionar como um assistente pessoal que entende comandos em linguagem natural e executa ações no seu sistema.

Em resumo, o **open-mangaba-cli** oferece uma alternativa ágil e poderosa para quem busca construir agentes inteligentes com foco em flexibilidade, simplicidade e controle direto via linha de comando, sem se prender a um único provedor de LLM ou a uma infraestrutura complexa.