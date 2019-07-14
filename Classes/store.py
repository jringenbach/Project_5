# coding : utf-8



class Store:
    """Defines the store where we can find the products
    
    name_store : name of the store (str)"""


    def __init__(self, name_store):
        self.name_store = name_store


#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------


    def about_me(self):
        """Print in the terminal information about this store"""

        print("Store name : "+self.name_store)



    def is_equal(self, other_store):
        """Test equality between this store and an other store. Return True if equals, False else
        
        other_store : Store Object"""

        #If the name of the stores are the same
        if self.name_store == other_store.name_store:
            return True
        else:
            return False
