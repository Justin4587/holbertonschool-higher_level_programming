#include "lists.h"

/**
 * check_cycle - cycle check
 * description : checks for loop
 * @list: singly linked 
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
    listint_t *rabbit1 = list, *rabbit2 = list;

    if (list == NULL)
        return(0);

    while (rabbit1 != NULL && rabbit1->next != NULL && rabbit2 != NULL)
    {
        rabbit1 = rabbit1->next->next;
        rabbit2 = rabbit2->next;

        if (rabbit1 == rabbit2)
            return(1);
    }
    return(0);
}