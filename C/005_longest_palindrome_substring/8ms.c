#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 500
char* longestPalindrome(char* s) {

	int stringSize;
	int subStringSize = 0, j,k;  	
	int max = 1;
	int head = 0;

	stringSize = strlen(s);

	if(s == NULL) return NULL;
	if(stringSize == 1) return s;

	for (subStringSize = 0; subStringSize < stringSize && (stringSize - subStringSize) > max/2;)				 
	{
		j=subStringSize; 
		k=subStringSize;
//		subStringSize++;
		while( k < stringSize-1  && s[k] == s[k+1]) {k++;}
		subStringSize = k + 1;
		while( j > 0 && k < stringSize-1 && s[j-1] == s[k+1]) {
			j--;
			k++;
		}


		if (max < (k - j + 1))
		{
			max = k - j + 1;
			head = j;
		}
		printf("subStringSize = %d j = %d k = %d max = %d head = %d Char = %c\n ",subStringSize,j,k,max,head,s[subStringSize] );

	}

	printf("Max = %d\n",max );

	char* res = (char *)malloc(sizeof(char) * (max + 1));

	if (res == NULL){
		printf("Memory allocate fault\n");
		return NULL;
	}

	for (subStringSize = 0; subStringSize < max; ++subStringSize)
	{
		res[subStringSize] = s[head+subStringSize];
	}
	
	res[max] = '\0';

	return res;
}
int main()
{
	char *string = malloc(sizeof(char)*5);
	string = "cbbd";
	char *lps = longestPalindrome(string);
	printf("%s of len %ld\n", lps, strlen(lps));
	return 0;
}
