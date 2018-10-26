#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 500
int hash (char key)
{
	int index = (int)key%SIZE;
	return index < 0 ? index + SIZE : index;
}

int search (char key, char *keys, int value, int *values)
{
	int index = hash(key);
	while (keys[index] == key) {
		if (values[index] == value) {
			return 1;
		}
		index++;
		index %= SIZE;
	}
	return 0;
}
int insert (char key, char *keys, int value, int *values)
{
	int index = hash(key);
	while (values[index] != -1) {
		index++;
		index %= SIZE;
	}
	keys[index] = key;
	values[index] = value;
	return 1;
}
void rmv (char *keys, int *values)
{
	for (int i = 0; i < SIZE; ++i)
	{
		keys[i] = '/';
		values[i] = -1;
	}
}
char* longestPalindrome(char* s) {
	int s_length = strlen(s);
	char *keys = malloc(sizeof(char)*SIZE);
	int *values = malloc(sizeof(int)*SIZE);
	int i = s_length%2, start = s_length/2;
	int k;
	int max = start + i, count = 0, j, steps = 0;
	if(!i)
		start--;
	for (j = 0; j < SIZE; ++j)
		values[j] = -1;
	do {
		int counter = 0;
		printf("%d\n", start);
		for (j = 0; j < max; ++j)
			if(insert (s[start-j], keys, j, values)) {}
		for (j = 0; j < max; j++)
			if((search (s[start+j], keys, j, values))) {
				counter++;}
		if (counter == max)			
			break;
		if (!count)
		{
			rmv(keys, values);
			count = 1;
			steps++;
			start-=steps;
			max--;
		}
		else {
			rmv(keys, values);
			count = 0;
			start += steps;
			start += steps;
		}
	}while(max > 1);
	char *lps = malloc(sizeof(char)*(max));
	for (k = start, j = max-1; j >=0; --k, --j)
		lps[j] = s[k];
	return lps;
}
int main()
{
	char *string = malloc(sizeof(char)*5);
	string = "reabcba";
	char *lps = longestPalindrome(string);
	printf("%s of len %ld\n", lps, strlen(lps));
	return 0;
}
