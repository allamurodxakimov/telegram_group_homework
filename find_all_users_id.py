from read_data import read_data
def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    c={}
    b={}
    ls=[]
    for i in data['messages']:
        c[i.get("actor")]=i['id']
        ls.append(c)
        b[i.get('from')]=i['id']
        ls.append(b)
    return ls
print(find_all_users_id(read_data("data/result.json")))