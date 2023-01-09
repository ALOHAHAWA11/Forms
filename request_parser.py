import logging

from validators import *


class RequestHandler:

    @staticmethod
    def parse_request(params: str) -> (dict, list, dict):
        parsed_data = dict()
        parsed_data_list = list()
        parsed_with_no_type = dict()
        fields = params.split('&')
        logging.info('Validate data')
        for param in fields:
            param = param.split('=')
            name_field, data = param[0], param[1]
            if validated_data := Validators.validate_usual_date(data):
                parsed_data.update({name_field: validated_data})
                parsed_with_no_type.update({name_field: {'$exists': True}})
                parsed_data_list.append({name_field: {'$exists': True}})
            elif validated_data := Validators.validate_unusual_date(data):
                parsed_data.update({name_field: validated_data})
                parsed_with_no_type.update({name_field: {'$exists': True}})
                parsed_data_list.append({name_field: {'$exists': True}})
            elif validated_data := Validators.validate_phone_number(data):
                parsed_data.update({name_field: validated_data})
                parsed_with_no_type.update({name_field: {'$exists': True}})
                parsed_data_list.append({name_field: {'$exists': True}})
            elif validated_data := Validators.validate_email(data):
                parsed_data.update({name_field: validated_data})
                parsed_with_no_type.update({name_field: {'$exists': True}})
                parsed_data_list.append({name_field: {'$exists': True}})
            else:
                parsed_data.update({name_field: (data, FieldType.TEXT.value)})
                parsed_with_no_type.update({name_field: {'$exists': True}})
                parsed_data_list.append({name_field: {'$exists': True}})
        return parsed_data, parsed_data_list, parsed_with_no_type
