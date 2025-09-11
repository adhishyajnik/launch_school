from datetime import datetime as dt

cur_age = int(input('What is your age? '))
ret_age = int(input('At what age would you like to retire? '))
yrs_rem = ret_age - cur_age

cur_yrr = dt.now().year

print(f"It's {cur_yrr}. You will retire in {cur_yrr + yrs_rem}.")
print(f"You have only {yrs_rem} years of work to go!")