//
// Programa de teste para comparar as travessias DFS e BFS
//

#include <stdio.h>
#include <stdlib.h>

#include "Graph.h"
#include "GraphDFSRec.h"
#include "GraphDFSWithStack.h"
#include "GraphBFSWithQueue.h"

int main(void) {
  // Criar um grafo de teste
  // Grafo não dirigido com 7 vértices
  Graph* g = GraphCreate(7, 0, 0);
  
  // Adicionar arestas
  GraphAddEdge(g, 0, 1);
  GraphAddEdge(g, 0, 2);
  GraphAddEdge(g, 1, 3);
  GraphAddEdge(g, 1, 4);
  GraphAddEdge(g, 2, 5);
  GraphAddEdge(g, 2, 6);
  
  printf("========================================\n");
  printf("Grafo de teste:\n");
  printf("========================================\n");
  GraphDisplay(g);
  printf("\n");
  
  // Vértice inicial para as travessias
  unsigned int startVertex = 0;
  
  // ==========================================
  // Teste 1: DFS Recursivo
  // ==========================================
  printf("========================================\n");
  printf("1. DFS RECURSIVO (a partir do vértice %u)\n", startVertex);
  printf("========================================\n");
  
  GraphDFSRec* dfsRec = GraphDFSRecExecute(g, startVertex);
  GraphDFSRecDisplay(dfsRec);
  
  printf("Ordem de visita e caminhos:\n");
  for (unsigned int v = 0; v < GraphGetNumVertices(g); v++) {
    if (GraphDFSRecHasPathTo(dfsRec, v)) {
      printf("  Vértice %u: ", v);
      GraphDFSRecShowPath(dfsRec, v);
      printf("\n");
    }
  }
  printf("\n");
  
  // ==========================================
  // Teste 2: DFS Iterativo com Stack
  // ==========================================
  printf("========================================\n");
  printf("2. DFS ITERATIVO COM STACK (a partir do vértice %u)\n", startVertex);
  printf("========================================\n");
  
  GraphDFSWithStack* dfsStack = GraphDFSWithStackExecute(g, startVertex);
  GraphDFSWithStackDisplay(dfsStack);
  
  printf("Ordem de visita e caminhos:\n");
  for (unsigned int v = 0; v < GraphGetNumVertices(g); v++) {
    if (GraphDFSWithStackHasPathTo(dfsStack, v)) {
      printf("  Vértice %u: ", v);
      GraphDFSWithStackShowPath(dfsStack, v);
      printf("\n");
    }
  }
  printf("\n");
  
  // ==========================================
  // Teste 3: BFS com Queue
  // ==========================================
  printf("========================================\n");
  printf("3. BFS COM QUEUE (a partir do vértice %u)\n", startVertex);
  printf("========================================\n");
  
  GraphBFSWithQueue* bfs = GraphBFSWithQueueExecute(g, startVertex);
  GraphBFSWithQueueDisplay(bfs);
  
  printf("Ordem de visita, caminhos e distâncias:\n");
  for (unsigned int v = 0; v < GraphGetNumVertices(g); v++) {
    if (GraphBFSWithQueueHasPathTo(bfs, v)) {
      printf("  Vértice %u: ", v);
      GraphBFSWithQueueShowPath(bfs, v);
      printf("\n");
    }
  }
  printf("\n");
  
  // ==========================================
  // Comparação
  // ==========================================
  printf("========================================\n");
  printf("COMPARAÇÃO DAS TRAVESSIAS\n");
  printf("========================================\n");
  printf("\n");
  
  printf("Observações:\n");
  printf("1. DFS Recursivo vs DFS Iterativo:\n");
  printf("   - A ordem de visita será IGUAL se empilharmos os adjacentes\n");
  printf("     em ORDEM REVERSA (último adjacente primeiro).\n");
  printf("   - Se empilharmos na ordem direta, a ordem será DIFERENTE.\n");
  printf("\n");
  
  printf("2. DFS vs BFS:\n");
  printf("   - DFS explora em profundidade (vai até o fim antes de voltar)\n");
  printf("   - BFS explora por níveis (visita todos os vizinhos antes de\n");
  printf("     avançar para o próximo nível)\n");
  printf("\n");
  
  printf("3. Caminhos mais curtos:\n");
  printf("   - BFS garante caminhos mais curtos em grafos não ponderados\n");
  printf("   - DFS não garante caminhos mais curtos\n");
  printf("   - O array 'distance' em BFS mostra o número de arestas no\n");
  printf("     caminho mais curto a partir do vértice inicial\n");
  printf("\n");
  
  // Limpar memória
  GraphDFSRecDestroy(&dfsRec);
  GraphDFSWithStackDestroy(&dfsStack);
  GraphBFSWithQueueDestroy(&bfs);
  GraphDestroy(&g);
  
  return 0;
}
