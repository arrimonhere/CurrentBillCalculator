""" Python Class-LT A: Residental
Current Bill Calculator
Developed By - Ar Rimon Ahmed """

Unit = int(input("Enter Your Using Unit : "))


# If Unit Became 1-75

if Unit>=1 and Unit<=75 :
	U_Price1 = Unit*4
	U_P = int( f'{(U_Price1):.0f}')
	
	D_Charge = 25

	Nit_Bill = U_P+D_Charge

	Vat = int( f'{((Nit_Bill*5)/100):.0f}')

	M_Charge = 10

	Total = Nit_Bill+Vat+M_Charge
	
	print("\nYour Using Unit Price Is : ",U_P)
	print("Demand Charge Is : ",D_Charge)
	print("Nit Bill Is : ",Nit_Bill)
	print("Vat Is : ",Vat)
	print("Meter Charge Is : ",M_Charge)
	print("Your Total Curent Bill Is : ",Total)
	
	

# If Unit Became 76-200
	
elif Unit>=76 and Unit<=200 :

  U_Price1 = (Unit-75)*5.45
  U_Price2 = 75*4
	
  U_PP = int( f'{(U_Price1+U_Price2):.0f}')
	
  D_Charge = 25

  Nit_Bill = U_PP+D_Charge

  Vat = int( f'{((Nit_Bill*5)/100):.0f}')

  M_Charge = 10

  Total = Nit_Bill+Vat+M_Charge
	
  print("\nYour Using Unit Price Is : ",U_PP)
  print("Demand Charge Is : ",D_Charge)
  print("Nit Bill Is : ",Nit_Bill)
  print("Vat Is : ",Vat)
  print("Meter Charge Is : ",M_Charge)
  print("Your Total Curent Bill Is : ",Total)


  # If Unit Became 201-300
	
elif Unit>=201 and Unit<=300 :
	
  U_Price1 = (Unit-200)*5.70
  U_Price2 = (200-75)*5.45
  U_Price3 = 75*4

  U_PPP = int( f'{(U_Price1+U_Price2+U_Price3):.0f}')
	
  D_Charge = 25

  Nit_Bill = U_PPP+D_Charge

  Vat = int( f'{((Nit_Bill*5)/100):.0f}')

  M_Charge = 10

  Total = Nit_Bill+Vat+M_Charge
	
  print("\nYour Using Unit Price Is : ",U_PPP)
  print("Demand Charge Is : ",D_Charge)
  print("Nit Bill Is : ",Nit_Bill)
  print("Vat Is : ",Vat)
  print("Meter Charge Is : ",M_Charge)
  print("Your Total Curent Bill Is : ",Total)

  # If Unit Became 301-400

elif Unit>=301 and Unit<=400 :
	
  U_Price1 = (Unit-300)*6.02
  U_Price2 = (300-200)*5.70
  U_Price3 = (200-75)*5.45
  U_Price4 = 75*4

  U_PPPP = int( f'{(U_Price1+U_Price2+U_Price3+U_Price4):.0f}')
	
  D_Charge = 25

  Nit_Bill = U_PPPP+D_Charge

  Vat = int( f'{((Nit_Bill*5)/100):.0f}')

  M_Charge = 10

  Total = Nit_Bill+Vat+M_Charge
	
  print("\nYour Using Unit Price Is : ",U_PPPP)
  print("Demand Charge Is : ",D_Charge)
  print("Nit Bill Is : ",Nit_Bill)
  print("Vat Is : ",Vat)
  print("Meter Charge Is : ",M_Charge)
  print("Your Total Curent Bill Is : ",Total)


    # If Unit Became 401-600

elif Unit>=401 and Unit<=600 :
	
  U_Price1 = (Unit-400)*9.30
  U_Price2 = (400-300)*6.02
  U_Price3 = (300-200)*5.70
  U_Price4 = (200-75)*5.45
  U_Price5 = 75*4

  U_PPPPP = int( f'{(U_Price1+U_Price2+U_Price3+U_Price4+U_Price5):.0f}')
	
  D_Charge = 25

  Nit_Bill = U_PPPPP+D_Charge

  Vat = int( f'{((Nit_Bill*5)/100):.0f}')

  M_Charge = 10

  Total = Nit_Bill+Vat+M_Charge
	
  print("\nYour Using Unit Price Is : ",U_PPPPP)
  print("Demand Charge Is : ",D_Charge)
  print("Nit Bill Is : ",Nit_Bill)
  print("Vat Is : ",Vat)
  print("Meter Charge Is : ",M_Charge)
  print("Your Total Curent Bill Is : ",Total)


  # If Unit Became Grater Than 600

elif Unit>=601 :
	
  U_Price1 = (Unit-600)*10.70
  U_Price2 = (600-400)*9.30
  U_Price3 = (400-300)*6.02
  U_Price4 = (300-200)*5.70
  U_Price5 = (200-75)*5.45
  U_Price6 = 75*4

  U_PPPPP = int( f'{(U_Price1+U_Price2+U_Price3+U_Price4+U_Price5+U_Price6):.0f}')
	
  D_Charge = 25

  Nit_Bill = U_PPPPP+D_Charge

  Vat = int( f'{((Nit_Bill*5)/100):.0f}')

  M_Charge = 10

  Total = Nit_Bill+Vat+M_Charge
	
  print("\nYour Using Unit Price Is : ",U_PPPPP)
  print("Demand Charge Is : ",D_Charge)
  print("Nit Bill Is : ",Nit_Bill)
  print("Vat Is : ",Vat)
  print("Meter Charge Is : ",M_Charge)
  print("Your Total Curent Bill Is : ",Total)
