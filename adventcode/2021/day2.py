def main(key, val):
    forward = 0
    vertical = 0

    for i, v in enumerate(key):
        if v == 'forward': #horizontal
            forward += int(val[i])
            print(int(val[i]))
        elif v == 'down':
            vertical += int(val[i])
        elif v == 'up': #up
            vertical -= int(val[i])
    
    return (forward * vertical)

    

if __name__ == '__main__':

    f = open('./day2in.txt', 'r')
    value = []
    for l in f:
        value.append(l.strip('\n'))
    
    #print("Value: ", value)
    keys = []
    val = []
    for i in value:
        #print(i)
        keys.append(i.split(' ')[0])
        val.append(i.split(' ')[1])
        #print(keys)
        #print(val)
    
        
    print(main(keys, val))