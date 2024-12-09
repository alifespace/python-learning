def is_Prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    
    return True

def process_integer(count):
    total = 0
    for i in range(count):
        num = int(input("Please input an integer:"))
        print(str(num) + ": " + str(is_Prime(num)))
        total += num
    print("Average number: ", total/count)        

process_integer(int(input("Please input how many integer: ")))