#include<stdio.h>
#include<conio.h>
int main()
{
int a[],n,k,s=0;
printf("enter the size of array");
scanf("%d",&n);
printf("enter the number");
scanf("%d",&k);
for(i=1;i<=n;i++)
{
a[i]=i;
for(j=1;j<=k;j++)
{
s=s+a[i];
}
}
printf("%d",s);
return 0;
}


