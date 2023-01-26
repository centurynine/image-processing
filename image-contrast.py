ansArray = []
count = 0
num = 0
def sum(num, row):
    ans = ((1/row)*num)
    ansArray.append(ans)
    return ansArray

def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    print(f'ARR = {arr}')
    print(f'SUM = {sum}')
    
loop = int(input('Enter loop: '))
row = int(input('Enter row: '))
for i in range(loop):
    count = count+1
    print(f"========= COUNT {count} =========")
    num = int(input('Enter num: '))
    # sum(num, row)
    sum(num, row)
    
_sum(ansArray)

