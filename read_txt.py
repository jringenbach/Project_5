# coding : utf-8

def get_list_from_txt_file(file_path):
    """Read a text file and return a list of its lines
    file_path : path to the file we want to read (str)"""

    list_line = list()

    try:
        #We read the categories in categories.txt
        with open(file_path, "r", encoding="utf-8") as text_file:
            list_line = text_file.readlines()
            text_file.close()
    
    except:
        print("Couldn't open the file : "+file_path)

    finally:
        return list_line

    
def get_text_from_file(file_path):
    """Read a file and return it as a string variable
    file_path : path to the file we want to read (str)"""

    #We try to read the file
    try:
        with open(file_path, "r", encoding="utf-8") as text_file:
            file = text_file.read()
            return file

    except:
        print("Couldn't open the file : "+file_path)