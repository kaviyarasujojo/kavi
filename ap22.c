#include <stdio.h>
int main()
{
  int array[10000], size,c=0,i;
  printf("Enter the number of elements in array\n");
  scanf("%d", &size);
  for (i=0;i<=size;i++)
   {
   printf(i);
    c=c+i;
  }
  printf("Maximum element is %d.\n",c);
  return 0;
}
