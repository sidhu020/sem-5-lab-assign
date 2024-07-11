# assign-1 Program-2
# 2. Write Program for simple interest. Simple Interest = (P x T x R)/100

principal_amount = float(input("Enter Principal amount Of Lone(IN INR Only):-"))
rate_of_interest = float(input("Enter Rate of interest (in %):- "))
number_of_years = float(input("Enter Number of years:- "))

interest = (principal_amount*rate_of_interest*number_of_years)/100

print("The  simple interest IS:- ")
print(interest)
