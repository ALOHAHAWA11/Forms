import enum

URLS = {
    '/get_form': 'That is form',
    '/': 'some'
}

PATTERNS = {
    'date_pattern_usual': r'(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[012])\.((19|20)\d\d)',
    'date_pattern_unusual': r'\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])',
    'phone_pattern': r'\+7\d{10}',
    'email_pattern': r'\d+\@\d+\.\d{2,3}'
}


class FieldType(enum.Enum):
    USUAL_DATE = 'USUAL_DATE_TYPE'
    UNUSUAL_DATE = 'UNUSUAL_DATE_TYPE'
    PHONE_NUMBER = 'PHONE_NUMBER_TYPE'
    EMAIL = 'EMAIL_TYPE'
    TEXT = 'TEXT_TYPE'
