# Convert calenders to desired format
def make_cal_dic(cal):
    cal_dict = {}
    for event in cal:
        cal_dict[event[0]] = True # Occupy start time
        cursor_time = event[0]
        while event[1] > cursor_time:
            cursor_time += 30
            cal_dict[cursor_time] = True
    return cal_dict


def find_spot(cal1, cal2):
    for slot in cal1:
        if cal2[slot] == False and cal1[slot] == False:
            print(slot)

if __name__ == '__main__':
    cal1 = {1: True, 2: False, 3: False, 4: True}
    cal2 = {1: False, 2: False, 3: False, 4: True}
    print(find_spot(cal1, cal2))