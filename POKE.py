import requests

def get_poke_info(name):

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

def get_poke_img_url(name):
    poke_dict = get_poke_info(name)
    if poke_dict:
        return poke_dict['sprites']['other']['official-artwork']['front_default']

def get_poke_list(limit=100, offset=0):
    url = 'https://pokeapi.co/api/v2/pokemon/'

    params ={
        'limit' : limit,
        'offset': offset
    }
    rpnse_msg = requests.get(url, params=params)

    if rpnse_msg.status_code == 200:
        rpnse_dict = rpnse_msg.json()
        return [p['name']for p in rpnse_dict['results']]
    else:
        print('Failed')
        print('Response Code', rpnse_msg.status_code)
        print(rpnse_msg.text)
