multiplicand_number=int(input("Enter the Multiplicand Number:"))
multiplier_number = int(input("Enter the Multiplier Number:"))

def multiplication_table(multplicand_number,multiplier_number):
   for i in range(1,multiplicand_number+1) :
      print("%d * %d = %d" %(i,multiplier_number,i* multiplier_number))

multiplication_table(multiplicand_number,multiplier_number)



