import json
from .atri import Atri
from fastapi import Request, Response

import urllib.parse







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




def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    f = open('products.json')
    data = json.load(f)
    set_products_data(at, data)
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    
    pass