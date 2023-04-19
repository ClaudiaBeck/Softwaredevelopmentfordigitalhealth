### Mock database ###
def search_database(user_ID, password):
    '''This method iterates through the dictionary and searches if the string exists in the dictionary and that the corresponding key/password matches'''
    mock_database = {"Dentist1": "adm1", "Dentist2": "adm2", "Dentist3": "adm3"}
    if user_ID in mock_database and password == mock_database[user_ID]:
        return True
    else:
        return False

# Patient example #
patient_name = "Claudia Beck"
patient_CPR = "180296-1010"
patient_address = "Sølvgade 21, 1.mf., København"
patient_phone = "50 50 70 70"
# For the sake of the example we have created above patient to show what the system should prompt to the user of information upon successful search.