def loadcsv(filename: str):
    from __init__ import readfile
    src = readfile(filename).splitlines()
    lines = src[1:]
    try:
        titles = ''.join(src[0]).split(',')
    except:
        return {}
    df = {}
    frame = []
    current_index = 0
    for title in titles:
        for line in lines:
            try:
                frame += [line.split(',')[current_index]]
            except:
                continue
        if title == '':
            pass
        else:
            df[title] = frame
        frame = []
        current_index += 1
    return df


def load_test():
    return loadcsv('df.csv')


def writecsv(filename: str, contents: list):
    from __init__ import writefile
    new = ''
    for row in contents:
        for col in row:
            new += str(col) + ','
        new += '\n'
    writefile(filename, new)
    
    
def predict(csv_filename: str):
    returns, csvdict = [], loadcsv(csv_filename)
    for key in csvdict:
        for item in csvdict[key]:
            try:
                returns.append(int(item))
            except:
                try:
                    returns.append(float(item))
                except:
                    returns.append(len(item))
    return {'Positive': max(returns), 'Negitive': min(returns)}
