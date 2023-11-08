from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    ls=[]
     
    for i in data["messages"]:
        if "actor" in i and i['actor'] not in ls and "Python" not in i['actor'] and 'Codeschooluz' not in i['actor']:
            ls.append(i['actor'])
        elif "from" in i and i['from'] not in ls and "Python" not in i['from'] :
            ls.append(i['from'])
    return (ls)
print(find_all_users_name(read_data("data/result.json")))
