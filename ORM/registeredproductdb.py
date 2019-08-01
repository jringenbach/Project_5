#My own libraries


#Python libraries
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
import records


class RegisteredProductDB:
    """Product the user looked a substitute for"""



    def __init__(self, barcode_product, barcode_substitute):
        self.id_registered_product = None
        self.barcode_product = barcode_product
        self.barcode_substitute = barcode_substitute



    def insert_to_database(self, db):
        """We insert this registered product into the database
        
        db : records.Connexion Object"""


        try:
            db.query("INSERT INTO RegisteredProduct (barcode_product, barcode_substitute) VALUES"\
            +"(:barcode_product, :barcode_substitute)", barcode_product = self.barcode_product,\
            barcode_substitute = self.barcode_substitute)

        except IntegrityError as int_err:
            print("This registered product is already in database.")
            print(int_err)

        except ProgrammingError as prg_err:
            print("There was a programming error while inserting registered product")
            print(prg_err)    