# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    num_months += 1
    extra = extra_payment if extra_payment_start_month <= num_months < extra_payment_end_month else 0
    new_principle = principal * (1+rate/12)
    real_payment = min(payment + extra, new_principle)
    principal = new_principle - real_payment
    total_paid += real_payment
    print(f"{num_months} {total_paid} {principal}")


print(f'Total paid ${total_paid:0.2f}')
print(f"Total months: {num_months}")
