<<<<<<< HEAD

class Storage():
    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.storage = []

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage

=======

class Storage():
    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.storage = []

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage

>>>>>>> 208b47ea4d0bcafc85cf570be2bfb1f6ac828c17
