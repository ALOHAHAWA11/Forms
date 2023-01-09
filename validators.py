import re
from const import PATTERNS, FieldType


class Validators:

    @staticmethod
    def validate_usual_date(expression):
        if re.match(PATTERNS['date_pattern_usual'], expression):
            return expression, FieldType.USUAL_DATE.value
        else:
            return None

    @staticmethod
    def validate_unusual_date(expression):
        if re.match(PATTERNS['date_pattern_unusual'], expression):
            return expression, FieldType.UNUSUAL_DATE.value
        else:
            return None

    @staticmethod
    def validate_phone_number(expression):
        if re.match(PATTERNS['phone_pattern'], expression):
            return expression, FieldType.PHONE_NUMBER.value
        else:
            return None

    @staticmethod
    def validate_email(expression):
        if re.match(PATTERNS['email_pattern'], expression):
            return expression, FieldType.EMAIL.value
        else:
            return None
