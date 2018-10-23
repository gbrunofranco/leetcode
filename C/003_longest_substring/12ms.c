#include <stdio.h>
#include <stdlib.h>
#define SIZE 100

int hash (int key)
{	
	int index = key%SIZE;
	return index < 0 ? index + SIZE : index;
}

int search (int *keys, int key, int *values)
{
	int index = hash (key);
	if (keys[index] == key)
		return values[index];
	return 0;
}

int insert (int key, int *keys, int value, int *values) 
{
	int index = hash(key);
	if (keys[index] == key)
		return 0;	
	else
	{
		keys[index] = key;
		values[index] = value;
		return 1;
	}
	return 0;
}
void rmv(int *keys, int key, int *values)
{
	int index = hash (key);
	keys[index] = -50;
	values[index] = -50;
}
int lengthOfLongestSubstring(char* s) 
{
	char key;
	int *keys = malloc(sizeof(int)*SIZE);
	int *values = malloc(sizeof(int)*SIZE);
	int start = 0;
	for (int i = 0; i < SIZE; ++i)
	{
		values[i] = -50;
		keys[i] = -50;
	}
	int i = 0, max_length_count = 0, current_length = 0;
	while ((key = s[i]) != '\0')
	{
		i++;
		if (insert((key - '0'), keys, i, values))
		{	
			current_length++;
			continue;
		}
		if (current_length > max_length_count)
			max_length_count = current_length;
		int remove = search (keys, (key - '0'), values);
		for (int j = remove - 1; j >= start; --j)
		{
			current_length--;
			rmv(keys, (s[j] - '0'), values);
		}
		i--;
		start = remove;
	}
	return max_length_count < current_length ? current_length: max_length_count;
}

int main(void)
{		
	int number = lengthOfLongestSubstring("adbce");
	printf("%d\n", number);
	return 0;
}
