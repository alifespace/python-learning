# 
class Cart:
    color = 'red'
    brand = 'BMW'

    def run(self):
        print('Cart is running')

    def stop(self):
        print('Cart is stopping')


car1 = Cart()
print(car1.color, type(car1), car1)
car1.run()

print(Cart.brand)
Cart.brand = 'Benz'
Cart.vendor = 'Germany'
print(car1.brand)
print(car1.vendor)
del Cart.vendor
del Cart.brand