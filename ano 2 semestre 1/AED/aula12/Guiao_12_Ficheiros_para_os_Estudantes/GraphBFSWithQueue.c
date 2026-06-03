//
// Algoritmos e Estruturas de Dados --- 2024/2025
//
// Joaquim Madeira, Joao Manuel Rodrigues - June 2021, Nov 2023, Nov 2024
//
// GraphBFS - QUEUE-based Breadth-First Search
//

#include "GraphBFSWithQueue.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "Graph.h"
#include "IntegersQueue.h"
#include "IntegersStack.h"

struct _GraphBFSWithQueue {
  unsigned int* marked;  // To mark vertices when reached for the first time
  int* distance;     // The number of edges on the path from the start vertex
  int* predecessor;  // The predecessor vertex, when a vertex was reached
  Graph* graph;
  unsigned int startVertex;
};

GraphBFSWithQueue* GraphBFSWithQueueExecute(Graph* g,
                                            unsigned int startVertex) {
  assert(g != NULL);
  assert(startVertex < GraphGetNumVertices(g));

  GraphBFSWithQueue* traversal =
      (GraphBFSWithQueue*)malloc(sizeof(struct _GraphBFSWithQueue));
  assert(traversal != NULL);

  unsigned int numVertices = GraphGetNumVertices(g);

  // CREATE AND INITIALIZE traversal->marked
  traversal->marked = (unsigned int*)calloc(numVertices, sizeof(unsigned int));
  assert(traversal->marked != NULL);
  
  // CREATE AND INITIALIZE traversal->distance
  traversal->distance = (int*)malloc(numVertices * sizeof(int));
  assert(traversal->distance != NULL);
  for (unsigned int i = 0; i < numVertices; i++) {
    traversal->distance[i] = -1;  // -1 means not reachable
  }
  
  // CREATE AND INITIALIZE traversal->predecessor
  traversal->predecessor = (int*)malloc(numVertices * sizeof(int));
  assert(traversal->predecessor != NULL);
  for (unsigned int i = 0; i < numVertices; i++) {
    traversal->predecessor[i] = -1;  // -1 means no predecessor
  }

  traversal->graph = g;
  traversal->startVertex = startVertex;

  // CARRY OUT THE TRAVERSAL
  
  // Create a queue for BFS
  Queue* queue = QueueCreate(numVertices);
  
  // Mark start vertex and set its distance to 0
  traversal->marked[startVertex] = 1;
  traversal->distance[startVertex] = 0;
  QueueEnqueue(queue, startVertex);
  
  // BFS iteration
  while (!QueueIsEmpty(queue)) {
    unsigned int vertex = QueueDequeue(queue);
    
    // Get adjacent vertices
    unsigned int* neighbors = GraphGetAdjacentsTo(g, vertex);
    
    // Process all neighbors
    for (unsigned int i = 1; i <= neighbors[0]; i++) {
      unsigned int w = neighbors[i];
      
      // If not yet visited
      if (traversal->marked[w] == 0) {
        traversal->marked[w] = 1;
        traversal->distance[w] = traversal->distance[vertex] + 1;
        traversal->predecessor[w] = vertex;
        QueueEnqueue(queue, w);
      }
    }
    
    // Free neighbors array
    free(neighbors);
  }
  
  // Clean up
  QueueDestroy(&queue);

  return traversal;
}

void GraphBFSWithQueueDestroy(GraphBFSWithQueue** p) {
  assert(*p != NULL);

  GraphBFSWithQueue* aux = *p;

  free(aux->marked);
  free(aux->distance);
  free(aux->predecessor);

  free(*p);
  *p = NULL;
}

// Getting the result

int GraphBFSWithQueueHasPathTo(const GraphBFSWithQueue* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  return p->marked[v];
}

Stack* GraphBFSWithQueuePathTo(const GraphBFSWithQueue* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  Stack* s = StackCreate(GraphGetNumVertices(p->graph));

  if (p->marked[v] == 0) {
    return s;
  }

  // Store the path
  for (unsigned int current = v; current != p->startVertex;
       current = p->predecessor[current]) {
    StackPush(s, current);
  }

  StackPush(s, p->startVertex);

  return s;
}

// DISPLAYING on the console

void GraphBFSWithQueueShowPath(const GraphBFSWithQueue* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  Stack* s = GraphBFSWithQueuePathTo(p, v);

  while (StackIsEmpty(s) == 0) {
    printf("%d ", StackPop(s));
  }

  StackDestroy(&s);
}

void GraphBFSWithQueueDisplay(const GraphBFSWithQueue* p) {
  assert(p != NULL);

  unsigned int numVertices = GraphGetNumVertices(p->graph);
  
  printf("Graph BFS With Queue traversal from vertex %u:\n", p->startVertex);
  printf("Vertex | Marked | Distance | Predecessor\n");
  printf("-------|--------|----------|------------\n");
  
  for (unsigned int i = 0; i < numVertices; i++) {
    printf("  %4u | %6u | %8d | %11d\n", i, p->marked[i], 
           p->distance[i], p->predecessor[i]);
  }
  printf("\n");
}

// NEW --- Display the Paths-Tree in DOT format
void GraphBFSWithQueueDisplayDOT(const GraphBFSWithQueue* p) {
  assert(p != NULL);

  Graph* original_graph = p->graph;
  unsigned int num_vertices = GraphGetNumVertices(original_graph);

  // The paths tree is a digraph, with no edge weights
  Graph* paths_tree = GraphCreate(num_vertices, 1, 0);

  // Use the predecessors array to add the tree edges
  for (unsigned int w = 0; w < num_vertices; w++) {
    // Vertex w has a predecessor vertex v?
    int v = p->predecessor[w];
    if (v != -1) {
      GraphAddEdge(paths_tree, (unsigned int)v, w);
    }
  }

  // Display the tree in the DOT format
  GraphDisplayDOT(paths_tree);

  // Housekeeping
  GraphDestroy(&paths_tree);
}
