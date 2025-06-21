letters=["A","b","c","d","f","i","o","r","t","y","z"]
numbers=['0','9','3','4','7','8']
symbols=['!','#','$','%','^','*',')','()']
nr_letters=int(input("enter number of letters you want in your password?\n"))
nr_symbols=int(input("enter number of symbols you want i your password\n"))
nr_numbers=int(input("enter numbers you want in your password?\n"))
import random
password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
    
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
    
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)

password =" "
for char in password_list:
    password +=char
print(f"your password is:{password}")
