# count.py
# program that counts how many times it was run.
# author: eoghan walsh

FILENAME = "count.txt"

def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
'''    
num = read_number()
print(num)
'''
def write_number(number):
    with open(FILENAME,"wt") as f:
        f.write(str(number))
'''
write_number(0)
'''

num = read_number()
num +=1
print(f"We have run this program {num} times")
write_number(num)