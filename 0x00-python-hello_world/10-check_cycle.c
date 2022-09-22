#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a list contains a cycle
 * @list: the singly linked list
 * Return: 0 if cycle is not present
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
