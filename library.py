import requests


def download_image_from_url(imp_url, path):

    print('Downloading image from URL...', end=' ')

    img_rpnse_msg = requests.get(imp_url)

    if img_rpnse_msg.status_code ==200:
        print('Succesful To Get Poke Info')
        with open('save_path', 'wb') as file:
            file.write(img_rpnse_msg.content)
        print('Succesful To Get Poke Info')
    else:
        print('Fail To Get Info. Response Code:', img_rpnse_msg.status_code)


    