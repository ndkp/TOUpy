prices = [1600, 1900, 2500, 3200]

tax_prices=list(filter(lambda price:price*1.08,prices))
print(tax_prices)