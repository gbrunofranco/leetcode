#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 500
int hash (char key)
{
	int index = (int)key%SIZE;
	return index < 0 ? index + SIZE : index;
}

int search (char *keys, char key, int *values) 
{
	int index = hash (key);
	if (keys[index] == key)
		return values[index];
	return 0;
}

int insert (char key, char *keys, int value, int *values)
{
	int index = hash(key);
	if (keys[index] == key)
		return 0;
	else
	{
		keys[index] = key;
		values[index] = value;
	}
	return 1;
}
void rmv (char key, char *keys, int *values)
{
	int index = hash(key);
	keys[index] = '4';
	values[index] = -2;
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
	do {
		int counter = 0;
		for (j = 0; j < max; ++j)
			if(insert (s[start-j], keys, j, values)) {}
		for (j = 0; j < max; j++)
			if(!(insert (s[start+j], keys, j, values))) {
			counter++;}
		if (counter == max)			
			break;
		if (!count)
		{
			for (int k = start; k >= start - max; --k)
				rmv(s[k], keys, values);
			count = 1;
			steps++;
			start--;
			max--;
		}
		else {
			for (int k = start; k >= start - max; --k)
				rmv(s[k], keys, values);
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
	string = "rrrrrrrrrrrrabcba";
	char *lps = longestPalindrome(string);
	printf("%s of len %ld\n", lps, strlen(lps));
	return 0;
}
