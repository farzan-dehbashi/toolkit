def max_area(heighs):
    l = 0
    r = len(heighs) - 1
    max_rect = {'start':0, 'end': len(heighs) - 1, 'area':0}
    while l + 1 != r:
        print(f'l={l}, r={r}, max_rec={max_rect}')
        if heighs[l+1] > heighs[l]:
            l+=1
            area = (r-l) * ((heighs[l]+heighs[r])/2)
            if area > max_rect['area']:
                max_rect['start'] = l
                max_rect['end'] = r
                max_rect['area'] = area
        elif heighs[r-1] > heighs[r]:
            r -= 1
            area = (r-l) * ((heighs[l]+heighs[r])/2)
            if area > max_rect['area']:
                max_rect['start'] = l
                max_rect['end'] = r
                max_rect['area'] = area
        else:
            if heighs[r-1] > heighs[l+1]:
                r -= 1
                area = (r-l) * ((heighs[l]+heighs[r])/2)
                if area > max_rect['area']:
                    max_rect['start'] = l
                    max_rect['end'] = r
                    max_rect['area'] = area
            else:
                l +=1
                area = (r-l) * ((heighs[l]+heighs[r])/2)
                if area > max_rect['area']:
                    max_rect['start'] = l
                    max_rect['end'] = r
                    max_rect['area'] = area

    return (max_rect)

print(max_area([1,8,6,2,5,4,8,3,7]))