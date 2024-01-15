import string
#import easyocr

# Initialize the OCR reader
#reader = easyocr.Reader(['en'], gpu=True)

dict_char_to_int = {'O': '0',
                    'I': '1',
                    'J': '3',
                    'A': '4',
                    'G': '6',
                    'S': '5'}

dict_int_to_char = {'0': 'O',
                    '1': 'I',
                    '3': 'J',
                    '4': 'A',
                    '6': 'G',
                    '5': 'S'}


def license_complies_format(text): #step 1
    """
    Check if the license plate text complies with the required format.

    Args:
        text (str): License plate text.

    Returns:
        bool: True if the license plate complies with the format, False otherwise.
    """
    if len(text) < 6:
        print('smaller than 6 chars')
        return False

    print(len(text))
    if len(text) == 6:
        if  (text[0] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys())and \
            (text[2] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
            (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
            (text[4] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
            (text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()):
                print('in license_complies_format')
                print("check len 6 OK")
                return True
        else:
            print('in license_complies_format')
            print("check len 6 NOK")
            return False
    elif len(text) == 7:
        if  (text[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
            (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
            (text[2] in string.ascii_uppercase or text[1] in dict_int_to_char.keys())and \
            (text[3] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
            (text[4] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
            (text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
            (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()):
                print('in license_complies_format')
                print("check len 7 OK")
                return True
        else:
            print('in license_complies_format')
            print("check len 7 NOK")
            return False
    else:
        print('in license_complies_format not 6 or 7 chars')
        return False


def format_license(text):
    """
    Format the license plate text by converting characters using the mapping dictionaries.

    Args:
        text (str): License plate text.

    Returns:
        str: Formatted license plate text.
    """
    print('in format_license')
    print(len(text))
    license_plate_ = ''
    if len(text) == 6:
        mapping = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_char_to_int, 5: dict_char_to_int,
                    2: dict_int_to_char, 3: dict_char_to_int}
        for j in [0, 1, 2, 3, 4, 5]:
            if text[j] in mapping[j].keys():
                license_plate_ += mapping[j][text[j]]
            else:
                license_plate_ += text[j]
    elif len(text) == 7:
        mapping = {0: dict_char_to_int, 1: dict_int_to_char, 4: dict_char_to_int, 5: dict_char_to_int,
                    2: dict_int_to_char, 3: dict_int_to_char, 6: dict_char_to_int} 
        for j in [0, 1, 2, 3, 4, 5, 6]:
            if text[j] in mapping[j].keys():
                license_plate_ += mapping[j][text[j]]
            else:
                license_plate_ += text[j]

    return license_plate_


def read_license_plate(detections):
    """
    Read the license plate text from the given cropped image.

    Args:
        license_plate_crop (PIL.Image.Image): Cropped image containing the license plate.

    Returns:
        tuple: Tuple containing the formatted license plate text and its confidence score.
    """

    #detections = reader.readtext(detections)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(' ', '')
        text.replace('-','')
        text.replace(';','')
        text.replace(':','')
        text.replace('\"','')
        text.replace('.','')
        text.replace('~','')
        text.replace(',','')
        text.replace(']','')
        text.replace('[','')

        print('in check_license_plate.py')
        print(text)
        if license_complies_format(text):
            return format_license(text), score

    return None, None