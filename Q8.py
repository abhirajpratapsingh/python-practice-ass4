# Q8 : write a python script to calculate simple interest 
take_principal = int ( input ( "enter the principal ammont : ") )
take_rate = int ( input ( "enter the rate :" ) )
take_time = int (input ( "enter the time :" ) )
simple_interest = ( take_principal * take_rate * take_time ) / 100
print ( "the S.I is" , simple_interest )