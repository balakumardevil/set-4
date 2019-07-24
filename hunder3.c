#include<stdio.h>
int main()
{
int n,a[100],i,j,k=0;
scanf("%d",&n);
for(i=1;i<=n;i++)
{

scanf("%d",&a[i]);
}
for(i=1;i<=n;i++)
{
for(j=i;j<=n;j++)
{
if(i==a[j])
{
printf("%d",i);
  k++;
}
}}
if(k==0)
{
  printf("%d",-1);
}
return 0;
}
