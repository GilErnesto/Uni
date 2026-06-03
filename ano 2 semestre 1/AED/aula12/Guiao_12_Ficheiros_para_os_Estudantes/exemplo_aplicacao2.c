//
// Exemplo 2: Listar caminhos mais curtos usando BFS
// 
// Este programa demonstra como usar a travessia por níveis (BFS)
// para encontrar e listar os caminhos mais curtos a partir de um vértice inicial
//

#include <stdio.h>
#include <stdlib.h>

#include "Graph.h"
#include "GraphBFSWithQueue.h"
#include "IntegersStack.h"

void printShortestPaths(Graph* g, unsigned int startVertex) {
  printf("========================================\n");
  printf("CAMINHOS MAIS CURTOS A PARTIR DO VÉRTICE %u\n", startVertex);
  printf("========================================\n\n");
  
  // Executar BFS a partir do vértice inicial
  GraphBFSWithQueue* bfs = GraphBFSWithQueueExecute(g, startVertex);
  
  unsigned int numVertices = GraphGetNumVertices(g);
  
  printf("%-10s | %-10s | %-30s\n", "Destino", "Distância", "Caminho Mais Curto");
  printf("-----------|------------|--------------------------------\n");
  
  for (unsigned int v = 0; v < numVertices; v++) {
    if (GraphBFSWithQueueHasPathTo(bfs, v)) {
      // Obter o caminho
      Stack* path = GraphBFSWithQueuePathTo(bfs, v);
      
      // Calcular distância (número de arestas)
      int pathLength = StackSize(path) - 1;  // -1 porque não contamos o vértice inicial
      
      printf("%-10u | %-10d | ", v, pathLength);
      
      // Imprimir o caminho
      int first = 1;
      while (!StackIsEmpty(path)) {
        if (!first) printf(" → ");
        printf("%u", StackPop(path));
        first = 0;
      }
      printf("\n");
      
      StackDestroy(&path);
    } else {
      printf("%-10u | %-10s | %s\n", v, "∞", "SEM CAMINHO");
    }
  }
  
  printf("\n");
  
  // Estatísticas
  printf("Estatísticas:\n");
  printf("-------------\n");
  
  // Contar vértices por distância
  int maxDistance = 0;
  int reachableCount = 0;
  
  for (unsigned int v = 0; v < numVertices; v++) {
    if (GraphBFSWithQueueHasPathTo(bfs, v)) {
      reachableCount++;
      Stack* path = GraphBFSWithQueuePathTo(bfs, v);
      int dist = StackSize(path) - 1;
      if (dist > maxDistance) maxDistance = dist;
      StackDestroy(&path);
    }
  }
  
  printf("  - Vértices alcançáveis: %d de %u\n", reachableCount, numVertices);
  printf("  - Distância máxima (diâmetro): %d arestas\n", maxDistance);
  
  // Contar por nível
  printf("\n  Distribuição por distância:\n");
  for (int d = 0; d <= maxDistance; d++) {
    int count = 0;
    printf("    Distância %d: ", d);
    
    for (unsigned int v = 0; v < numVertices; v++) {
      if (GraphBFSWithQueueHasPathTo(bfs, v)) {
        Stack* path = GraphBFSWithQueuePathTo(bfs, v);
        int dist = StackSize(path) - 1;
        if (dist == d) {
          if (count > 0) printf(", ");
          printf("%u", v);
          count++;
        }
        StackDestroy(&path);
      }
    }
    
    if (count > 0) {
      printf(" (%d vértice%s)\n", count, count > 1 ? "s" : "");
    }
  }
  
  printf("\n");
  
  // Limpar memória
  GraphBFSWithQueueDestroy(&bfs);
}

int main(void) {
  printf("╔════════════════════════════════════════════╗\n");
  printf("║  EXEMPLO 2: CAMINHOS MAIS CURTOS (BFS)    ║\n");
  printf("╚════════════════════════════════════════════╝\n\n");
  
  // ==========================================
  // Exemplo 2.1: Grafo Simples
  // ==========================================
  printf("CASO 1: Grafo Simples\n");
  printf("---------------------\n\n");
  
  Graph* g1 = GraphCreate(7, 0, 0);
  
  // Criar um grafo em forma de árvore
  GraphAddEdge(g1, 0, 1);
  GraphAddEdge(g1, 0, 2);
  GraphAddEdge(g1, 1, 3);
  GraphAddEdge(g1, 1, 4);
  GraphAddEdge(g1, 2, 5);
  GraphAddEdge(g1, 2, 6);
  
  printf("Estrutura do grafo (árvore):\n");
  printf("        0\n");
  printf("       / \\\n");
  printf("      1   2\n");
  printf("     / \\ / \\\n");
  printf("    3  4 5  6\n\n");
  
  printShortestPaths(g1, 0);
  
  GraphDestroy(&g1);
  
  // ==========================================
  // Exemplo 2.2: Grafo com Múltiplos Caminhos
  // ==========================================
  printf("\n");
  printf("CASO 2: Grafo com Múltiplos Caminhos\n");
  printf("-------------------------------------\n");
  printf("BFS encontra o caminho com menos arestas\n\n");
  
  Graph* g2 = GraphCreate(6, 0, 0);
  
  // Criar um grafo com múltiplos caminhos entre vértices
  GraphAddEdge(g2, 0, 1);
  GraphAddEdge(g2, 0, 2);
  GraphAddEdge(g2, 1, 3);
  GraphAddEdge(g2, 2, 3);
  GraphAddEdge(g2, 3, 4);
  GraphAddEdge(g2, 4, 5);
  GraphAddEdge(g2, 0, 5);  // Caminho direto!
  
  printf("Estrutura do grafo:\n");
  printf("    0 ----------- 5\n");
  printf("   / \\            |\n");
  printf("  1   2           4\n");
  printf("   \\ /            |\n");
  printf("    3 ----------- /\n\n");
  
  printf("Existem vários caminhos de 0 para 5:\n");
  printf("  - 0 → 5 (1 aresta) ← CAMINHO MAIS CURTO\n");
  printf("  - 0 → 1 → 3 → 4 → 5 (4 arestas)\n");
  printf("  - 0 → 2 → 3 → 4 → 5 (4 arestas)\n\n");
  
  printShortestPaths(g2, 0);
  
  printf("Observação: BFS garante encontrar o caminho com menor\n");
  printf("número de arestas (distância = 1 para o vértice 5).\n\n");
  
  GraphDestroy(&g2);
  
  // ==========================================
  // Exemplo 2.3: Grafo de Rede Social
  // ==========================================
  printf("\n");
  printf("CASO 3: Rede Social (graus de separação)\n");
  printf("-----------------------------------------\n\n");
  
  Graph* g3 = GraphCreate(8, 0, 0);
  
  // Simular uma rede social
  // Pessoa 0: Alice
  GraphAddEdge(g3, 0, 1);  // Alice conhece Bob
  GraphAddEdge(g3, 0, 2);  // Alice conhece Carol
  
  // Pessoa 1: Bob
  GraphAddEdge(g3, 1, 3);  // Bob conhece David
  GraphAddEdge(g3, 1, 4);  // Bob conhece Eve
  
  // Pessoa 2: Carol
  GraphAddEdge(g3, 2, 5);  // Carol conhece Frank
  
  // Pessoa 3: David
  GraphAddEdge(g3, 3, 6);  // David conhece Grace
  
  // Pessoa 5: Frank
  GraphAddEdge(g3, 5, 7);  // Frank conhece Henry
  
  printf("Estrutura da rede social:\n");
  printf("  Alice (0) é amiga de Bob (1) e Carol (2)\n");
  printf("  Bob (1) é amigo de David (3) e Eve (4)\n");
  printf("  Carol (2) é amiga de Frank (5)\n");
  printf("  David (3) é amigo de Grace (6)\n");
  printf("  Frank (5) é amigo de Henry (7)\n\n");
  
  printf("Graus de separação a partir de Alice (vértice 0):\n\n");
  
  printShortestPaths(g3, 0);
  
  printf("Interpretação:\n");
  printf("  - Distância 0: a própria Alice\n");
  printf("  - Distância 1: amigos diretos de Alice\n");
  printf("  - Distância 2: amigos de amigos de Alice\n");
  printf("  - Distância 3: amigos de amigos de amigos\n\n");
  
  GraphDestroy(&g3);
  
  // ==========================================
  // Exemplo 2.4: Labirinto
  // ==========================================
  printf("\n");
  printf("CASO 4: Encontrar Saída de um Labirinto\n");
  printf("----------------------------------------\n\n");
  
  // Representar um labirinto 3x3 como grafo
  // Layout:
  //   0 - 1 - 2
  //   |       |
  //   3 - 4   5
  //       |   |
  //   6 - 7 - 8
  
  Graph* g4 = GraphCreate(9, 0, 0);
  
  GraphAddEdge(g4, 0, 1);
  GraphAddEdge(g4, 1, 2);
  GraphAddEdge(g4, 0, 3);
  GraphAddEdge(g4, 3, 4);
  GraphAddEdge(g4, 4, 7);
  GraphAddEdge(g4, 6, 7);
  GraphAddEdge(g4, 7, 8);
  GraphAddEdge(g4, 2, 5);
  GraphAddEdge(g4, 5, 8);
  
  printf("Labirinto (grade 3x3):\n");
  printf("  0 — 1 — 2\n");
  printf("  |       |\n");
  printf("  3 — 4   5\n");
  printf("      |   |\n");
  printf("  6 — 7 — 8\n\n");
  
  printf("Entrada: vértice 0 (canto superior esquerdo)\n");
  printf("Saída: vértice 8 (canto inferior direito)\n\n");
  
  printShortestPaths(g4, 0);
  
  GraphDestroy(&g4);
  
  // ==========================================
  // Aplicações Práticas
  // ==========================================
  printf("\n");
  printf("╔════════════════════════════════════════════╗\n");
  printf("║          APLICAÇÕES PRÁTICAS               ║\n");
  printf("╚════════════════════════════════════════════╝\n\n");
  
  printf("A travessia BFS para caminhos mais curtos é útil para:\n\n");
  
  printf("1. SISTEMAS DE NAVEGAÇÃO (GPS):\n");
  printf("   - Encontrar a rota com menor número de ruas\n");
  printf("   - (Para grafos não ponderados)\n\n");
  
  printf("2. REDES SOCIAIS:\n");
  printf("   - Calcular graus de separação entre pessoas\n");
  printf("   - Sugerir conexões (amigos em comum)\n");
  printf("   - Conceito dos \"6 graus de separação\"\n\n");
  
  printf("3. ROTEAMENTO DE REDES:\n");
  printf("   - Encontrar o caminho com menor número de saltos\n");
  printf("   - Otimizar latência em redes de computadores\n\n");
  
  printf("4. JOGOS E PUZZLES:\n");
  printf("   - Resolver labirintos\n");
  printf("   - IA para jogos: encontrar caminho mais curto\n");
  printf("   - Pathfinding em jogos de estratégia\n\n");
  
  printf("5. BIOLOGIA COMPUTACIONAL:\n");
  printf("   - Analisar redes de interação de proteínas\n");
  printf("   - Encontrar caminhos metabólicos\n\n");
  
  printf("6. ANÁLISE DE WEBSITES:\n");
  printf("   - Calcular distância entre páginas web\n");
  printf("   - Otimizar estrutura de navegação\n\n");
  
  printf("VANTAGEM DO BFS:\n");
  printf("  Em grafos NÃO PONDERADOS, BFS garante encontrar o caminho\n");
  printf("  com menor número de arestas. A primeira vez que um vértice\n");
  printf("  é alcançado é sempre pela rota mais curta!\n\n");
  
  return 0;
}
