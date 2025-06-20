while True:
    try:
        st = input()
        result = ''
        pre_text = None
    
        for s in st:

            #首字
            if pre_text == None:
                pre_text = s
                continue

            if (s == ' ' and pre_text == ' '):
                pre_text = '*'
            
            #print(pre_text,s)
            result += pre_text
            pre_text = s
        else:
            if s == ' ':
                result += '*'
            else:
                result += s
        if result[0] == ' ':
            result = "*" + result[1:]

        print(result)
    
    except:
        break