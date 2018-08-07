import java.util.*;
class numbers 
{
public static void main(String arg[])
{
int a;
System.out.println("enter the number");
Scanner s=new Scanner(System.in);
a=s.nextInt();
if(a>0)
{
System.out.println(a+"is positive");
}
else if(a<0)
{
System.out.println(a+"is negative");
}
else
{
System.out.println(a+"is zero");
}
}
}
