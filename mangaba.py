#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MANGABA CLI - Script Principal Executável

Este script permite executar 'mangaba' diretamente no terminal e exibe:
- Banner colorido MANGABA
- Jornada completa do usuário
- Guia de primeiros passos
- Comandos principais

Uso:
    python mangaba.py
    ou
    mangaba (após configurar como executável)
"""

import sys
import os
import click
from pathlib import Path

# Adiciona o diretório src ao path para importar módulos
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

try:
    from show_banner import show_mangaba_banner, show_simple_banner, check_color_support
except ImportError:
    # Fallback se show_banner não estiver disponível
    def show_mangaba_banner():
        # Banner com cores da bandeira do Brasil distribuídas por letra (fallback)
        # Padrão de cores para MANGABA: M=verde, A=amarelo, N=azul, G=branco, A=verde, B=amarelo, A=azul
        banner = """
\033[38;2;0;151;57m╭─────────────────────────────────────────────────────────────────────────────╮\033[0m
\033[38;2;0;151;57m│  \033[1m\033[38;2;0;151;57m███╗   ███╗\033[38;2;254;221;0m █████╗ \033[38;2;1;33;105m███╗   ██╗\033[38;2;255;255;255m ██████╗ \033[38;2;0;151;57m █████╗\033[38;2;254;221;0m ██████╗ \033[38;2;1;33;105m █████╗\033[0m\033[38;2;0;151;57m    🇧🇷 │\033[0m
\033[38;2;0;151;57m│  \033[1m\033[38;2;0;151;57m████╗ ████║\033[38;2;254;221;0m██╔══██╗\033[38;2;1;33;105m████╗  ██║\033[38;2;255;255;255m██╔════╝\033[38;2;0;151;57m ██╔══██╗\033[38;2;254;221;0m██╔══██╗\033[38;2;1;33;105m██╔══██╗\033[0m\033[38;2;0;151;57m     │\033[0m
\033[38;2;0;151;57m│  \033[1m\033[38;2;0;151;57m██╔████╔██║\033[38;2;254;221;0m███████║\033[38;2;1;33;105m██╔██╗ ██║\033[38;2;255;255;255m██║  ███╗\033[38;2;0;151;57m███████║\033[38;2;254;221;0m██████╔╝\033[38;2;1;33;105m███████║\033[0m\033[38;2;0;151;57m     │\033[0m
\033[38;2;0;151;57m│  \033[1m\033[38;2;0;151;57m██║╚██╔╝██║\033[38;2;254;221;0m██╔══██║\033[38;2;1;33;105m██║╚██╗██║\033[38;2;255;255;255m██║   ██║\033[38;2;0;151;57m██╔══██║\033[38;2;254;221;0m██╔══██╗\033[38;2;1;33;105m██╔══██║\033[0m\033[38;2;0;151;57m     │\033[0m
\033[38;2;0;151;57m│  \033[1m\033[38;2;0;151;57m██║ ╚═╝ ██║\033[38;2;254;221;0m██║  ██║\033[38;2;1;33;105m██║ ╚████║\033[38;2;255;255;255m╚██████╔╝\033[38;2;0;151;57m██║  ██║\033[38;2;254;221;0m██████╔╝\033[38;2;1;33;105m██║  ██║\033[0m\033[38;2;0;151;57m     │\033[0m
\033[38;2;0;151;57m│  \033[1m\033[38;2;0;151;57m╚═╝     ╚═╝\033[38;2;254;221;0m╚═╝  ╚═╝\033[38;2;1;33;105m╚═╝  ╚═══╝\033[38;2;255;255;255m ╚═════╝\033[38;2;0;151;57m ╚═╝  ╚═╝\033[38;2;254;221;0m╚═════╝\033[38;2;1;33;105m ╚═╝  ╚═╝\033[0m\033[38;2;0;151;57m     │\033[0m
\033[38;2;0;151;57m│                                                                           │\033[0m
\033[38;2;0;151;57m│  \033[3m\033[38;2;255;255;255mCLI Tool for LLM Agents • Cores da Bandeira do Brasil\033[0m\033[38;2;0;151;57m               │\033[0m
\033[38;2;0;151;57m╰─────────────────────────────────────────────────────────────────────────────╯\033[0m
"""
        print(banner)
    
    def show_simple_banner():
        print("\n🥭 MANGABA CLI - LLM Agent Management Tool\n")
    
    def check_color_support():
        return False


def display_banner():
    """Exibe o banner MANGABA com detecção automática de cores."""
    if check_color_support():
        show_mangaba_banner()
    else:
        show_simple_banner()


def display_user_journey():
    """Exibe a jornada completa do usuário."""
    click.echo("\n🎯 BEM-VINDO AO MANGABA CLI!")
    click.echo("\n📖 JORNADA DO USUÁRIO - PASSO A PASSO")
    click.echo("=" * 50)
    
    # Passo 1: Configuração Inicial
    click.echo("\n🔧 PASSO 1: CONFIGURAÇÃO INICIAL")
    click.echo("   ┌─ Configure sua chave de API:")
    click.echo("   │   python -m src.main config set GOOGLE_API_KEY <sua_chave>")
    click.echo("   │")
    click.echo("   └─ Verifique a configuração:")
    click.echo("       python -m src.main config get GOOGLE_API_KEY")
    
    # Passo 2: Primeiro Agente
    click.echo("\n🤖 PASSO 2: CRIE SEU PRIMEIRO AGENTE")
    click.echo("   ┌─ Comando:")
    click.echo("   │   python -m src.main agent create")
    click.echo("   │")
    click.echo("   ├─ Exemplo de configuração:")
    click.echo("   │   Nome: assistente")
    click.echo("   │   Provedor: google")
    click.echo("   │   Prompt: Você é um assistente útil e preciso")
    click.echo("   │")
    click.echo("   └─ Verifique agentes criados:")
    click.echo("       python -m src.main agent list")
    
    # Passo 3: Primeira Tarefa
    click.echo("\n📝 PASSO 3: CRIE SUA PRIMEIRA TAREFA")
    click.echo("   ┌─ Comando:")
    click.echo("   │   python -m src.main task create")
    click.echo("   │")
    click.echo("   ├─ Exemplo de tarefa simples:")
    click.echo("   │   Nome: ola_mundo")
    click.echo("   │   Agente: assistente")
    click.echo("   │   Prompt: Diga olá e explique o que você pode fazer")
    click.echo("   │")
    click.echo("   └─ Verifique tarefas criadas:")
    click.echo("       python -m src.main task list")
    
    # Passo 4: Primeira Execução
    click.echo("\n🚀 PASSO 4: EXECUTE SUA PRIMEIRA TAREFA")
    click.echo("   ┌─ Execução básica:")
    click.echo("   │   python -m src.main run ola_mundo")
    click.echo("   │")
    click.echo("   └─ Execução com detalhes (recomendado):")
    click.echo("       python -m src.main run ola_mundo --verbose")
    
    # Passo 5: Tarefas Avançadas
    click.echo("\n⚡ PASSO 5: EXPLORE TAREFAS AVANÇADAS")
    click.echo("   ┌─ Análise de dados:")
    click.echo("   │   Prompt: Use Python para ler 'dados.csv' e criar estatísticas")
    click.echo("   │")
    click.echo("   ├─ Pesquisa web:")
    click.echo("   │   Prompt: Busque notícias sobre IA e resuma em 3 pontos")
    click.echo("   │")
    click.echo("   ├─ Automação de arquivos:")
    click.echo("   │   Prompt: Organize arquivos da pasta Downloads por tipo")
    click.echo("   │")
    click.echo("   └─ Comandos do sistema:")
    click.echo("       Prompt: Use shell para fazer backup da pasta projetos")


def display_quick_commands():
    """Exibe comandos rápidos e úteis."""
    click.echo("\n⚡ COMANDOS RÁPIDOS")
    click.echo("=" * 20)
    
    click.echo("\n📋 GERENCIAMENTO:")
    click.echo("   • python -m src.main agent list     - Listar agentes")
    click.echo("   • python -m src.main task list      - Listar tarefas")
    click.echo("   • python -m src.main config get     - Ver configurações")
    
    click.echo("\n🗑️ LIMPEZA:")
    click.echo("   • python -m src.main agent delete <nome>  - Deletar agente")
    click.echo("   • python -m src.main task delete <nome>   - Deletar tarefa")
    
    click.echo("\n🔧 DEPURAÇÃO:")
    click.echo("   • python -m src.main run <tarefa> --verbose  - Modo detalhado")
    click.echo("   • python mangaba.py                         - Exibir este guia")


def display_examples():
    """Exibe exemplos práticos de uso."""
    click.echo("\n💡 EXEMPLOS PRÁTICOS")
    click.echo("=" * 22)
    
    click.echo("\n📊 ANÁLISE DE DADOS:")
    click.echo("   Tarefa: analisar_vendas")
    click.echo("   Prompt: Use Python para ler 'vendas.csv', calcular total por mês")
    click.echo("           e criar um gráfico de barras ASCII")
    
    click.echo("\n🌐 PESQUISA WEB:")
    click.echo("   Tarefa: noticias_tech")
    click.echo("   Prompt: Busque as 5 principais notícias de tecnologia hoje")
    click.echo("           e resuma cada uma em 2 linhas")
    
    click.echo("\n📁 ORGANIZAÇÃO:")
    click.echo("   Tarefa: organizar_downloads")
    click.echo("   Prompt: Analise a pasta Downloads, crie subpastas por tipo")
    click.echo("           (imagens, documentos, videos) e organize os arquivos")
    
    click.echo("\n🔄 AUTOMAÇÃO:")
    click.echo("   Tarefa: backup_projeto")
    click.echo("   Prompt: Use shell para criar backup compactado da pasta")
    click.echo("           'meu_projeto' com timestamp no nome")


def display_troubleshooting():
    """Exibe dicas de solução de problemas."""
    click.echo("\n🔍 SOLUÇÃO DE PROBLEMAS")
    click.echo("=" * 25)
    
    click.echo("\n❌ Erro: 'Chave de API não configurada'")
    click.echo("   🔧 Solução: python -m src.main config set GOOGLE_API_KEY <chave>")
    
    click.echo("\n❌ Erro: 'Agente não encontrado'")
    click.echo("   🔧 Solução: python -m src.main agent list")
    click.echo("              python -m src.main agent create")
    
    click.echo("\n❌ Erro: 'Tarefa não encontrada'")
    click.echo("   🔧 Solução: python -m src.main task list")
    click.echo("              python -m src.main task create")
    
    click.echo("\n❌ Erro de conexão")
    click.echo("   🔧 Soluções: 1. Verifique internet")
    click.echo("               2. Verifique chave de API")
    click.echo("               3. Tente novamente em alguns minutos")
    
    click.echo("\n💡 DICA: Sempre use --verbose para debug detalhado!")


def display_footer():
    """Exibe rodapé com informações adicionais."""
    click.echo("\n" + "=" * 60)
    click.echo("📚 DOCUMENTAÇÃO COMPLETA: docs/index.md")
    click.echo("🎨 GUIA DO BANNER: BANNER_GUIDE.md")
    click.echo("💻 EXEMPLOS DE CÓDIGO: example_integration.py")
    click.echo("\n🌟 MANGABA CLI - Transforme ideias em ação com IA!")
    click.echo("=" * 60)


@click.command()
@click.option('--no-banner', is_flag=True, help='Não exibir banner')
@click.option('--quick', is_flag=True, help='Exibir apenas comandos rápidos')
@click.option('--examples', is_flag=True, help='Exibir apenas exemplos')
@click.option('--help-debug', is_flag=True, help='Exibir apenas ajuda de debug')
def main(no_banner, quick, examples, help_debug):
    """MANGABA CLI - Ferramenta de Gerenciamento de Agentes LLM.
    
    Execute este comando para ver a jornada completa do usuário,
    incluindo configuração, criação de agentes, tarefas e exemplos práticos.
    """
    
    # Exibe banner (a menos que seja suprimido)
    if not no_banner:
        display_banner()
    
    # Modos específicos
    if quick:
        display_quick_commands()
        return
    
    if examples:
        display_examples()
        return
    
    if help_debug:
        display_troubleshooting()
        return
    
    # Jornada completa (padrão)
    display_user_journey()
    display_quick_commands()
    display_examples()
    display_troubleshooting()
    display_footer()


if __name__ == '__main__':
    main()