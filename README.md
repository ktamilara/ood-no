import java.io.*;
import java.util.*;
class oddnumbers
{
public static void main(String args[])
{
int num,i;
System.out.println("enter the numbers");
Scanner sc=new Scanner(System.in);
num=sc.nextInt();
for(i=1;i<=num;i++)
{
if(i%2!=0)
{
System.out.println(i + " ");
}
}
}
}
