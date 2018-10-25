#include <stdio.h>
#include <stdlib.h>
char* longestPalindrome(char* s) {
	int length = strlen(s);
	int i = length/2;
	int counter = length%2;
	int max_lps_length = 1001;
	int lps_length = 0;
	int lps_start;
	do {
		if (
	}
	return ;
}
int main()
{
	char *string = malloc(sizeof(char)*5);
	string = "abrba";
	char *lps = longestPalindrome(string);
	printf("%s\n", lps);
	return 0;
}
