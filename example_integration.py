#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de como integrar o banner MANGABA no CLI principal.

Este arquivo demonstra diferentes formas de usar o banner:
1. Como comando separado
2. Integrado ao CLI principal
3. Como função de boas-vindas
4. Em scripts de inicialização
"""

import click
from show_banner import show_mangaba_banner, show_simple_banner, check_color_support


# ============================================================================
# 1. COMANDO SEPARADO PARA EXIBIR BANNER
# ============================================================================

@click.command()
@click.option('--simple', is_flag=True, help='Exibir banner simples sem cores')
@click.option('--force-color', is_flag=True, help='Forçar exibição com cores')
def banner(simple, force_color):
    """Exibe o banner MANGABA."""
    if simple:
        show_simple_banner()
    elif force_color or check_color_support():
        show_mangaba_banner()
    else:
        show_simple_banner()


# ============================================================================
# 2. CLI PRINCIPAL COM BANNER INTEGRADO
# ============================================================================

@click.group(invoke_without_command=True)
@click.option('--no-banner', is_flag=True, help='Não exibir banner')
@click.pass_context
def cli(ctx, no_banner):
    """MANGABA CLI - Ferramenta de Gerenciamento de Agentes LLM."""
    
    # Se nenhum subcomando foi fornecido, exibe ajuda com banner
    if ctx.invoked_subcommand is None:
        if not no_banner:
            if check_color_support():
                show_mangaba_banner()
            else:
                show_simple_banner()
            
            click.echo("\n🎉 Bem-vindo ao MANGABA CLI!")
            click.echo("\n🚀 Comandos principais:")
            click.echo("   • mangaba agent create    - Criar novo agente")
            click.echo("   • mangaba task create     - Criar nova tarefa")
            click.echo("   • mangaba run <task>      - Executar tarefa")
            click.echo("   • mangaba banner          - Exibir banner")
            click.echo("\n📚 Para ajuda detalhada: mangaba --help")
            click.echo("\n💡 Dica: Use --no-banner para pular o banner")
        else:
            click.echo(ctx.get_help())


# ============================================================================
# 3. SUBCOMANDOS DE EXEMPLO
# ============================================================================

@cli.command()
@click.option('--name', prompt='Nome do agente', help='Nome do agente')
@click.option('--provider', prompt='Provedor LLM', 
              type=click.Choice(['google', 'openai']), help='Provedor de LLM')
def agent_create(name, provider):
    """Criar um novo agente."""
    click.echo(f"\n🤖 Criando agente '{name}' com provedor '{provider}'...")
    # Aqui seria a lógica real de criação
    click.echo("✅ Agente criado com sucesso!")


@cli.command()
@click.option('--name', prompt='Nome da tarefa', help='Nome da tarefa')
@click.option('--agent', prompt='Nome do agente', help='Agente responsável')
@click.option('--prompt', prompt='Prompt da tarefa', help='Descrição da tarefa')
def task_create(name, agent, prompt):
    """Criar uma nova tarefa."""
    click.echo(f"\n📝 Criando tarefa '{name}' para agente '{agent}'...")
    click.echo(f"📋 Prompt: {prompt}")
    # Aqui seria a lógica real de criação
    click.echo("✅ Tarefa criada com sucesso!")


@cli.command()
@click.argument('task_name')
@click.option('--verbose', is_flag=True, help='Modo verboso')
def run(task_name, verbose):
    """Executar uma tarefa."""
    click.echo(f"\n🚀 Executando tarefa '{task_name}'...")
    if verbose:
        click.echo("🔍 Modo verboso ativado")
    # Aqui seria a lógica real de execução
    click.echo("✅ Tarefa executada com sucesso!")


# Adiciona o comando banner ao grupo
cli.add_command(banner)


# ============================================================================
# 4. FUNÇÕES UTILITÁRIAS
# ============================================================================

def welcome_message():
    """Exibe mensagem de boas-vindas com banner."""
    if check_color_support():
        show_mangaba_banner()
    else:
        show_simple_banner()
    
    click.echo("\n🎯 MANGABA CLI está pronto para uso!")
    click.echo("\n📖 Guia rápido:")
    click.echo("   1. Configure sua API key: mangaba config set GOOGLE_API_KEY <key>")
    click.echo("   2. Crie um agente: mangaba agent create")
    click.echo("   3. Crie uma tarefa: mangaba task create")
    click.echo("   4. Execute a tarefa: mangaba run <nome_da_tarefa>")
    click.echo("\n🔗 Documentação completa: docs/index.md")


def startup_banner():
    """Banner para scripts de inicialização."""
    if check_color_support():
        show_mangaba_banner()
    else:
        show_simple_banner()
    
    click.echo("\n⚡ Inicializando MANGABA CLI...")
    click.echo("🔧 Verificando configurações...")
    click.echo("📦 Carregando ferramentas...")
    click.echo("✅ Sistema pronto!")


# ============================================================================
# 5. EXEMPLOS DE USO EM DIFERENTES CONTEXTOS
# ============================================================================

def example_error_with_banner():
    """Exemplo de como usar banner em mensagens de erro."""
    try:
        # Simula um erro
        raise ValueError("Chave de API não configurada")
    except ValueError as e:
        if check_color_support():
            show_mangaba_banner()
        
        click.echo(f"\n❌ Erro: {e}")
        click.echo("\n🔧 Solução:")
        click.echo("   mangaba config set GOOGLE_API_KEY <sua_chave>")
        click.echo("\n📚 Ajuda: mangaba --help")


def example_success_with_banner():
    """Exemplo de como usar banner em mensagens de sucesso."""
    if check_color_support():
        show_mangaba_banner()
    
    click.echo("\n🎉 Operação concluída com sucesso!")
    click.echo("\n📊 Resultados:")
    click.echo("   • Agentes criados: 3")
    click.echo("   • Tarefas executadas: 5")
    click.echo("   • Tempo total: 2.5s")


# ============================================================================
# 6. CONFIGURAÇÕES AVANÇADAS
# ============================================================================

class BannerConfig:
    """Configurações para exibição do banner."""
    
    def __init__(self):
        self.show_banner = True
        self.force_color = False
        self.simple_mode = False
    
    def display(self):
        """Exibe o banner baseado nas configurações."""
        if not self.show_banner:
            return
        
        if self.simple_mode:
            show_simple_banner()
        elif self.force_color or check_color_support():
            show_mangaba_banner()
        else:
            show_simple_banner()


# ============================================================================
# MAIN - DEMONSTRAÇÃO
# ============================================================================

if __name__ == '__main__':
    # Demonstra diferentes usos do banner
    
    click.echo("=" * 70)
    click.echo("🎨 DEMONSTRAÇÃO DO BANNER MANGABA")
    click.echo("=" * 70)
    
    click.echo("\n1. Banner padrão:")
    if check_color_support():
        show_mangaba_banner()
    else:
        show_simple_banner()
    
    click.echo("\n2. Mensagem de boas-vindas:")
    welcome_message()
    
    click.echo("\n3. Para usar o CLI completo, execute:")
    click.echo("   python example_integration.py --help")
    
    click.echo("\n4. Exemplos de comandos:")
    click.echo("   python example_integration.py banner")
    click.echo("   python example_integration.py banner --simple")
    click.echo("   python example_integration.py agent-create")
    click.echo("   python example_integration.py task-create")
    click.echo("   python example_integration.py run minha_tarefa")
    
    click.echo("\n" + "=" * 70)