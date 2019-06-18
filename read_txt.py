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