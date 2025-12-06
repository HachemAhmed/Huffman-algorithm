# Huffman Algorithm (Word-Based) 📚

Este projeto implementa o **Algoritmo de Huffman** para compressão de textos, utilizando **palavras** como símbolos base, em vez de caracteres individuais. Desenvolvido como parte da avaliação prática de Estruturas de Dados no **CEFET-MG**.

## 📋 Descrição do Projeto

O objetivo deste software é ler um conjunto de textos, calcular a frequência de ocorrência de cada palavra e gerar uma árvore binária de Huffman para criar códigos binários otimizados. Palavras mais frequentes recebem códigos menores, resultando na compressão dos dados.

O programa gera um relatório completo (`output.dat`) contendo:
1. A estrutura visual da Árvore de Huffman
2. O dicionário de códigos gerados (Palavra → Binário)
3. O texto final comprimido (sequência de bits)
4. Informações suficientes para permitir a decodificação do texto original

## 🚀 Como Executar

### Pré-requisitos
* Python 3.8 ou superior
* **Sem dependências externas** - utiliza apenas bibliotecas padrão do Python (`heapq`, `re`, `collections`)
* Terminal Linux (testado em Ubuntu 24.04) ou Windows

### Passo a Passo

1.  **Clone o repositório:**
```bash
    git clone https://github.com/HachemAhmed/Huffman-algorithm.git
    cd Huffman-algorithm
```

2.  **Prepare o arquivo de entrada:**
    O arquivo `data/input.dat` já vem com exemplos de textos. Certifique-se de separar cada texto por uma **linha em branco** e salvar o arquivo em codificação **UTF-8**.

3.  **Execute o programa:**
```bash
    python3 main.py
```

4.  **Verifique o resultado:**
    O relatório será gerado automaticamente em `data/output.dat`:
```bash
    cat data/output.dat
```

## 📂 Estrutura do Projeto
```
Huffman-algorithm/
├── main.py          # Controlador principal (gerencia I/O e fluxo)
├── huffman.py       # Lógica do algoritmo (árvore e compressão)
├── data/
│   ├── input.dat    # Textos de entrada
│   └── output.dat   # Resultado da compressão (gerado automaticamente)
└── README.md
```

## 🔧 Módulos Implementados

### `main.py`
Controlador responsável por:
- Leitura do arquivo `input.dat`
- Processamento de múltiplos textos
- Geração do relatório em `output.dat`
- Tratamento de erros de encoding

### `huffman.py`
Contém a implementação completa do algoritmo:
- **`HuffmanNode`**: Classe que representa cada nó da árvore
- **`get_frequencies()`**: Calcula frequência de palavras e pontuações
- **`build_huffman_tree()`**: Constrói a árvore binária usando heap de prioridade
- **`generate_codes()`**: Gera códigos binários através de travessia recursiva
- **`compress_text()`**: Substitui palavras por códigos binários
- **`format_tree()`**: Formata a árvore em representação visual

## 📊 Exemplo de Saída
```
=== TEXTO 1 ===
TEXTO ORIGINAL: O computador executa instruções em alta velocidade...

--- 1. ESTRUTURA DA ARVORE ---
`-- (13)
    |-- (5)
    |   |-- (2)
    |   |   |-- [precisão] (1)
    |   |   `-- [alta] (1)
    ...

--- 2. DICIONARIO DE CODIGOS ---
O: 0110
computador: 1110
executa: 0111
...

--- 3. TEXTO COMPRIMIDO (BINARIO) ---
0110111001111011111100110000101010110111000001001
```

## 🎯 Características Técnicas

- **Algoritmo:** Huffman com heap de prioridade (complexidade O(n log n))
- **Símbolos:** Palavras completas em vez de caracteres individuais
- **Separação:** Regex para identificar palavras e pontuações
- **Estrutura de dados:** Árvore binária implementada com nós encadeados
- **Codificação:** 0 para ramo esquerdo, 1 para ramo direito

## ✒️ Autor

**Ahmed Hachem**  
Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG)  
Dezembro de 2025

---

### 📝 Nota sobre Compressão

Este projeto demonstra o conceito de compressão de Huffman em nível de palavras. A eficiência da compressão é mais evidente quando há palavras com frequências variadas no texto de entrada. Para textos onde cada palavra aparece apenas uma vez, todos os códigos terão comprimentos similares, o que é o comportamento esperado do algoritmo.