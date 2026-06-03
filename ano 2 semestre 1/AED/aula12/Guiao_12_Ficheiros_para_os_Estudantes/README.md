# Travessias em Grafos - Guião 12

## Resumo das Implementações

Este guião implementa e compara três algoritmos de travessia de grafos:

1. **DFS Recursivo** (GraphDFSRec) - Travessia em profundidade recursiva
2. **DFS Iterativo** (GraphDFSWithStack) - Travessia em profundidade com pilha
3. **BFS** (GraphBFSWithQueue) - Travessia por níveis com fila

---

## 📁 Arquivos Principais

### Módulos de Travessia

- **GraphDFSRec.c/.h** - DFS recursivo (completo)
- **GraphDFSWithStack.c/.h** - DFS iterativo com pilha (✅ completado)
- **GraphBFSWithQueue.c/.h** - BFS com fila (✅ completado)

### Programas de Teste e Exemplos

- **test_traversals.c** - Compara as três travessias lado a lado
- **exemplo_aplicacao1.c** - Identifica vértices alcançáveis usando DFS
- **exemplo_aplicacao2.c** - Lista caminhos mais curtos usando BFS

---

## 🔍 Análise dos Algoritmos

### 1. DFS Recursivo (GraphDFSRec)

**Funcionamento:**
- Usa a pilha de chamadas recursivas
- Marca vértices como visitados
- Armazena o predecessor de cada vértice

**Ordem de visita:**
```
Função _dfs(vertex):
  1. Marca vertex como visitado
  2. Para cada adjacente w de vertex (na ordem do array):
     - Se w não foi visitado:
       - predecessor[w] = vertex
       - _dfs(w) [chamada recursiva]
```

### 2. DFS Iterativo com Pilha (GraphDFSWithStack)

**Implementação:**
```c
Stack* stack = StackCreate(numVertices);
StackPush(stack, startVertex);
marked[startVertex] = 1;

while (!StackIsEmpty(stack)) {
  vertex = StackPop(stack);
  
  // Para cada adjacente (em ordem REVERSA para igualar DFS recursivo)
  for (i = neighbors[0]; i >= 1; i--) {
    w = neighbors[i];
    if (!marked[w]) {
      marked[w] = 1;
      predecessor[w] = vertex;
      StackPush(stack, w);
    }
  }
}
```

**⚠️ Observação Importante:**
- Para que a ordem de visita seja igual ao DFS recursivo, é necessário **empilhar os adjacentes em ordem reversa**
- Se empilharmos na ordem direta (i = 1 até neighbors[0]), a ordem de visita será diferente

### 3. BFS com Fila (GraphBFSWithQueue)

**Implementação:**
```c
Queue* queue = QueueCreate(numVertices);
QueueEnqueue(queue, startVertex);
marked[startVertex] = 1;
distance[startVertex] = 0;

while (!QueueIsEmpty(queue)) {
  vertex = QueueDequeue(queue);
  
  // Para cada adjacente (ordem natural)
  for (i = 1; i <= neighbors[0]; i++) {
    w = neighbors[i];
    if (!marked[w]) {
      marked[w] = 1;
      distance[w] = distance[vertex] + 1;
      predecessor[w] = vertex;
      QueueEnqueue(queue, w);
    }
  }
}
```

**Propriedades do BFS:**
- Visita vértices por **níveis** (distância crescente)
- Array `distance[]` armazena o **número de arestas** no caminho mais curto
- Garante encontrar o **caminho mais curto** em grafos não ponderados

---

## 📊 Comparação: Ordem de Visita

### Quando DFS Recursivo e DFS Iterativo têm a MESMA ordem?

✅ **São IGUAIS quando:**
- Os adjacentes são empilhados em **ordem REVERSA** no DFS iterativo
- Isso simula o comportamento da pilha de recursão

### Quando têm ordem DIFERENTE?

❌ **São DIFERENTES quando:**
- Os adjacentes são empilhados em ordem direta
- O último adjacente do array será visitado primeiro (comportamento LIFO da pilha)

### Exemplo Visual

Grafo:
```
    0
   / \
  1   2
```

**DFS Recursivo:** 0 → 1 → 2
- Visita adjacente 1 primeiro (primeiro no array)
- Depois visita adjacente 2

**DFS Iterativo (ordem reversa):** 0 → 1 → 2 ✅ IGUAL
- Empilha: 2, depois 1
- Desempilha: 1 (visitado primeiro), depois 2

**DFS Iterativo (ordem direta):** 0 → 2 → 1 ❌ DIFERENTE
- Empilha: 1, depois 2
- Desempilha: 2 (visitado primeiro), depois 1

---

## 🎯 Estruturas de Dados

### Comum a todas as travessias:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `marked[]` | `unsigned int*` | 1 se vértice foi visitado, 0 caso contrário |
| `predecessor[]` | `int*` | Predecessor do vértice na árvore de travessia (-1 se nenhum) |
| `graph` | `Graph*` | Referência para o grafo |
| `startVertex` | `unsigned int` | Vértice inicial da travessia |

### Específico do BFS:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `distance[]` | `int*` | Número de arestas no caminho mais curto (-1 se inalcançável) |

---

## 🚀 Compilação e Execução

### Compilar todos os programas:
```bash
make clean
make
```

### Executar comparação das travessias:
```bash
./test_traversals
```

### Executar exemplo 1 (vértices alcançáveis):
```bash
./exemplo_aplicacao1
```

### Executar exemplo 2 (caminhos mais curtos):
```bash
./exemplo_aplicacao2
```

---

## 📚 Aplicações Práticas

### DFS (Depth-First Search)

✅ **Melhor para:**
- Detectar ciclos em grafos
- Ordenação topológica
- Encontrar componentes fortemente conexas
- Resolver puzzles e labirintos (exploração completa)
- Análise de dependências

### BFS (Breadth-First Search)

✅ **Melhor para:**
- **Caminhos mais curtos** em grafos não ponderados
- Calcular distâncias mínimas
- Análise de redes sociais (graus de separação)
- Roteamento de redes (menor número de saltos)
- Encontrar o caminho mais próximo

---

## 🔑 Conceitos Importantes

### Árvore de Caminhos (Paths Tree)

- Construída usando o array `predecessor[]`
- Representa os caminhos da travessia
- Pode ser visualizada em formato DOT com `DisplayDOT()`

### Distância em Grafos Não Ponderados

- **Distância** = número de arestas no caminho
- BFS garante encontrar a **menor distância**
- Array `distance[]` armazena essas distâncias

### Vértices Alcançáveis

- Um vértice é **alcançável** se `marked[v] == 1`
- Em grafos desconexos, nem todos os vértices são alcançáveis
- Útil para análise de conectividade

---

## ⚙️ Complexidade

Todas as travessias têm complexidade:

- **Tempo:** O(V + E)
  - V = número de vértices
  - E = número de arestas
  
- **Espaço:** O(V)
  - Arrays: marked, predecessor, distance
  - Stack/Queue: no máximo V elementos

---

## 📝 Notas de Implementação

### Memória

- Sempre liberar a memória com `Destroy()` após uso
- BFS: não esquecer de liberar `distance[]`

### Grafos Direcionados vs Não Direcionados

- A alcançabilidade depende da direção das arestas
- Em grafos direcionados, A→B não implica B→A

### Valores Especiais

- `predecessor[v] = -1` → sem predecessor (vértice inicial ou inalcançável)
- `distance[v] = -1` → vértice inalcançável (apenas BFS)
- `marked[v] = 0` → vértice não visitado

---

## 🎓 Exercícios Sugeridos

1. Modificar DFS iterativo para empilhar em ordem direta e comparar resultados
2. Implementar função para contar componentes conexas
3. Encontrar o diâmetro de um grafo (maior distância entre quaisquer dois vértices)
4. Implementar detecção de ciclos usando DFS
5. Criar função que retorna todos os vértices a uma distância específica (usando BFS)

---

## 📖 Referências

- Algoritmos e Estruturas de Dados (AED) - Universidade de Aveiro
- Sedgewick & Wayne - "Algorithms", 4th Edition
- Cormen et al. - "Introduction to Algorithms"
