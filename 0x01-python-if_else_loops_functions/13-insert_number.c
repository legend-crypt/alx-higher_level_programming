#include "lists.h"

/**
 * *insert_node - insert a node into a sorted singly linked list
 * @head: the head pointer
 * @number: the number
 * Return: the address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *temp;

	temp = *head;
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		return (NULL);
	}

	while (temp && new_node->n > temp->n)
	{
		temp = temp->next;
	}
	new_node->next = temp->next;
	temp->next = new_node;
	return (*head);

}
