#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * rev_list - reverses a list
 * @head: list head
 * Return: node of type listint_t
 */
listint_t *rev_list(listint_t **head)
{
listint_t *curr = *head, *nextN, *prev = NULL;
while (curr)
{
nextN = curr->next;
curr->next = prev;
prev = curr;
curr = nextN;
}
*head = prev;
return (*head);
}
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of the list
 * Return: 1 on success.0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *tmp, *opp, *cnt;
size_t size = 0, i;
if (*head == NULL || (*head)->next == NULL)
return (1);
tmp = *head;
while (tmp)
{
size++;
tmp = tmp->next;
}
tmp = *head;
for (i = 0; i < (size / 2) - 1; i++)
tmp = tmp->next;
if ((size % 2) == 0 && tmp->n != tmp->next->n)
return (0);
tmp = tmp->next->next;
opp = rev_list(&tmp);
cnt = opp;
tmp = *head;
while (opp)
{
if (tmp->n != opp->n)
return (0);
tmp = tmp->next;
opp = opp->next;
}
rev_list(&cnt);
return (1);
}
