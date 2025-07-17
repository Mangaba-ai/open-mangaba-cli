#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para exibir o banner MANGABA colorido no terminal.

Uso:
    python show_banner.py
"""

def show_mangaba_banner():
    """
    Exibe o banner MANGABA com cores da bandeira do Brasil (verde, amarelo, azul, branco).
    """
    # Cores da bandeira do Brasil:
    # Verde: #009739 (0, 151, 57)
    # Amarelo: #FEDD00 (254, 221, 0) 
    # Azul: #012169 (1, 33, 105)
    # Branco: #FFFFFF (255, 255, 255)
    
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
    """
    Exibe uma versão simplificada do banner sem cores (para terminais que não suportam cores).
    """
    simple_banner = """
╭─────────────────────────────────────────────────────────────────────────────╮
│  ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  █████╗ ██████╗  █████╗    🇧🇷 │
│  ████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗     │
│  ██╔████╔██║███████║██╔██╗ ██║██║  ███╗███████║██████╔╝███████║     │
│  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██╔══██╗██╔══██║     │
│  ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║██████╔╝██║  ██║     │
│  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝     │
│                                                                           │
│       CLI Tool for LLM Agents • Cores da Bandeira do Brasil               │
╰─────────────────────────────────────────────────────────────────────────────╯
"""
    print(simple_banner)

def check_color_support():
    """
    Verifica se o terminal suporta cores ANSI.
    """
    import os
    import sys
    
    # Verifica se está rodando no Windows
    if os.name == 'nt':
        # No Windows, tenta habilitar suporte a cores ANSI
        try:
            import colorama
            colorama.init()
            return True
        except ImportError:
            # Se colorama não estiver disponível, verifica se o terminal suporta cores
            return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    
    # Em sistemas Unix-like, verifica se é um terminal interativo
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

def main():
    """
    Função principal que exibe o banner apropriado.
    """
    print("\n🥭 MANGABA CLI - Banner Display\n")
    
    if check_color_support():
        print("✅ Terminal suporta cores - Exibindo banner colorido:")
        print()
        show_mangaba_banner()
    else:
        print("⚠️  Terminal não suporta cores - Exibindo banner simples:")
        print()
        show_simple_banner()
    
    print("\n💡 Dicas:")
    print("   • Para usar no seu código: from show_banner import show_mangaba_banner")
    print("   • Para terminal sem cores: from show_banner import show_simple_banner")
    print("   • Para verificar suporte: from show_banner import check_color_support")
    print()
    print("🚀 Para começar a usar o MANGABA CLI:")
    print("   python -m src.main --help")
    print()

if __name__ == "__main__":
    main()