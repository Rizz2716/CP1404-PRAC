# price_per_kwh = float(input("Enter cents per kWh: "))
# daily_use= float(input("Enter daily usage in kWh "))
# billing_days= float(input("Enter number of billing days: "))
#
# bill_estimate=float
# bill_estimate = ((price_per_kwh/100) * daily_use )* billing_days
#
# print("Estimated bill: $ {:.2f}". format(bill_estimate))

tariff_11= 0.244618
tariff_31= 0.136928
tariff=float(input("Which Tariff 11 or 31: "))
daily_use= float(input("Enter daily usage in kWh: "))
billing_days= float(input("Enter number of billing days: "))
if tariff==11:
    bill_estimate = tariff_11 * daily_use * billing_days
elif tariff==31:
    bill_estimate = tariff_31 * daily_use * billing_days

print("Estimated bill: $ {:.2f}". format(bill_estimate))

