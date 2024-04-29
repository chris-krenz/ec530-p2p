"""
Contains function to check for potentially malicious code.
"""


def sanitizer(message: bytes | str) -> str:
    """
    Sanitize message to ensure not malicious.  Primarily filters out SQL Queries.
    Raises exception if match is found; otherwise returns string indicating message is clean.
    The coincidental combination of these words with a ';' is relatively unlikely.
    Will be false positives, but erring on the side of safety.
    """
    message = message.decode() if type(message) == bytes else message

    # (must also contain a ';')
    restricted_sql = [['select',   'from'],
                      ['drop',     'database'],
                      ['drop',     'table'],
                      ['drop',     'index'],
                      ['update',   'set'],
                      ['delete',   'from'],
                      ['alter',    'table'],
                      ['grant',    'to'],
                      ['revoke',   'from'],
                      ['truncate', 'table'],
                      ['rollback', 'to']]

    if ';' in message:
        for keyword_set in restricted_sql:
            if all([(keyword in message.lower()) for keyword in keyword_set]):
                print('TESTING')
                raise RuntimeError('You entered illegal characters, please try again...')

    return 'Submitted message clean...'
