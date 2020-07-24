
# Programmed by Sachin. 
 
k=True 
lst=[] 
while k:
  print("""
  Main menu
  1. Add Employee record
  2. Update Employee record
  3. Delete Employee record
  4. View Employee details
  5. Exit. 
  """)
 
  k=int(input("What you want to do?")) 
 
  if k==1:
    n=int(input("Enter the numbers of employee you want to add")) 
    lst=[] 
 
    for i in range(0,n):
      ele=[int(input("Enter E-ID")), input("Enter the Name"), float(input("Enter the Salary")), eval(input("Enter Department")) ] 
      lst.append(ele)
 
  print(lst[:4])
 
  if (k==2):
    j=int(input("Enter E-ID")) 
    for m in lst:
      if m[0]==j:
        print(""" What you want to update
                  a. Salary
                  b. Department 
                  c. Both
              """) 
        t=input("Select from above") 
        if t=='a':
          z=float(input("Enter new Salary")) 
          m[2]=z
        print(lst) 
        if t=='b':
          y=eval(input("Enter new Department")) 
          m[3]=y
        print(lst) 
        if t=='c':
          v=float(input("Enter new salary")) 
          u=eval(input("Enter new department")) 
          m[2]=v
          m[3]=u
        print(lst) 
      if m[0]!=j:
        print("Invalid input") 
 
  if k==3:
    g=int(input("Enter the E-ID whom you want to remove")) 
    for n in lst:
      if n[0]==g:
        del(n[:4])
      print(lst) 
 
  if k==4:
    print(lst)
 
  elif k==5:
    print("Goodbye") 
    k=None