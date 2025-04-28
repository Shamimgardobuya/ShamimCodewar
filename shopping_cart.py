#cart is a list having all the items required


#class have the product_price_ and quantity, product name
#variable to hold total current price
#removing item from cart, removing the specific product and reducing the price

class Cart:
    cart_ = {} #class attribute shared with all instances of the class
    
    def __init__(self):
        self.cart = []
    
    def add_item_to_cart(self,  name , price,  quantity, size): #instance attribute, unique value to all instances
        self.cart.append({'name': name, 'price': price, 'quantity': quantity, 'size': size})
        
        return f'Order of {name} has been added to cart, cart is now reading {self.cart}'
    def remove_item_from_cart(self,  name , price,  quantity, size):
        for item in self.cart:
            if name in item.values(): #if using db , ensure use something like bar code to uniquely identify item
                self.cart.remove(item)
        return f'Order of {name} has successfully been removed from cart {self.cart}'
    
    def checkout(self):
        order_summary = [ i.get('price') * i.get('quantity') for i in self.cart]
        return f'Here is your order summary, total {sum(order_summary)} for orders in cart {self.cart}'
        
        
        
order = Cart()
print(order.add_item_to_cart('cake', 500, 2, '200g' ))
# print(order.remove_item_from_cart('cake', 500, 1, '200g' ))
print(order.checkout())


