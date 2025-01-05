#20546
#돈을 입력 받고 몇 개를 살 수 있는지 계속 나누어야함 
money = int(input())
stocks = list(map(int,input().split()))

#준현 개미 생성
def jun():
    left_money = money
    stock_n = 0
    for stock in stocks:
        stock_n += left_money // stock
        left_money = left_money % stock
        if left_money == 0:
            break

    return left_money, stock_n

#성민 개미 생성
def sung():
    left_money = money
    stock_n = 0
    for i in range(len(stocks)-4):
        if stocks[i] < stocks[i+1] < stocks[i+2] < stocks[i+3]:
            left_money += stock_n * stocks[i+3]
            stock_n = 0

        if stocks[i] > stocks[i+1] > stocks[i+2] > stocks[i+3]:
            stock_n += left_money // stocks[i+3]
            left_money = left_money % stocks[i+3]

    return left_money, stock_n

jun_money, jun_stock = jun()
total_jun_money = jun_money + jun_stock * stocks[-1]
sung_money, sung_stock = sung()
total_sung_money = sung_money + sung_stock * stocks[-1]

#if문을 통해 print 결정
if total_jun_money < total_sung_money:
    print('TIMING')
elif total_jun_money > total_sung_money:
    print('BNP')
else:
    print('SAMESAME')
