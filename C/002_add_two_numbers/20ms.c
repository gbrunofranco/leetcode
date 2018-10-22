#include <stdio.h>
#include <stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* addTwoNumbersWrap(struct ListNode* l1, struct ListNode* l2, int carry) {
	int new_val = carry;
	int next_carry = 0;
	struct ListNode *node = malloc(sizeof(struct ListNode));
	if (l1 == NULL && l2 == NULL && carry == 0)
		return NULL;
	if (l1 != NULL)
		new_val += l1->val;
	if (l2 != NULL)
		new_val += l2->val;
	if (new_val > 9)
	{
		new_val -= 10;
		next_carry = 1;
	}
	node->val = new_val;
	if (l1 != NULL && l2 != NULL)
		node->next = addTwoNumbersWrap (l1->next, l2->next, next_carry);
	else if (l1 == NULL && l2 != NULL)
		node->next = addTwoNumbersWrap (NULL, l2->next, next_carry);
	else if (l1 != NULL && l2 == NULL)
		node->next = addTwoNumbersWrap (l1->next, NULL, next_carry);
	else if (l1 == NULL && l2 == NULL)
		node->next = addTwoNumbersWrap (NULL, NULL, next_carry);
	return node;
}

struct ListNode* addTwoNumbers (struct ListNode* l1, struct ListNode* l2) {
	return addTwoNumbersWrap(l1, l2, 0);
}

int main(void)
{
	struct ListNode* head_one = malloc(sizeof(struct ListNode));
	head_one->val = 5;
	head_one->next = NULL; 
	struct ListNode* head_two = malloc(sizeof(struct ListNode));
 	head_two->val = 5;
 	head_two->next = NULL;
	struct ListNode* result = addTwoNumbers(head_one, head_two);
	printf("%d, %d\n", result->val, result->next->val);
	return 0;
}
