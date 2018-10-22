#include <stdio.h>
#include <stdlib.h>
#define SIZE 30000

int hash (int key)
{	
	int index = key%SIZE;
	return index < 0 ? index + SIZE : index;
}

int search (int *indexes, int key)
{
	int index = hash (key);
	if (indexes[index] == key)
		return 1;
	return 0;
}

int insert (int key, int *indexes) 
{
	int index = hash(key);
	if (indexes[index] == key)
		return 0;	
	else
	{
		indexes[index] = key;
		return 1;
	}
	return 0;
}
int lengthOfLongestSubstring(char* s) 
{
	char key;
	int *indexes = malloc(sizeof(int)*SIZE);
	int i = 0, max_length_count = 0, current_length = 0;
	while ((key = s[i]) != '\0')
	{
		i++;
		if (insert((key - '0'), indexes))
		{	
			current_length++;
			continue;
		}
		if (current_length > max_length_count)
			max_length_count = current_length;
		current_length = 0;
		for (int j = 0; j <= i; ++j)
			indexes[j] = 0;
	}
	return max_length_count;
}

int main(void)
{
	int number = lengthOfLongestSubstring("hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789");
	printf("%d\n", number);
	return 0;
}
