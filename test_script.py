import requests

test_sample = {
    'param1': {"customer_phone": "+78671234567",
               "seller_phone": "+73459874309",
               "delivery_date": "09.01.2023",
               "order_date": "2023-09-01",
               "commentary": "Best wishes!"},  # Params for full match
    'param2': {"caller": "+73459874567"},  # Params for double matching
    'param3': {"different_customer_phone": "+78889925477",
               "seller_phone": "+73451238566",
               "delivery_date": "09.01.2023",
               "order_date": "2023-09-01",
               "commentary": "Again best wishes!"},  # Params for generate new form
    'param5': {"customer_phone": "+78671234567",
               "seller_phone": "+73459874309",
               "delivery_date": "09.01.2023",
               "order_date": "2023-09-01",
               "commentary": "Best wishes!",
               "second_commentary": "I like tomatoes",
               "third_commentary": "lolololo"}  # Matched but extended form
}

for param, key in test_sample.items():
    req = requests.post('http://127.0.0.1:5000/get_form',
                        headers={'User-Agent': 'Forms/'},
                        params=key)
    print(req.text)
