num=int(input("Enter the number"))

sum=0

pow= len(str(num))

temp=num

while(temp>0):
     
      rem= temp%10
      sum= sum+rem**pow
      temp= temp//10
if num==sum:
   
    print(num,"Number is Armstrong")

else:
    
    print(num,"Number is not a Armstrong")