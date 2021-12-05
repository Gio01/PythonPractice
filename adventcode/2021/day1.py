def main(val):
    prev = val[0]
    #print(prev)
    increase_ct = 0
    for i, v in enumerate(val): 
        #print(prev_low)
        #print(v)
        if (int(v) > int(prev)):
            increase_ct += 1
        prev = v
    #print(increase_ct)
    return increase_ct
    

if __name__ == '__main__':
    
    inv = open('./day1in.txt', 'r')  
    values = []
    for l in inv:
        l = l.strip('\n')
        values.append(l)
    #print(values)
    print(main(values))