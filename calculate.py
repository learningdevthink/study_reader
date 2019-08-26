# string = input("숫자 값을 입력하세요 >")
num = 26



def is_prime_number(num):
    if num % 2 == 1:
        if num % 3 == 1:
            return True
        return False
    return False
    
for i in range(1, num+1):
    if is_prime_number(i):
        print(i)


