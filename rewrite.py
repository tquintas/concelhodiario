import requests
latlong=[]
with open('concelhos_metadata.csv','r') as fl:
    fl.readline()
    for lines in fl:
        link = lines.strip().split(';')[-2]
        name = lines.strip().split(';')[2]
        f = requests.get(link)
        l = f.text.split('\n')
        latlong.append(name)
        latlong.append(',')
        for i in l:
            if 'id="coordinates"' in i:
                new_link = i[i.rindex('href=')+6:i.index('>',i.rindex('href='))-1]
                new_link = new_link.replace('&amp;','&')
                new_f = requests.get(new_link)
                new_l = new_f.text
                val = new_l[new_l.index('>geo:')+5:new_l.index('<',new_l.index('>geo:'))]
                latlong.append(val)
        print(name,val)
        latlong.append('\n')
latlong=''.join(latlong)

with open('coords.csv','x') as fll:
    fll.write(latlong)

print('Done')
