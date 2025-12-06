import os
import huffman 

# Configurações de Arquivo
# Pega o diretório onde este arquivo (main.py) está: .../Huffman-algorithm/src
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Sobe um nível para achar a raiz do projeto: .../Huffman-algorithm
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# Monta o caminho para a pasta data independente de onde o terminal esteja
INPUT_FILE = os.path.join(PROJECT_ROOT, 'data', 'input.dat')
OUTPUT_FILE = os.path.join(PROJECT_ROOT, 'data', 'output.dat')
def process_texts():
    # 1. Verificação de Segurança
    if not os.path.exists(INPUT_FILE):
        print(f"Erro Crítico: Arquivo de entrada '{INPUT_FILE}' não encontrado.")
        return

    # 2. Leitura
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print("Erro de Encoding: Tente salvar o input.dat como UTF-8.")
        return

    raw_texts = content.split('\n\n')
    texts = [t.strip() for t in raw_texts if t.strip()]

    print(f"--- Iniciando Processamento de {len(texts)} textos ---")

    # 3. Processamento e Escrita
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        for i, text in enumerate(texts):
            print(f"Processando texto {i+1}...")

            # --- FLUXO DO ALGORITMO (Chamando o módulo) ---
            freqs = huffman.get_frequencies(text)
            root = huffman.build_huffman_tree(freqs)
            codes = huffman.generate_codes(root)
            compressed_bin = huffman.compress_text(text, codes)
            tree_view = huffman.format_tree(root, "", False)
            
            # --- GERAÇÃO DO RELATÓRIO ---
            header = f"=== TEXTO {i+1} ==="
            out.write(f"{header}\n")
            out.write(f"TEXTO ORIGINAL: {text}\n\n")
            
            out.write("--- 1. ESTRUTURA DA ARVORE ---\n")
            out.write(tree_view)
            out.write("\n")
            
            out.write("--- 2. DICIONARIO DE CODIGOS ---\n")
            for word, code in codes.items():
                out.write(f"{word}: {code}\n")
            out.write("\n")
            
            out.write("--- 3. TEXTO COMPRIMIDO (BINARIO) ---\n")
            out.write(f"{compressed_bin}\n")
            out.write("\n" + "="*40 + "\n\n")
    
    print(f"\nSucesso! Resultado salvo em: {os.path.abspath(OUTPUT_FILE)}")

if __name__ == "__main__":
    process_texts()