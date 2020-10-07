class NotExistsItemError(Exception):
    pass

class Item:

    def __init__(self, name, price): # atributos de producto
        self.name = name
        self.price = price

    def code(self): # adicionar codigo de producto
        return "{}-123456789".format(self.name)

    def __str__(self):
        return self.name

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item): # agregar items al carrito
        self.items.append(item)

    def remove_item(self, item): # eliminar items al carrito
        self.items.remove(item)

    def constains_items(self): # validar si contiene items dentro de carrito
        return len(self.items) > 0

    def total(self): # mostar total del carrito
        return sum([item.price for item in self.items]) 
            
    def get_item(self, item): # Mostar items del carrito
        if item not in self.items:
            raise NotExistsItemError('Items does not exists')
        else:
            return self.items[ self.items.index(item) -1 ]