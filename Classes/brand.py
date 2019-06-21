# coding : utf-8

class Brand:
    """Brand of a product
    self.brands_tags : name of the brand (str)"""

    def __init__(self, brands_tags):

        self.brands_tags = brands_tags

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print in the terminal the brand"""

        print("Brands tags : "+self.brands_tags)



    def find_duplicates_in_list(self, list_brands):
        """Find if the brands already exists in a list"""

        for brand in list_brands:
            if self.is_equal(brand):
                list_brands.remove(brand)



    def is_equal(self, other_brands):
        """Test if this brand is equal to an other brand in the list.
        Return True if equal, else it returns False
        other_brands : Brands Object"""

        if self.brands_tags == other_brands.brands_tags:
            return True
        else:
            return False  