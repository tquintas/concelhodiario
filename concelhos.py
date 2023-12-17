import unidecode as _u
import random2 as _r
from doomsday import nextDay
import matplotlib.image as _img

mes="""
        name:"{}",
        code:"{:04d}",
        lat:{},
        long:{},
        area:{},
        population:{},
        site:"{}",
        district:"{}",
        parish:"{}",
        nuts3:"{}",
        nuts2:"{}",
    """
mes2="""
        edition:"{:03d}",
        date:"{}",
        answer:"{}",
    """
ls='{\n'
ld='{\n'
cds=[]
nms,nmsa=[],[]
dicofre = []
with open('/Users/tiagoquintas/Sites/concelhodiario/concelhosmetadata.csv','r') as fl:
    fl.readline()
    for lines in fl:
        f = lines.strip().split(';')
        ls+='\t'+f[2]+':{'+mes.format(f[1],int(f[0]),f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11])+'},\n'
        cds.append(f[2])
        nms.append(_u.unidecode(f[1].lower()))
        nmsa.append(f[1])
        dicofre.append(f[0])
    ls+='}'
try:
    with open('/Users/tiagoquintas/Sites/concelhodiario/conclist.txt','x') as new:
        new.write(ls)
except FileExistsError:
    pass

try:
    with open('/Users/tiagoquintas/Sites/concelhodiario/codelist.txt','x') as neww:
        neww.write(str(cds))
        neww.write('\n')
        neww.write(str(nms))
except FileExistsError:
    pass      

_r.shuffle(cds)
day = (2023,10,23)
counting=0
for c in cds:
    counting+=1
    day = nextDay(*day)
    str_date = '{:04d}-{:02d}-{:02d}'.format(*day)
    ld+='\t'+'"'+str_date+'"'+':{'+mes2.format(counting,str_date,c)+'},\n'
else:
    ld+='}'

try:
    with open('/Users/tiagoquintas/Sites/concelhodiario/datelist.txt','x') as dates:
        dates.write(ld)
except FileExistsError:
    pass

try:
    with open('/Users/tiagoquintas/Sites/concelhodiario/conclistcomacentos.txt','x') as acentos:
        acentos.write(str(nmsa))
except FileExistsError:
    pass

"""
img1 = _img.imread('/Users/tiagoquintas/Sites/cenasbraz/100x105.png')
img2 = _img.imread('/Users/tiagoquintas/Sites/cenasbraz/100x105_red.png')
img3 = _img.imread('/Users/tiagoquintas/Sites/cenasbraz/100x111.png')
img4 = _img.imread('/Users/tiagoquintas/Sites/cenasbraz/100x118.png')
img5 = _img.imread('/Users/tiagoquintas/Sites/cenasbraz/100x119.png')

for d in dicofre:
    if d=="1006" or d=="1204" or d=="1301" or d=="1318": continue
    img = _img.imread('/Users/tiagoquintas/Sites/brazoes/'+d+'.png')
    if img.shape[0]==105:
        for i in range(105):
            for j in range(100):
                if d=="0809" or d=="1208" or d=="1511":
                    if img2[i,j].any(): img[i,j]=img2[i,j]
                else:
                    if img1[i,j].any(): img[i,j]=img1[i,j]
    elif img.shape[0]==111:
        for i in range(111):
            for j in range(100):
                if img3[i,j].any(): img[i,j]=img3[i,j]
    elif img.shape[0]==118:
        for i in range(118):
            for j in range(100):
                if img4[i,j].any(): img[i,j]=img4[i,j]
    elif img.shape[0]==119:
        for i in range(119):
            for j in range(100):
                if img5[i,j].any(): img[i,j]=img5[i,j]
    _img.imsave('/Users/tiagoquintas/Sites/brazoes/'+d+'b.png',img)
"""

