def is_Prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: 
            print(str(num) + " is not prime.")
            return
    
    print(str(num) + " is prime.")

def process_integer(str1):
    total = 0
    count = 1
    num = ""
    for i in str1:
        if i == ' ':
            total += int(num)
            is_Prime(int(num))
            count += 1
            num = ""
        else:
            num += i
    is_Prime(int(num))
    total += int(num)
    print("Average number: ", total/count)        

process_integer(input("Please input several integer: "))