//
// Algoritmos e Estruturas de Dados --- 2024/2025
//
// Joaquim Madeira, Nov 2023, Nov 2024
//

// Complete the functions (marked by ...)
// so that they pass all tests.

#include "PersonSet.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "SortedList.h"

// NOTE THAT:
// - Field capacity was eliminated.
// - Field size was eliminated, because size==ListGetSize(...).

// Definition of the structure
struct _PersonSet_ {
  List *persons;  // points to a SortedList of Person pointers
};

// Comparison function to be used in generic SortedList.
// Comparison is based on Person ID
static int cmpP(const void *a, const void *b) {
  Person *p1 = (Person *)a;
  Person *p2 = (Person *)b;
  int d = p1->id - p2->id;
  return (d > 0) - (d < 0);
}

// Create a PersonSet.
PersonSet *PersonSetCreate() {
  // You must allocate space for the struct and create an empty persons list!
  PersonSet *ps = (PersonSet *)malloc(sizeof(PersonSet));
  if (ps == NULL) abort();
  
  ps->persons = ListCreate(cmpP);
  
  return ps;
}

// Destroy PersonSet *pps
void PersonSetDestroy(PersonSet **pps) {
  assert(*pps != NULL);
  
  PersonSet *ps = *pps;
  
  // Clear the list (this frees the nodes but not the Person objects)
  ListDestroy(&(ps->persons));
  
  // Free the PersonSet structure
  free(ps);
  *pps = NULL;
}

int PersonSetSize(const PersonSet *ps) { return ListGetSize(ps->persons); }

int PersonSetIsEmpty(const PersonSet *ps) { return ListIsEmpty(ps->persons); }

void PersonSetPrint(const PersonSet *ps) {
  printf("{\n");
  for (ListMoveToHead(ps->persons); ListCurrentIsInside(ps->persons);
       ListMoveToNext(ps->persons)) {
    Person *p = (Person *)ListGetCurrentItem(ps->persons);
    PersonPrintf(p, ";\n");
  }
  printf("}(size=%d)\n", PersonSetSize(ps));
  ListTestInvariants(ps->persons);
}

// Find node in list ps->persons of person with given id.
// (INTERNAL function.)
static int search(const PersonSet *ps, int id) {
  Person dummyperson;
  dummyperson.id = id;
  return ListSearch(ps->persons, &dummyperson);
}

// Add person *p to *ps.
// Do nothing if *ps already contains a person with the same id.
void PersonSetAdd(PersonSet *ps, Person *p) {
  assert(ps != NULL);
  assert(p != NULL);
  
  // Try to insert the person. ListInsert handles duplicates.
  ListInsert(ps->persons, p);
}

// Pop one person out of *ps.
Person *PersonSetPop(PersonSet *ps) {
  assert(!PersonSetIsEmpty(ps));
  // It is easiest to pop and return the person in the first position!
  
  return (Person *)ListRemoveHead(ps->persons);
}

// Remove the person with given id from *ps, and return it.
// If no such person is found, return NULL and leave set untouched.
Person *PersonSetRemove(PersonSet *ps, int id) {
  // You may call search here!
  assert(ps != NULL);
  
  if (search(ps, id) == 0) {
    // Found the person, remove it
    return (Person *)ListRemoveCurrent(ps->persons);
  }
  
  return NULL;
}

// Get the person with given id of *ps.
// return NULL if it is not in the set.
Person *PersonSetGet(const PersonSet *ps, int id) {
  // You may call search here!
  assert(ps != NULL);
  
  if (search(ps, id) == 0) {
    // Found the person, return it
    return (Person *)ListGetCurrentItem(ps->persons);
  }
  
  return NULL;
}

// Return true (!= 0) if set contains person wiht given id, false otherwise.
int PersonSetContains(const PersonSet *ps, int id) {
  return search(ps, id) >= 0;
}

// Return a NEW PersonSet with the union of *ps1 and *ps2.
// NOTE: memory is allocated.  Client must call PersonSetDestroy!
PersonSet *PersonSetUnion(const PersonSet *ps1, const PersonSet *ps2) {
  PersonSet *ps = PersonSetCreate();

  // Add all persons from ps1
  for (ListMoveToHead(ps1->persons); ListCurrentIsInside(ps1->persons);
       ListMoveToNext(ps1->persons)) {
    Person *p = (Person *)ListGetCurrentItem(ps1->persons);
    PersonSetAdd(ps, p);
  }
  
  // Add all persons from ps2 (duplicates will be ignored by PersonSetAdd)
  for (ListMoveToHead(ps2->persons); ListCurrentIsInside(ps2->persons);
       ListMoveToNext(ps2->persons)) {
    Person *p = (Person *)ListGetCurrentItem(ps2->persons);
    PersonSetAdd(ps, p);
  }

  return ps;
}

// Return a NEW PersonSet with the intersection of *ps1 and *ps2.
// NOTE: memory is allocated.  Client must call PersonSetDestroy!
PersonSet *PersonSetIntersection(const PersonSet *ps1, const PersonSet *ps2) {
  PersonSet *ps = PersonSetCreate();
  
  // For each person in ps1, check if it's also in ps2
  for (ListMoveToHead(ps1->persons); ListCurrentIsInside(ps1->persons);
       ListMoveToNext(ps1->persons)) {
    Person *p = (Person *)ListGetCurrentItem(ps1->persons);
    if (PersonSetContains(ps2, p->id)) {
      PersonSetAdd(ps, p);
    }
  }

  return ps;
}

// Return a NEW PersonSet with the set difference of *ps1 and *ps2.
// NOTE: memory is allocated.  Client must call PersonSetDestroy!
PersonSet *PersonSetDifference(const PersonSet *ps1, const PersonSet *ps2) {
  PersonSet *ps = PersonSetCreate();
  
  // For each person in ps1, add it to result if it's NOT in ps2
  for (ListMoveToHead(ps1->persons); ListCurrentIsInside(ps1->persons);
       ListMoveToNext(ps1->persons)) {
    Person *p = (Person *)ListGetCurrentItem(ps1->persons);
    if (!PersonSetContains(ps2, p->id)) {
      PersonSetAdd(ps, p);
    }
  }

  return ps;
}

// Return true iff *ps1 is a subset of *ps2.
int PersonSetIsSubset(const PersonSet *ps1, const PersonSet *ps2) {
  assert(ps1 != NULL);
  assert(ps2 != NULL);
  
  // Check if every person in ps1 is also in ps2
  for (ListMoveToHead(ps1->persons); ListCurrentIsInside(ps1->persons);
       ListMoveToNext(ps1->persons)) {
    Person *p = (Person *)ListGetCurrentItem(ps1->persons);
    if (!PersonSetContains(ps2, p->id)) {
      return 0;  // Found a person in ps1 that's not in ps2
    }
  }
  
  return 1;  // All persons in ps1 are also in ps2
}

// Return true if the two sets contain exactly the same elements.
int PersonSetEquals(const PersonSet *ps1, const PersonSet *ps2) {
  // You may call PersonSetIsSubset here!
  assert(ps1 != NULL);
  assert(ps2 != NULL);
  
  // Two sets are equal if they have the same size and each is a subset of the other
  return (PersonSetSize(ps1) == PersonSetSize(ps2)) && 
         PersonSetIsSubset(ps1, ps2) && 
         PersonSetIsSubset(ps2, ps1);
}
