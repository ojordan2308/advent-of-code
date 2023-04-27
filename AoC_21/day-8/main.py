def contains(a, b):
    if len(a) >= len(b):
        for char in b:
            if char not in a:
                return False
        return True
    
    for char in a:
        if char not in b:
            return False
    return True

def difference(a, b):
    result = ''

    if len(a) >= len(b):
        for char in a:
            if char not in b:
                result += char
        return result

    for char in b:
        if char not in a:
            result += char
    return result

def join(a, b):
    return ''.join(set([char for char in a]+[char for char in b]))

def decode(codes):
    decoder = {}
    encoder = {}
    for code in codes:
        if len(code)==2:
            decoder[code] = 1
            encoder[1] = code
        if len(code)==4:
            decoder[code] = 4
            encoder[4] = code
        if len(code)==3:
            decoder[code] = 7
            encoder[7] = code
        if len(code)==7:
            decoder[code] = 8
            encoder[8] = code
    for code in codes:
        if code not in decoder:
            if len(code) == 5 and contains(code, encoder[1]):
                decoder[code] = 3
                encoder[3] = code
            if len(code) == 6 and not contains(code, encoder[1]):
                decoder[code] = 6
                encoder[6] = code
    for code in codes:
        if code not in decoder:
            if len(code) == 5 and not contains(code, difference(encoder[8], encoder[6])):
                decoder[code] = 5
                encoder[5] = code
                break
    for code in codes:
        if code not in decoder:
            if len(code) == 5:
                decoder[code] = 2
                encoder[2] = code
            if contains(code, join(encoder[5], encoder[1])):
                decoder[code] = 9
                encoder[9] = code
    for code in codes:
        if code not in decoder:
            decoder[code] = 0
            encoder[0] = code
    return {''.join(sorted(code)): value for (code, value) in decoder.items()}

        

if __name__ == "__main__":

    #part1_total = 0
    part2_total = 0
    with open('./input.txt') as input:
        for line in input:
            line = line.rstrip('\n')
            input_codes, output_codes = [list(map(lambda x: x.strip(), line.split('|')[i].split()))
                                        for i in range(2)]
            decoder = decode(input_codes)
            num = ''
            for code in output_codes:
                num += str(decoder[''.join(sorted(code))])
            part2_total += int(num)
            #for code in ouput_codes:
                #if len(code) in (2, 3, 4, 7):
                    #part1_total += 1
    #print(part1_total)
    print(part2_total)

   

