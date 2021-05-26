import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
r = requests.get('https://www.ssense.com/en-us/men/product/nike/orange-overbreak-sp-sneakers/8049691',headers = headers)
print(r.status_code)

import requests
import json

url = "https://api.bigcommerce.com/stores/lkdb4vv2gy/v3/catalog/products/16790"


# payload = {
#   "name": "Nike. Orange Overbreak SP Sneaker",
#   "brand_id": 1,
#   "categories": "['Men Footware']",
#   "price": "190",
#   "description": "Supplier color: Pollen rise/Neptune green. Upper: textile, synthetic. Sole: rubber. Low-top paneled mesh and faux-suede sneakers in orange. Round rubber cap toe in black. Lace-up closure in tones of orange and grey. Textile logo patch at tongue. Padded collar. Loog printed in orange at green buffed faux-leather heel tab. Buffed faux-leather Swoosh appliqués in green at sides. Textured React® foam rubber sole in black and gradient tones of beige. Approx 2'' platform. ",
#   "sku":"211011M237224",
#   "weight": 4,
#   "type": "physical",
#   "variants": [
#     {
#       "sku": "Nike-orange-8-41",
#       "option_values": [
#         {
#           "option_display_name": "Size",
#           "label": "US-8 = IT-41"
#         }
#       ]
#     },
#     {
#       "sku": "Nike-orange-8.5-41.5",
#       "option_values": [
#         {
#           "option_display_name": "Size",
#           "label": "US-8.5 = IT-41.5"
#         }
#       ]
#     },
#     {
#       "sku": "Nike-orange-9.5-42.5",
#       "option_values": [
#         {
#           "option_display_name": "Size",
#           "label": "US-9.5 = IT-42.5"
#         }
#       ]
#     },
#     {
#       "sku": "Nike-orange-12-45",
#       "option_values": [
#         {
#           "option_display_name": "Size",
#           "label": "US-12 = IT-45"
#         }
#       ]
#     }
      
#   ],
#   "images": [{
#       "is_thumbnail": True,
#       "sort_order": 1,
#       "description": "NIKE Orage Sneaker Image 1",
#       "image_url": "https://img.ssensemedia.com/images/b_white,g_center,f_auto,q_auto:best/211011M237224_1/nike-orange-overbreak-sp-sneakers.jpg"
#      },
      
#       {
#       "is_thumbnail": False,
#       "sort_order": 2,
#       "description": "NIKE Orage Sneaker Image 1",
#       "image_url": "https://img.ssensemedia.com/images/b_white,c_lpad,g_center,h_1412,w_940/c_scale,h_960/f_auto,dpr_1.3/211011M237224_2/nike-orange-overbreak-sp-sneakers.jpg"
#      },
#       {
#       "is_thumbnail": False,
#       "sort_order": 3,
#       "description": "NIKE Orage Sneaker Image 1",
#       "image_url": "https://img.ssensemedia.com/images/b_white,c_lpad,g_center,h_1412,w_940/c_scale,h_960/f_auto,dpr_1.3/211011M237224_5/nike-orange-overbreak-sp-sneakers.jpg"
#      }
#   ]
# }
payload = {
    "name": "Nike. Orange Overbreak SP Sneker",
    "price":200
    
}

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'x-auth-token': "nw680dqzdka5sl2n5ui9ps3p1nlxana"
    }

response = requests.put(url, data=json.dumps(payload), headers=headers)

print(response.text)


