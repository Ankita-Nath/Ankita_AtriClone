from .atri import Atri
from fastapi import Request, Response

import json


import urllib.parse


def set_data(at: Atri, data):
    for i in range(1, 6):
        instance: at.Flex13.__class__ = getattr(at, f'Flex13{i}')
        instance.styles.display = 'none'
    for i in range(1, int(data['rating']) + 1):
        instance: at.Flex13.__class__ = getattr(at, f'Flex13{i}')
        instance.styles.display = 'flex'
    # Comment
    instance: at.TextBox1.__class__ = getattr(at, 'TextBox78')
    instance.custom.text = instance.custom.text[0] + data['review'] + instance.custom.text[-1]

    # Review
    instance: at.TextBox1.__class__ = getattr(at, 'TextBox79')
    instance.custom.text = data['comment']

    # Place
    instance: at.TextBox1.__class__ = getattr(at, 'TextBox80')
    instance.custom.text = data['place']

    # Name
    instance: at.TextBox1.__class__ = getattr(at, 'TextBox81')
    instance.custom.text = data['name']

    # Image
    instance: at.Image74.__class__ = getattr(at, 'Image40')
    instance.custom.src = "/app-assets/" + data['image']





def set_products_data(at: Atri, data):
    for i in range(1,9):
        # Price
        instance: at.Product_Price_1.__class__ = getattr(at, f'Product_Price_{i}')
        instance.custom.text = '$ ' + data[i-1]['Price'] + ' USD'

        # Name
        instance: at.Product_Name_1.__class__ = getattr(at, f'Product_Name_{i}')
        instance.custom.text = data[i - 1]['Name']

        # About
        instance: at.Product_About_1.__class__ = getattr(at, f'Product_About_{i}')
        instance.custom.text = data[i - 1]['About']

        # Image
        instance: at.Product_Image_1.__class__ = getattr(at, f'Product_Image_{i}')
        instance.custom.src = 'app-assets/' + data[i - 1]['Image']





def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    at.TextBox142.custom.text = '1'
    fd = open('reviews.json')
    data = json.load(fd)
    at.Flex130.styles.display = 'none'
    at.Flex137.styles.display = 'none'
    set_data(at, data[0])

    pass


