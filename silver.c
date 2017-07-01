#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,c;
clrscr();
printf("\n enter the number");
scanf("\n%d%\n%d\n%d",&a,&b,&c");
if(a>b&&a>c)
{
printf("%d is greater",a);
}
else if(b>c&&b>a)
{
printf("%d is greater",b);
}
else if(c>a&&c>b)
{
printf("%d is greater",c);
}
else
{
printf(" give correct value");
}
getch();
}
