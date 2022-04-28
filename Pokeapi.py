import requests

def get_poke_info(name):
    """
    Gets a dictionary of information from the PokeApi For a specified Pokemon.

    :param name: Pokemon Name
    :return: Dictionry of pokemon info ; none if unsuccessful
    """

    if name is None:
        print('Invalid: Missing Parameter')
        return
    name = name.strip().lower()
    if name == '':
        print('Invalid:Empty Parameter')
    
    poke_url = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    
    rpnse = requests.get(poke_url)
    
    if rpnse.status_code ==200:
        print('Succesful To Get Poke Info')
        return rpnse.json()
    else:
        print('Fail To Get Info')
        return

def Get_poke_list(limit=200,offset=0):
    """
    Gets a list of al poke from the PokeApi.

    :param name: limit , offset
    :return: List of 200 Pokemons ; none if unsuccessful
    """
    
    print("Getting list of Pokemon...",  end=' ' )

    poke_url = 'https://pokeapi.co/api/v2/pokemon/'

    p = {
        'offset': offset,
        'limit': limit
    }
    
    rpnse = requests.get(poke_url, data=p, params=p)
    
    if rpnse.status_code ==200:
        print('Succesful To Get Poke Info')
        poke_dict = rpnse.json()
        return [p['name'] for p in poke_dict['results']]

    else:
        print('Fail To Get Info. Response Code:', rpnse.status_code)

def get_poke_image(name):
    """
    Gets a url for the image of pokemon from the PokeApi For a specified Pokemon.

    :param name: Pokemon Name
    :return: Image Url of pokemon ; none if unsuccessful
    """
    poke_dict = get_poke_info(name)

    if poke_dict:
        poke_iUrl = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_iUrl 