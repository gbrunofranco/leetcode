#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
	int i = 0, j = 0, k = 0;
	int nums3Size = nums1Size + nums2Size;
	int *nums3 = malloc(sizeof(int)*nums3Size);
	do {
		if (k < nums3Size && i < nums1Size && j < nums2Size && nums1[i] <= nums2[j]) {
			nums3[k] = nums1[i];
			i++;
			k++;
		}
		else if (k < nums3Size && i < nums1Size && j < nums2Size && nums1[i] > nums2[j]) {
			nums3[k] = nums2[j];
			j++;
			k++;
		}
		else if (k < nums3Size && i >= nums1Size && j < nums2Size)
		{
			nums3[k] = nums2[j];
			j++;
			k++;
		}
		else if (k < nums3Size && i < nums1Size && j >= nums2Size) {
			nums3[k] = nums1[i];
			i++;
			k++;
		}
	}while(k < nums3Size);
	if (!(nums3Size%2))
	{

		int val1 = nums3[(int)(nums3Size/2)];
		int val2 = nums3[(int)(nums3Size/2) - 1];
		return (val1+(float)val2)/2;
	}
	return nums3[nums3Size/2];
}

int main () 
{
	int *nums1 = malloc(sizeof(int)*2);
	int *nums2 = malloc(sizeof(int)*1);
	nums1[0] = 1;
	nums1[1] = 3;

	nums2[0] = 2;
	double result = findMedianSortedArrays(nums1, 2, nums2, 1);
	printf("%f\n", result);
	return 0;
}
