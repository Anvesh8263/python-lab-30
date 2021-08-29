Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #include <stdio.h>

int main()
{
    int s;
    scanf("%d",&s);
    int a[s][s];
    for(int i=0;i<s;i++)
        for(int j=0;j<s;j++)
            scanf("%d",&a[i][j]);
    
    int t = 0, b = 0, l = 0, r = 0;
    // top
    for(int i=0;i<s;i++)
    {
        if(a[0][i]==0)
        {   t = 1;
            continue;}
        else
        {   t = 0;
            break;}
    }
    // bottom
    for(int i=0;i<s;i++)
    {
        if(a[s-1][i]==0)
        {   b = 1;
            continue;}
        else
        {   b = 0;
            break;}
    }
    // right
    for(int i=0;i<s;i++)
    {
        if(a[i][s-1]==0)
        {   r = 1;
            continue;}
        else
        {   r = 0;
            break;}
    }
    // left
    for(int i=0;i<s;i++)
    {
        if(a[i][0]==0)
        {   l = 1;
            continue;}
        else
        {   l = 0;
            break;}
    }
    
    if (t == 1)
    printf("Folded\nTop");
    else if (b == 1)
    printf("Folded\nBottom");
    else if (r == 1)
    printf("Folded\nRight");
    else if (l == 1)
    printf("Folded\nLeft");
    else
    printf("Not Folded");
    

    return 0;
}