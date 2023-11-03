/*
 * Defines functions for a linked list.
 * CSC 225, Assignment 7
 * Given code, Winter '20
 */

#include <stdlib.h>
#include <stdio.h>
#include "list.h"

/* lstcreate: Creates an empty linked list. */
List *lstcreate() {
    /* TODO: Complete this function.
     *       Given: n/a
     *       Returns: A pointer to a dynamically allocated List structure */
    List* list = (List*)malloc(sizeof(struct List));
    list->head = NULL;
    list->size = 0;
    return list;
}

/* lstdestroy: Destroys an existing linked list. */
void lstdestroy(List *lst) {
    /* TODO: Complete this function.
    *   Given: A pointer to a List structure
    *  Returns: n/a */
    Node* head = lst->head;
    int size = lst->size;
    int i = 0;
    while(i <= (size - 1) && head != NULL){
        Node* next = head->next;
        free(head);
        head = next;
        i++;
    }
    free(lst);
}

/* lstsize: Computes the size of a linked list. */
int lstsize(List *lst) {
    /* TODO: Complete this function.
    *   Given: A pointer to a List structure
    *  Returns: The size of that list */
    Node* head = lst->head;
    int i = 0;
    while(head != NULL){
        Node* next = head->next;
        i++;
        head = next;
    }
    return i;
}

/* lstget: Gets the element in a linked list at an index. */
void *lstget(List *lst, int idx) {
    /* TODO: Complete this function.
    *       Given: A pointer to a List structure, an index
    *       Returns: A pointer to that element, NULL if none exists */
    Node* head = lst->head;
    int i = 0;
    while(i != idx){
        Node* next = head->next;
        i++;
        head = next;
    }
    return head;
}

/* lstset: Sets the element in a linked list at an index. */
int lstset(List *lst, int idx, void *data) {
    /* TODO: Complete this function.
    *       Given: A pointer to a List structure, an index, a pointer to data
    *      Returns: 0 on success, 1 if index not in bounds [0, size - 1] */
    while (((lst->size) - 1) >= idx && idx >= 0){
        Node* head = lst->head;
        int i = 0;
        while (i != idx){
            Node* next = head->next;
            i++;
            head = next;
        }
        head -> data = data;
        return 0;
    }
    return 1;
}

/* lstadd: Adds an element to a linked list at an index. */
int lstadd(List *lst, int idx, void *data) {
    /* TODO: Complete this function.
    *       Given: A pointer to a List structure, an index, a pointer to data
    *       Returns: 0 on success, 1 if index not in bounds [0, size] */
    Node* head;
    Node* last;
    int i = 0;
    Node* newNode = malloc(sizeof(Node));
    newNode->data = data;
    head = lst->head;
    last = head;
        
    if(idx > lst->size || idx < 0){
        return 1;
    }
    
    if(lst->head == NULL){
         newNode->next = NULL;
         lst->head = newNode;
         lst->size++;
         return 0;
    }
        
    while(i != idx){
         i++;
         last = head;
         head = head->next;
    }
        
    newNode->data = data;
    newNode->next = NULL;
        
    last->next = newNode;
    newNode->next = head;
    lst->size++;
    return 0;
}

/* lstremove: Removes an element from a linked list at an index. */
void *lstremove(List *lst, int idx) {
    /* TODO: Complete this function.
    *     Given: A pointer to a List structure, an index
    *    Returns: A pointer to the removed element, NULL if none exists */
    Node* prev = NULL;
    Node* head = lst->head;
    int i = 0;
    while(head != NULL){
        if (i == idx){
            Node* removed = head;
            void* temp = removed->data;
            if (prev != NULL){
                prev->next = head->next;
            }
            else{
                lst->head = head->next;
            }
            lst->size--;
            free(removed);
            return temp;
        }
        prev = head;
        head = head->next;
        i++;
    }
    return NULL;
}

/* lstreverse: Creates a new linked list in reverse order. */
List *lstreverse(List *lst) {
    /* TODO: Complete this function.
     *       Given: A pointer to a List structure
     *       Returns: A pointer to a newly allocated List containing the
     *                same elements in reversed order */
    List* revList = (List*)malloc(sizeof(List));
    Node* prev = NULL;
    Node* node = lst->head;
    while(node!=NULL){
        Node* x = (Node*)malloc(sizeof(Node));
        x->data = node->data;
        x->next = prev;
        prev = x;
        node = node->next;
    }
    revList->head = prev;
    return revList;
}
