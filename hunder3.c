#include<stdio.h>
#include<conio.h>
void main()
{
int n,a[100],i,j,k;
clrscr();
scanf("%d",&n);
for(i=1;i<=n;i++)
{

scanf("%d",&a[i]);
}
for(i=1;i<=n;i++)
{
for(j=i;j<=n;j++)
{
  int k=0;
if(i==a[j])
{
printf("%d",i);
  k++;
}
}}
if(k>0)
{
  printf("%d",-1);
}
getch();
}
