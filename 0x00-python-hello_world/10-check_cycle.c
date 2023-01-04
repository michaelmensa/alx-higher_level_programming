#include <stdio.h>
#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: input head
  * Return: 0 if there is no cycle, otherwise, 1.
  */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
		return (0);
	while (list)
	{
		temp = list;
		list = list->next;
		if(temp <= list)
			return (1);
	}
	return (0);
}
