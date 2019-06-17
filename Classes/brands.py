# coding : utf-8

class Brands:
    """Brand of a product"""

    def __init__(self, brands_tags):
        self.brands_tags = brands_tags

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def about_me(self):
        """Print in the terminal the brand"""
        print("Brands tags : "+self.brands_tags)