def convert_gender(gender: str):
    gender = gender.upper()
    if gender == 'M':
        return 'MALE'
    elif gender == 'F':
        return 'FEMALE'
    else:
        return 'UNKNOWN GENDER'


