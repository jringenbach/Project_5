# coding : utf-8

#Python libraries
import mysql.connector
import json

class Link_DB:
    """Contains information to connect to the database"""



    def __init__(self):
        print("Initialization of Link_DB")



    def connexion_with_conf_file(self, file_path):
        """Connects a user to the database by reading its connexion information in a json configuration file.

        file_name : path and name of the json configuration file
        """

        #We open the configuration file to get the user information
        with open(file_path) as json_data:
            
                #We load the json file
                connexion_info = json.load(json_data)

                #We get the user information
                host_db = connexion_info["connexion_info"]["host"]
                database_db = connexion_info["connexion_info"]["database"]
                user_db = connexion_info["connexion_info"]["user"]
                password_db = connexion_info["connexion_info"]["password"]

                #We try to connect the user
                try:
                    connexion = mysql.connector.connect(host=host_db,database=database_db,user=user_db,password=password_db)
                    
                    #If the connexion is successful, we display a message
                    if connexion.is_connected():
                        print("User "+user_db+" has successfully connected to database : "+database_db)

                #If an error occurs during connexion, we display it
                except Error as e:
                    print(e)

                finally:
                    connexion.close()



                json_data.close()
