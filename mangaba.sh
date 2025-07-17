#!/bin/bash
# MANGABA CLI - Script Shell para Linux/Mac
# Permite executar 'mangaba' diretamente no terminal
#
# Uso:
#   ./mangaba.sh           - Exibe jornada completa
#   ./mangaba.sh --quick   - Comandos rápidos
#   ./mangaba.sh --examples - Exemplos práticos
#   ./mangaba.sh --help-debug - Ajuda de debug

# Obtém o diretório do script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Muda para o diretório do script
cd "$SCRIPT_DIR"

# Executa o script Python com todos os argumentos passados
python3 mangaba.py "$@"

# Se não há argumentos, exibe uma mensagem adicional
if [ $# -eq 0 ]; then
    echo ""
    echo "💡 Dica: Para tornar 'mangaba' disponível globalmente:"
    echo "   1. Copie este script para /usr/local/bin/mangaba"
    echo "   2. Execute: chmod +x /usr/local/bin/mangaba"
    echo "   3. Agora você pode usar 'mangaba' de qualquer lugar!"
fi