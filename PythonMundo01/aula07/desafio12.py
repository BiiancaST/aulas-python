preço = float(input('qual o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('o produto que custava {:.2f}, vai custa {:.2f} na promoção'.format(preço, novo))
