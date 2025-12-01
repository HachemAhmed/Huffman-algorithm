import heapq
import re
from collections import Counter

class HuffmanNode:
    """Representa um nó na árvore de Huffman."""
    def __init__(self, char, freq):
        self.char = char  # Palavra ou Símbolo
        self.freq = freq
        self.left = None
        self.right = None

    # Permite que o heapq compare nós pela frequência
    def __lt__(self, other):
        return self.freq < other.freq

def get_frequencies(text):
    """
    Recebe um texto e retorna um Counter com a frequência de cada token.
    Separa palavras de pontuações.
    """
    # Regex: \w+ pega palavras, [^\w\s] pega pontuações isoladas
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return Counter(tokens)

def build_huffman_tree(frequencies):
    """
    Constrói a árvore de Huffman a partir do mapa de frequências.
    Retorna o nó raiz.
    """
    priority_queue = []
    
    # 1. Cria nós folha para cada palavra
    for word, freq in frequencies.items():
        node = HuffmanNode(word, freq)
        heapq.heappush(priority_queue, node)
    
    # 2. Combina os nós até restar apenas a raiz
    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        
        sum_freq = left_node.freq + right_node.freq
        parent_node = HuffmanNode(None, sum_freq)
        
        parent_node.left = left_node
        parent_node.right = right_node
        
        heapq.heappush(priority_queue, parent_node)
    
    # Retorna a raiz (último elemento da fila) ou None se vazio
    return priority_queue[0] if priority_queue else None

def generate_codes(node, current_code="", code_map=None):
    """
    Percorre a árvore recursivamente para gerar os códigos binários.
    """
    if code_map is None:
        code_map = {}
    
    if node is None:
        return code_map

    # Se é folha (tem palavra), registra o código
    if node.char is not None:
        code_map[node.char] = current_code
        return code_map

    # Recursão: Esquerda = 0, Direita = 1
    generate_codes(node.left, current_code + "0", code_map)
    generate_codes(node.right, current_code + "1", code_map)
    
    return code_map

def compress_text(text, code_map):
    """
    Substitui as palavras do texto pelos seus códigos binários.
    """
    tokens = re.findall(r'\w+|[^\w\s]', text)
    # Junta os códigos sem espaço (padrão de compressão)
    return "".join([code_map.get(token, "") for token in tokens])

def format_tree(node, prefix="", is_left=True):
    """
    Gera uma string visual da estrutura da árvore para o relatório.
    """
    if node is None:
        return ""

    result = ""
    if node.char is not None:
        result += f"{prefix}{'|-- ' if is_left else '`-- '}[{node.char}] ({node.freq})\n"
    else:
        result += f"{prefix}{'|-- ' if is_left else '`-- '}({node.freq})\n"
        
    new_prefix = prefix + ("|   " if is_left else "    ")
    
    if node.left:
        result += format_tree(node.left, new_prefix, True)
    if node.right:
        result += format_tree(node.right, new_prefix, False)
        
    return result