//
// Exemplo 1: Identificar vértices alcançáveis usando DFS
// 
// Este programa demonstra como usar a travessia em profundidade (DFS)
// para identificar todos os vértices alcançáveis a partir de um vértice inicial
//

#include <stdio.h>
#include <stdlib.h>

#include "Graph.h"
#include "GraphDFSRec.h"

void printReachableVertices(Graph* g, unsigned int startVertex) {
  printf("========================================\n");
  printf("VÉRTICES ALCANÇÁVEIS A PARTIR DO VÉRTICE %u\n", startVertex);
  printf("========================================\n\n");
  
  // Executar DFS a partir do vértice inicial
  GraphDFSRec* dfs = GraphDFSRecExecute(g, startVertex);
  
  unsigned int numVertices = GraphGetNumVertices(g);
  unsigned int reachableCount = 0;
  
  printf("Vértices alcançáveis:\n");
  for (unsigned int v = 0; v < numVertices; v++) {
    if (GraphDFSRecHasPathTo(dfs, v)) {
      printf("  - Vértice %u", v);
      
      if (v == startVertex) {
        printf(" (vértice inicial)");
      } else {
        printf(" - Caminho: ");
        GraphDFSRecShowPath(dfs, v);
      }
      printf("\n");
      reachableCount++;
    }
  }
  
  printf("\nTotal: %u vértices alcançáveis de %u vértices no grafo\n", 
         reachableCount, numVertices);
  
  // Verificar se há vértices NÃO alcançáveis
  unsigned int unreachableCount = numVertices - reachableCount;
  if (unreachableCount > 0) {
    printf("\nVértices NÃO alcançáveis:\n");
    for (unsigned int v = 0; v < numVertices; v++) {
      if (!GraphDFSRecHasPathTo(dfs, v)) {
        printf("  - Vértice %u\n", v);
      }
    }
  }
  
  printf("\n");
  
  // Limpar memória
  GraphDFSRecDestroy(&dfs);
}

int main(void) {
  printf("╔════════════════════════════════════════╗\n");
  printf("║  EXEMPLO 1: VÉRTICES ALCANÇÁVEIS (DFS) ║\n");
  printf("╚════════════════════════════════════════╝\n\n");
  
  // ==========================================
  // Exemplo 1.1: Grafo Conexo
  // ==========================================
  printf("CASO 1: Grafo Conexo\n");
  printf("--------------------\n");
  printf("Todos os vértices estão conectados\n\n");
  
  Graph* g1 = GraphCreate(6, 0, 0);
  
  // Criar um grafo conexo
  GraphAddEdge(g1, 0, 1);
  GraphAddEdge(g1, 0, 2);
  GraphAddEdge(g1, 1, 3);
  GraphAddEdge(g1, 2, 3);
  GraphAddEdge(g1, 3, 4);
  GraphAddEdge(g1, 4, 5);
  
  printf("Estrutura do grafo:\n");
  printf("  0 -- 1 -- 3 -- 4 -- 5\n");
  printf("  |    |    |\n");
  printf("  2 -------/\n\n");
  
  printReachableVertices(g1, 0);
  
  GraphDestroy(&g1);
  
  // ==========================================
  // Exemplo 1.2: Grafo com Componentes Desconexas
  // ==========================================
  printf("\n");
  printf("CASO 2: Grafo com Componentes Desconexas\n");
  printf("-----------------------------------------\n");
  printf("Existem vértices isolados ou componentes separadas\n\n");
  
  Graph* g2 = GraphCreate(8, 0, 0);
  
  // Componente 1: vértices 0, 1, 2
  GraphAddEdge(g2, 0, 1);
  GraphAddEdge(g2, 1, 2);
  
  // Componente 2: vértices 3, 4, 5
  GraphAddEdge(g2, 3, 4);
  GraphAddEdge(g2, 4, 5);
  
  // Vértice isolado: 6
  
  // Vértice isolado: 7
  
  printf("Estrutura do grafo:\n");
  printf("  Componente 1: 0 -- 1 -- 2\n");
  printf("  Componente 2: 3 -- 4 -- 5\n");
  printf("  Isolados: 6, 7\n\n");
  
  printReachableVertices(g2, 0);
  
  printf("Nota: A partir do vértice 0, apenas os vértices da sua\n");
  printf("      componente conexa são alcançáveis (0, 1, 2).\n\n");
  
  GraphDestroy(&g2);
  
  // ==========================================
  // Exemplo 1.3: Grafo Direcionado
  // ==========================================
  printf("\n");
  printf("CASO 3: Grafo Direcionado\n");
  printf("-------------------------\n");
  printf("As arestas têm direção\n\n");
  
  Graph* g3 = GraphCreate(5, 1, 0);  // 1 = dirigido
  
  // Criar um grafo direcionado
  GraphAddEdge(g3, 0, 1);
  GraphAddEdge(g3, 1, 2);
  GraphAddEdge(g3, 2, 3);
  GraphAddEdge(g3, 3, 1);  // Ciclo: 1 -> 2 -> 3 -> 1
  GraphAddEdge(g3, 0, 4);
  
  printf("Estrutura do grafo:\n");
  printf("       /--> 1 --> 2\n");
  printf("      /     ^      |\n");
  printf("     0      |      v\n");
  printf("      \\     \\---- 3\n");
  printf("       \\--> 4\n\n");
  
  printReachableVertices(g3, 0);
  
  // Testar a partir de outro vértice
  printReachableVertices(g3, 4);
  
  printf("Nota: Em grafos direcionados, a alcançabilidade depende\n");
  printf("      da direção das arestas.\n\n");
  
  GraphDestroy(&g3);
  
  // ==========================================
  // Aplicações Práticas
  // ==========================================
  printf("\n");
  printf("╔════════════════════════════════════════╗\n");
  printf("║        APLICAÇÕES PRÁTICAS             ║\n");
  printf("╚════════════════════════════════════════╝\n\n");
  
  printf("A identificação de vértices alcançáveis é útil para:\n\n");
  
  printf("1. REDES DE COMPUTADORES:\n");
  printf("   - Identificar quais computadores podem ser alcançados\n");
  printf("     a partir de um servidor específico\n");
  printf("   - Detectar falhas de conectividade\n\n");
  
  printf("2. REDES SOCIAIS:\n");
  printf("   - Descobrir o círculo de amigos (direto e indireto)\n");
  printf("     de uma pessoa\n");
  printf("   - Calcular o tamanho de uma comunidade\n\n");
  
  printf("3. SISTEMAS DE ARQUIVOS:\n");
  printf("   - Listar todos os arquivos acessíveis a partir de\n");
  printf("     um diretório\n");
  printf("   - Verificar dependências de arquivos\n\n");
  
  printf("4. ANÁLISE DE DEPENDÊNCIAS:\n");
  printf("   - Identificar quais módulos de software são afetados\n");
  printf("     por uma mudança em um módulo específico\n\n");
  
  printf("5. JOGOS E PUZZLES:\n");
  printf("   - Determinar se um objetivo é alcançável a partir de\n");
  printf("     um estado inicial\n\n");
  
  return 0;
}
