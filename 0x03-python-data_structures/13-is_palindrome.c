#include "lists.h"
#define CAPACITY 100000

int is_palindrome(listint_t **head) {
  int nums[CAPACITY];
  int length = 0;

  for (listint_t *temp = *head; temp; temp = temp->next)
    nums[length++] = temp->n;

  for (int i = 0; i < length / 2; i++)
    if (nums[i] != nums[length - i - 1])
      return 0;

  return 1;
}
