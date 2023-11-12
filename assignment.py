print('''
 |************************************|
       YUSUF AND SONS LIMITED
 ######################################
 To calculate Simple or Compound Interest
     Enter the required information
     ''')
P = int(input("Enter given Principal: "))
R = int(input("Enter given Rate: "))
T = int(input("Enter given Time: "))
N = int(input("Enter given n: "))
simple_Interest = ((P * R * T)/100 )
compound_Interest = (P*(1 + (R/100)/N)**N * T)
print('''
 'n' can be defined as the number of times interest is applied per time period 
 Dear Customer,
 Your required''')
print('Simple Interest = ' + str(simple_Interest) +'%')
print('Compound Interest = ' + str(compound_Interest) +'%')
print('''*****************************************
              Thank You 
##########################################
        ''')