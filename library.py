import requests
import ctypes


def set_desk_bg_img(img_path):
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path , 0)



def download_image_from_url(img_url, img_path):
    """
    Downloading a picture for the specified pokemon.

    :param name1: Image URl
    :param name2: Image Path 
    :return: Getting url of the pokemon image and saving it on path; None if unsuccessful
    """

    print('Downloading image from URL...', end=' ')

    img_rpnse_msg = requests.get(img_url)

    if img_rpnse_msg.status_code ==200:
        print('Succesful To Get Poke Info')
        with open(img_path, 'wb') as file:
            file.write(img_rpnse_msg.content)
        print('Succesful To Get Poke Info')
    else:
        print('Fail To Get Info. Response Code:', img_rpnse_msg.status_code)


    