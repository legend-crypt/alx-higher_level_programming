#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: the list
 * Return: return is a cycle is found else return 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
	{
		return (0);
	}
	fast = list->next;
	slow = list;

	while (fast && slow)
	{
		if(fast->next == NULL)
		{
			return (0);
		}
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
