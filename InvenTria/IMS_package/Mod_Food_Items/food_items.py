#fooditem
from datetime import date
class FoodItems ():
    """Represents a single food item in the inventory."""
    def __init__(self,name, category, quantity, price,barcode,expirydate):
        '''initializing the attributes of the class '''
        self.name=name
        self.category=category
        self.quantity=quantity
        self.price=price
        self.barcode=barcode
        self.expirydate=date.isoformat(date.fromisoformat(expirydate))

    def __str__(self):
        """Provides a user-friendly string representation of the FoodItem object."""
        return f">>Name:{self.name}\n>>Category:{self.category}\n>>Quantity:{self.quantity}\n>>Price:{self.price}\n>>Barcode:{self.barcode}\n>>Expiry Date:{self.expirydate}"