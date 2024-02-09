# convert.py
# program that takes a float amount in dollars and outputs absolute amount in cent
# author: eoghan walsh

dollars = float(input("Please enter dollar amount: "))
dollar_str = str("{:.2f}".format(dollars))
cent = abs(int(dollar_str.replace(".",""))) # https://www.w3schools.com/python/python_strings_modify.asp
cent_comma = "{:,}".format(cent)
print(f"That amount in cent is: {cent_comma}")