a=int(input("enter total day \n"))
abb=25400/a
ab=int(input("enter absent day \n"))
if ab>=3:
    abc=a-(ab-2)
    abcc=abc*abb
else:
    abcc=25400 
 
if ab==0:
    abcd=0   
elif ab==1:
    abcd=400
elif ab==2:
    abcd=800
elif ab>=3:
    abcd=800+280
b=float(input("enter total over time \n"))
bc=b*130
c=input("social security card yes or no \n")
d=c.lower()
if d =="yes":
    cd=400
else:
    cd=0 


print("Salary",abcc)
print("over time",bc)
print("card",cd)
print("Allowans Deduction",abcd)
print("total salary",abcc+bc+(1080-abcd)-cd)