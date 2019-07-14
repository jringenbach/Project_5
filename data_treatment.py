#Contain methods to clean the datas from openfoodfacts


def clean_datas(openfoodfacts_dict):
    """Clean datas
    openfoodfacts_dict : dictionary that contains categories and their products (dict)"""

    print("Cleaning datas")

    for key, list_item in openfoodfacts_dict.items():
        if key != "categories":
            i = 0
            for i in range(0, len(list_item)):
                if key == "products":
                    list_item[i].product_name_fr = list_item[i].product_name_fr.replace("'", "''")
                if key == "brands":
                    list_item[i].brand_tags = list_item[i].brand_tags.replace(" ", "")
                if key == "stores":
                    list_item[i].name_store = list_item[i].name_store.replace(", ", "")
                    list_item[i].name_store = list_item[i].name_store.replace(",", "")

                i += 1
    
    return openfoodfacts_dict





def delete_wrong_character(key, list_item):
    """Delete characters that can't be inserted in database"""
    print("Deleting wrong characters from : "+key)
    for item in list_item:
        if key == "products":
            item = item.product_name_fr.replace("'", "\'")
        if key == "brands":
            item = item.brand_tags.replace("'", "\'")



def find_all_duplicates(key, list_item):
    """Find the duplicates in every object in openfoodfacts"""

    print("Cleaning datas : finding duplicates")
    for item in list_item:
        item.find_duplicates_in_list(list_item)

    print("Number of "+key+" : "+str(len(list_item)))




def get_list_of_all_objects(list_categories):
    """Get list of products, brands, nutrition_grade from the list of categories
    and return a dictionary with every list
    list_categories : list of Categorie Objects (list)"""

    list_products = list()
    list_brands = list()
    list_nutrition_grade = list()
    list_stores = list()

    #We check every categorie in the list
    for categorie in list_categories:

        #We check every product in the categorie
        for product in categorie.products:
            list_products.append(product)
            for brand in product.brands:
                list_brands.append(brand)
            for store in product.stores:
                list_stores.append(store)
            list_nutrition_grade.append(product.nutrition_grade)

        #We build a dictionary with every list
        openfoodfacts_dict = {"categories" : list_categories,
        "products" : list_products,
        "brands" : list_brands,
        "nutrition_grade" : list_nutrition_grade,
        "stores" : list_stores}

        return openfoodfacts_dict
