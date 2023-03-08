#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: the list
 * Return: return is a cycle is found else return 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list->next;
	listint_t *slow = list;


	if (list == NULL)
	{
		return (0);
	}

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		fast = list->next->next;
		slow = list->next;
	}
	return (0);
}
