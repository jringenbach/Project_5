# coding : utf-8



class Store:
    """Defines the store where we can find the products
    
    store_name : name of the store (str)"""


    def __init__(self, store_name):
        self.store_name = store_name


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


    def about_me(self):
        """Print in the terminal information about this store"""

        print("Store name : "+self.store_name)



    def is_equal(self, other_store):
        """Test equality between this store and an other store. Return True if equals, False else
        
        other_store : Store Object"""

        #If the name of the stores are the same
        if self.store_name == other_store.store_name:
            return True
        else:
            return False
