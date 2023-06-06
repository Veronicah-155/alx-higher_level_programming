#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list.
 * @number: number to insert.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *current;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	current->n = number;

	if (node == NULL || node->n >= number)
	{
		current->next = node;
		*head = current;
		return (current);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	current->next = node->next;
	node->next = current;

	return (current);
}
