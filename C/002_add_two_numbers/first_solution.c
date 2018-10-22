#include <stdio.h>
#include <stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* addTwoNumbers_wrap(struct ListNode* l1, struct ListNode* l2, int num) {
	int new_val = num;
	int carry = 0;
	if (l1 == NULL && l2 == NULL)
		return NULL;
	if (l1 != NULL)
		new_val += (*l1).val;
	if (l2 != NULL)
		new_val += (*l2).val;
	struct ListNode *node = malloc(sizeof(struct ListNode));
	if (new_val > 9)
	{
		new_val-=10;
		carry = 1;
	}
	(*node).val = new_val;
	(*node).next = addTwoNumbers_wrap ((*l1).next, (*l2).next, carry);
	return node;
}

struct ListNode* addTwoNumbers (struct ListNode* l1, struct ListNode* l2) {
	return addTwoNumbers_wrap(l1, l2, 0);
}
