# coding : utf-8

class Brand:
    """Brand of a product
    brands_tags : name of the brand (str)"""

    def __init__(self, brand_tags):

        self.brand_tags = brand_tags

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print in the terminal the brand"""

        print("Brands tags : "+self.brand_tags)



    def find_duplicates_in_list(self, list_brands):
        """Find if the brands already exists in a list"""

        for brand in list_brands:
            if self.is_equal(brand):
                list_brands.remove(brand)



    def is_equal(self, other_brand):
        """Test if this brand is equal to an other brand in the list.
        Return True if equal, else it returns False
        other_brand : Brands Object"""

        if self.brand_tags == other_brand.brand_tags:
            return True
        else:
            return False  