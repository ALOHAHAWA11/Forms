import logging

import pymongo
from config import MONGO_ADDRESS, DATABASE_NAME, COLLECTION_NAME


class DatabaseHandler:
    __slots__ = ('__client', '__forms_db', '__forms_collection')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseHandler, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__client = pymongo.MongoClient(MONGO_ADDRESS)
        self.__forms_db = self.__client[DATABASE_NAME]
        self.__forms_collection = self.__forms_db[COLLECTION_NAME]

    @property
    def forms_collection(self):
        return self.__forms_collection

    def insert_primary_data(self):
        self.forms_collection.insert_many([{
            'form_name': "OrderForm",
            'customer_phone': "phone",
            'seller_phone': "phone",
            'delivery_date': "date",
            'order_date': "date",
            'commentary': "text"
        },
            {
                'form_name': "FeedbackForm",
                'user_email': "email",
                'message': "text"
            },
            {
                'form_name': "BasicForm",
                'date': "date",
                'email': "email",
                'phone': "phone",
                'text': "text"
            },
            {
                'form_name': "RequestForm",
                'requester_phone': "phone",
                'requester_email': "email"
            },
            {
                'form_name': "CallForm",
                'caller': "phone"
            },
            {
                'form_name': "SecondCallForm",
                'caller': "phone"
            }]
        )

    def delete_primary_data(self):
        self.forms_collection.delete_many({})

    def find_matches(self, data_with_type: dict, data_list: list, data_with_no_types: dict):
        self.insert_primary_data()
        docs = self.forms_collection.find({'$or': data_list})
        matched_forms = list()
        form_pattern = dict()
        for doc in docs:
            sliced_doc = doc.copy()
            sliced_doc.pop('_id')
            sliced_doc.pop('form_name')
            if set(sliced_doc.keys()).issubset(set(data_with_no_types)):
                matched_forms.append(doc['form_name'])
                logging.info('There is matched form!')
        if len(matched_forms) == 0:
            for field_name, field_type in data_with_type.items():
                form_pattern.update({field_name: field_type[1]})
            logging.info('Generate new pattern')
            return form_pattern
        return matched_forms
