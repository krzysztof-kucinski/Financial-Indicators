#Company Name
name = input("What is your Company name: ")
#Analyzed year
year = input("What is the analzed year: ")

#ROIC coponents

#a1 - Earnings Before Interest and Taxes - zysk operacyjny'
#a2 - Capital assets - środki trwałe'
#b1 - Inventories - zapasy'
#b2 - Receivables - należności'
#c1 - Payables- zobowiązania wobec dostawców'

a1 = float(input("Earnings Before Interest and Taxes: "))
a2 = float(input("Capital assets: "))
b1 = float(input("Inventories: "))
b2 = float(input("Receivables: "))
c1 = float(input("Payables: "))

#ROIC formula'
Roic = float((a1)/((a2)+b1+b2-c1))

print("W roku",year,"firma",name,"wygenerowała ROIC o wartości",round(Roic,2))
