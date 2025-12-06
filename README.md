# Huffman Algorithm (Word-Based) 📚

Este projeto implementa o **Algoritmo de Huffman** para compressão de textos, utilizando **palavras** como símbolos base, em vez de caracteres individuais. Desenvolvido como parte da avaliação prática de Estruturas de Dados no **CEFET-MG**.

## 🎓 Contexto Acadêmico

**Disciplina:** Estruturas de Dados  
**Professor:** Michel Pires  
**Instituição:** Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG)  
**Data de Entrega:** 06/12/2025

## 📋 Descrição do Projeto

O objetivo deste software é ler um conjunto de textos, calcular a frequência de ocorrência de cada palavra e gerar uma árvore binária de Huffman para criar códigos binários otimizados. Palavras mais frequentes recebem códigos menores, resultando na compressão dos dados.

O programa gera um relatório completo (`output.dat`) contendo:
1. A estrutura visual da Árvore de Huffman
2. O dicionário de códigos gerados (Palavra → Binário)
3. O texto final comprimido (sequência de bits)

## 🚀 Como Executar

### Pré-requisitos
* Python 3.8 ou superior
* **Sem dependências externas** - utiliza apenas bibliotecas padrão
* Terminal Linux (testado em Ubuntu 24.04) ou Windows

### Passo a Passo

1.  **Clone o repositório:**
```bash
    git clone https://github.com/HachemAhmed/Huffman-algorithm.git
    cd Huffman-algorithm
```

2.  **Prepare o arquivo de entrada:**
    O arquivo `data/input.dat` já vem com exemplos. Certifique-se de separar cada texto por uma **linha em branco** e salvar em **UTF-8**.

3.  **Execute o programa:**
```bash
    python3 main.py
```

4.  **Verifique o resultado:**
    O relatório será gerado em `data/output.dat`:
```bash
    cat data/output.dat
```

## 📂 Estrutura do Projeto
```
Huffman-algorithm/
├── main.py          # Controlador principal (gerencia I/O)
├── huffman.py       # Lógica do algoritmo (árvore e compressão)
├── data/
│   ├── input.dat    # Textos de entrada
│   └── output.dat   # Resultado da compressão (gerado)
└── README.md
```

## 🔧 Módulos

* **`main.py`**: Controlador que gerencia leitura/escrita de arquivos e fluxo de execução
* **`huffman.py`**: Contém a classe `HuffmanNode` e algoritmos de:
  - Cálculo de frequências
  - Construção da árvore binária
  - Geração de códigos
  - Compressão de texto

## ✒️ Autor

**Ahmed Hachem**  
Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG)
