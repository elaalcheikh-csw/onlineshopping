class product:
   
    def __init__(self,name=str(),price=float(),quantity=int()):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display_details(self):
        print(f" name of the product: {self.name}")
        print(f"price of the product: {self.price}")
        print(f" quantity of the products:{self.quantity}")
class ShoppingCart:
    
     def __init__(self,products=[]):
         self.products=products
     def add_product(self, product):
         self.products.append(product)
     def remove_product(self, product):
         if product in self.products:
            self.products.remove(product)
         else:
             print(f" this product doesn't exist in the cart")
     def view_cart(self):
         if product in self.products:
           print("shpcrt:")
           for product in self.products:
            
              product.display_details()
         else:
             print("There is no product inside this cart")
         

                 
class User:
     def __init__(self,username=str(), email=str()):
         self.username=username
         self.email=email
         self.shopping_cart=ShoppingCart()
     def view_cart(self):
         self.shopping_cart.view_cart()
     def checkout(self):
         if not self.shopping_cart.products:
             print("you have to put products inside your cart:")
         else:
             order=Order( self.shopping_cart.products)
             order.display_order()
class  Order:
    def __init__(self,products=[]):
        self.products=products
    def display_order(self):
        
        print("the details:")
        res= 0
        for product in self.products:
            product.display_details()
            res += product.price * product.quantity
        print("res")
class DiscountedProduct(product):
    def __init__(self,name=str(),price=float(),quantity=int(),percent_disc=float()):
        super().__init__(name,price,quantity)
        self.percent_disc=percent_disc
    def display_details(self):
        super().display_details()
        print(f"{self.percent_disc}")
if __name__ == "__main__":
    p1=product("calculator",70,1)

    u1 = User("mia", "mia@gmail.com")
    u1.shopping_cart.add_product(p1)
    u1.checkout()
    
    p2 = DiscountedProduct("pencil", 22,15 ,5.0)
    u2= User("ali","ali@gmail.com")
   
    u2.shopping_cart.add_product(p2)

    u2.view_cart()