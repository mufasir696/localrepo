while(True):
  print("1.for Addition/2.for Subtraction/n3.for Multiplication/n4.for Division/n5.for GPA calculate/n6.for CGPA calculate")
  choice=int(input("Enter the option"))
  if choice==1:
    n1=int(input("Enter the first number"))
    n2=int(input("Enter the second number"))
    print("Sum",n1+n2)
  elif choice==2:
      n1=int(input("Enter the first number"))
      n2=int(input("Enter the second number"))
      print("Subtraction",n1-n2)
  elif choice==3:
       n1=int(input("Enter the first number"))
       n2=int(input("Enter the second number"))
       print("Multiplication",n1*n2)
  elif choice==4:
       n1=int(input("Enter the first number"))
       n2=int(input("Enter the second number"))
       print("Division",n1/n2)
  elif choice==5:
    crn=int(input("Enter the number of courses: "))
    total_credits=0
    total_gp=0.0
    for i in range(1, crn+1):
        crm=input("Enter the name of course: ")
        crd=int(input("Enter the credit hour of this course: "))
        crt=int(input("Enter the total marks of this course: "))
        cro=int(input("Enter the obtained marks of this course: "))
        
        pert = (cro / crt) * 100
        
        if pert >= 90 and pert <= 100:
            gp = 4.0
        elif pert >= 80 and pert < 90:
            gp = 3.0
        elif pert >= 70 and pert < 80:
            gp = 2.0
        elif pert >= 60 and pert < 70:
            gp = 1.0
        else:
            gp = 0
        
        total_gp += gp * crd
        total_credits += crd
    
    gpa = total_gp / total_credits
    print("Your GPA is:", round(gpa, 2))
  elif choice==6:
      sem=int(input("Enter the number of semester"))
      total_credit=0
      total_weight=0.0
      for i in range(1,sem+1):
          gpa=float(input(f"Enter the gpa of:{i}"))
          crd=int(input("Enter the credit hour"))
          total_credit+=crd
          total_weight+=gpa*crd

      cgpa=total_weight/total_credit
      print("CGPA",cgpa)
  else:
      exit()
