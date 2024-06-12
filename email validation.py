'''
This is an Email Validation project whch contains parameter like-
 1. Email must have minimum of six character
 2. Email must start with alphabet only
 3. Email must have @ and the nuber of @should be once
 4. Email must contain only a single dot and only two or three characters before from the end
 5. Email must not contain space in it
 6. Email must not contain Upper case alphabet in it'''


email=input("Enter the eamil=")
k,p,j,pr=0,0,0,0
if len(email)>=6: #Email must be more then 6 characters
    if email[0].isalpha(): #email must start with Alphabet only
        if ("@"in email) and (email.count("@")==1): #email must have @ and the count of @ should be one 
            if (email[-4]==".") ^ (email[-3]=="."): #dot should be 3 or 2 characters before froom the end
                for i in email:
                    if i==i.isspace(): #it will check if any space is present or not
                        k=1
                    elif i.isalpha(): #to check if the alphabet is upper case or lower
                        if i==i.upper():
                            p=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        j=1

                if k==1 or p==1 or j==1:
                    pr="Wrong email P5"
            else:
                pr="wrong email P4"
        
        else:
            pr="Wrong email P3"
            
    else:
        pr="Wrong Email P2"
else:
    pr="Wrong Email P1"
if pr==0:
    print('Success')
else:
    print(pr)