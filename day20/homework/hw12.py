#შეიყვანეთ რიცხვი და დაბეჭდეთ ყველა რიცხვი, რომელიც ნაკლებია ან გათანაბრებულია 10-თან.
number = int(input("enter number"))
for number in range(number):
    if number<=10:
             number=number+1
             print(number)