from abc import ABC, abstractmethod

class Entity(ABC):
    @property
    @abstractmethod
    def id_number(self):
        return 0

class Product(Entity):
    id = 0

    def __init__(self, name=None, value=0, amount=0, scale='kg'):
        self._id = Product.id
        Product.id += 1
        self._name = name or f"{self.__class__}_{self._id}"
        self._value = value
        self._amount = amount
        self._scale = scale

    @property
    def id_number(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, other):
        self._amount = other

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, other):
        self._scale = other

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._id}"

    def __str__(self):
        return f"{self._amount}{self._scale} of {self._name} valued at {self._value}"

class Inventory(Entity):
    id = 0

    def __init__(self):
        self._id = Inventory.id
        Inventory.id += 1
        self._products = {}

    def product_add(self, *args):
        def add_to_products(prod):
            try:
                self._products[prod.name].append(prod)
            except KeyError:
                self._products[prod.name] = [prod]

        for arg in args:
            if isinstance(arg, (tuple, list)):
                for prod in arg:
                    add_to_products(prod)
            elif isinstance(arg, Product):
                add_to_products(arg)

    @property
    def product_value(self):
        return sum(single.value for product in self._products for single in self._products[product])

    @property
    def product_count(self):
        return sum(1 for product in self._products for _ in self._products[product])

    @property
    def product_diff_amount(self):
        return len(self._products)

    @property
    def products(self):
        return self._products

    @property
    def id_number(self):
        return self._id

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._id}"

class ObjFactory(ABC):
    @abstractmethod
    def get_object(self):
        return 0

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._id}"

class InventoryFactory(ObjFactory):
    def get_object(self, amt=1):
        for _ in range(amt):
            yield Inventory()

class ProductFactory(ObjFactory):
    def get_object(self, amt=1):
        for _ in range(amt):
            yield Product()

if __name__ == "__main__":
    """
    Product Inventory Project – Create an application which manages an inventory of products. 
    Create a product class which has a price, id, and quantity on hand. 
    Then create an inventory class which keeps track of various products and can sum up the inventory value.
    """
    # create an inventory
    inventory = Inventory()
    # add some products to the inventory
    gen_prod = lambda value: Product(value=value)
    for i in range(1, 10):
        inventory.product_add(gen_prod(value=i))
    for i in range(1, 5):
        inventory.product_add(gen_prod(value=i))
    # Get amount of product on hand, value of product, and amount of different products
    prod_amt = inventory.product_count
    prod_val = inventory.product_value
    prod_diff = inventory.product_diff_amount
    for name, info in (("amount of product", prod_amt), ("value of product", prod_val), ("different products", prod_diff)):
        print(f"{name}: {info}")
    print(inventory.products)
    for product in inventory.products:
        print(product + " prob details: " + str(inventory.products[product]))


