stocks = []
with open('input16.txt', 'r') as file:
    for line in file:
        num = int(line.strip())
        if num == 0:
            break
        stocks.append(num)

stock_counts = {}
for stock in stocks:
    if stock in stock_counts:
        stock_counts[stock] += 1
    else:
        stock_counts[stock] = 1

sorted_counts = sorted(stock_counts.items(), key=lambda x: x[1], reverse=True)
trending = sorted_counts[0]
second_place = sorted_counts[1]

print("Trending: " + str(trending[0]) + " [" + str(trending[1]) + " count]")
print("Second Place: " + str(second_place[0]) + " [" + str(second_place[1]) + " count]")

