import math

#stores costs for both costs and minimum costs
costs = []
bare_costs = []

#takes in the income and age of the user
income = int(input("income: "))
age = int(input("age: "))

#calculates food cost based on income
def food_cost(i):
    temp = 30.5723*(i**0.5146)
    costs.append(temp)
    bare_costs.append(temp)

#calculates utilities costs based on income
def utility_cost(i):
    temp = 130.451*(i**0.3209)
    costs.append(temp)
    bare_costs.append(temp)

#calculates clothing costs based on income
def clothing_cost(i):
    temp = 2.02778*(10**(-17))*(i**4)-((6.43284*(10**(-12)))*(i**3))+(5.81473*(10**(-7))*(i**2))-0.00296238*i+857.78279
    costs.append(temp)
    bare_costs.append(temp)

#calculates entertainment costs
def entertainment_cost(i):
    temp = 1.3833*(10**(-7))*(i**2)+0.006175*i+1360.978
    costs.append(temp)

#calculates transportation costs based on income
def transportation_cost(i):
    temp = round((73718.7586)/(1+(math.pow((math.e),(-(0.0000101536*i-2.57732))))))
    costs.append(temp)
#calculates healthcare costs based on age
def healthcare_cost(a):
    temp = 898-30.2*a+0.692*(a**2)
    costs.append(temp)
    bare_costs.append(temp)

#calculates child rearing costs based on income
def childcare_cost(i):
    temp = 0.104*i+4481
    costs.append(temp)

#calculates education costs based on income
def education_cost(i):
    temp = (151097.226)/(1+math.pow(math.e,(-(0.00000772441*i-1.60384))))
    costs.append(temp)
    
#each of the following housing functions
#calculate the cost of housing based on income
#each is used for a different category discussed later
def housing1(i):
    temp = 9972+((59772)/(1+math.pow(math.e,((-0.000013)*(i-223759)))))
    costs.append(temp)
    bare_costs.append(temp)

def housing2(i):
    temp = 9676*(math.pow(math.e,(0.0000067*i)))+792
    costs.append(temp)
    bare_costs.append(temp)

def housing3(i):
    temp = 887*(math.pow(math.e, (0.0000067*i)))+792
    costs.append(temp)
    bare_costs.append(temp)

#calculates income tax based on income bracket
#accounting for the fact that any income in each bracket
#is taxed in that bracket
def income_tax(i):
    total=0
    if i>=626351:
        total+=0.37*626351
        i-=626351
    if i>=250526:
        total+=0.35*250526
        i-=250526
    if i>=197301:
        total+=0.32*197301
        i-=197301
    if i>=103351:
        total+=0.24*103351
        i-=103351
    if i>=48476:
        total+=0.22*48476
        i-=48476
    if i>=11925:
        total+=0.12*11925
        i-=11925
    if i>=0:
        total+=0.1*i
    costs.append(total)
    bare_costs.append(total)
    
#runs each function with the inputted values
food_cost(income)
utility_cost(income)
clothing_cost(income)
entertainment_cost(income)
transportation_cost(income)
healthcare_cost(age)
income_tax(income)
#only includes childcare for a certain age range
if age<=50 and age>=36:
    childcare_cost(income)
#only includes education for a certain age range
if age<=36 and age>=18:
    education_cost(income)
#defines which housing equation to used based on
#age with a minimum income to move to the second level
if income<106500 or age<=36 and age>=18:
    housing1(income)
elif age<=50 and age>=36:
    housing2(income)
elif age>=51:
    housing3(income)

#stores totals for bare and regular disposable income
total1=0
total2=0

#adds up all of the expenses for bare costs and costs to get a total
for i in costs:
    total1+=i

for i in bare_costs:
    total2+=i

print(income-total1)
print(income-total2)