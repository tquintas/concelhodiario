import requests
import matplotlib.image as _img
import numpy as _n
arpop=[]
distri = ['Aveiro','Beja','Braga','Bragança','Castelo Branco','Coimbra','Évora','Faro','Guarda','Leiria','Lisboa','Portalegre','Porto','Santarém','Setúbal','Viana do Castelo','Vila Real','Viseu']
Norte=['Alto Minho','Cávado','Ave','Área Metropolitana do Porto','Alto Tâmega','Tâmega e Sousa','Douro','Terras de Trás-os-Montes']
Algarve='Algarve'
Centro=['Oeste','Região de Aveiro','Região de Coimbra','Região de Leiria','Viseu Dão-Lafões','Beira Baixa','Médio Tejo','Beiras e Serra da Estrela']
Lisboa='Área Metropolitana de Lisboa'
Alentejo=['Alentejo Litoral','Baixo Alentejo','Lezíria do Tejo','Alto Alentejo','Alentejo Central']
with open('/Users/tiagoquintas/Sites/concelhodiario/concelhos-sites.csv','r') as fl:
    fl.readline()
    for lines in fl:
        link = lines.strip().split(';')[-2]
        name = lines.strip().split(';')[2]
        code = lines.strip().split(';')[4]
        dis = distri[int(lines.strip().split(';')[1][:2])-1]
        f = requests.get(link)
        l = f.text.split('\n')
        arpop.append(name)
        arpop.append(';')
        arpop.append(dis)
        arpop.append(';')
        reg=''
        regg=''
        area=''
        pop=''
        site=''
        imagem=''
        freg=''
        for i in l:
            """
            if 'title="Quilómetro quadrado"' in i:
                area = (i[4:i.index('<a href')].strip()).replace('&#160;','').replace(',','.')
                arpop.append(area)
                arpop.append(';')
            if 'title="População residente"' in i:
                pop = (i[4:i.index('<a href')].strip()).replace('&#160;','').replace(',','.')
                arpop.append(pop)
                arpop.append(';')
            
            if 'title="Sítio eletrónico"' in i:
                try:
                    site = l[l.index(i)+2]
                    site = site[site.index('href="')+6:site.index('">www')]
                    arpop.append(site)
                except:
                    try:
                        site = site[site.index('href="')+6:site.index('">http')]
                        arpop.append(site)
                    except:
                        try:
                            site = site[site.index('href="')+6:site.index('">M')]
                            arpop.append(site)
                        except:
                            site=''
                            continue
            
            if 'alt="Localização de' in i:
                try:
                    imagem = 'http:'+i[i.index('1.5x, //')+6:i.index(' 2x"')]
                    arpop.append(imagem)
                except:
                    pass
                arpop.append(';')
            """
            if 'title="Freguesia">' in i:
                try:
                    freg=int(l[l.index(i)+2][4:])
                    arpop.append(str(freg))
                    arpop.append(';')
                except:
                    arpop.append(';')
            if '>NUTS III<' in i:
                try:
                    reg=l[l.index(i)+2]
                    reg=reg[reg.index('">')+2:reg.index('</a>')]
                    arpop.append(reg)
                    arpop.append(';')
                    if reg in Norte:
                        regg='Norte'
                    elif reg in Centro:
                        regg='Centro'
                    elif reg in Alentejo:
                        regg='Alentejo'
                    elif reg==Lisboa:
                        regg=Lisboa
                    elif reg==Algarve:
                        regg=Algarve
                    else:
                        regg=''
                    arpop.append(regg)
                    arpop.append(';')
                except:
                    arpop.append(';')
                    arpop.append(';')
        print(name,freg,dis,reg,regg)
        arpop.append('\n')
arpop=''.join(arpop)

with open('/Users/tiagoquintas/Sites/concelhodiario/areapopul4.csv','x') as fll:
    fll.write(arpop)
"""
with open('/Users/tiagoquintas/Sites/concelhodiario/areapopul.csv','r') as f:
    for lines in f:
        code = lines.strip().split(';')[0]
        url = lines.strip().split(';')[2]
        image = requests.get(url).content
        with open('/Users/tiagoquintas/Sites/concelhodiario/locais/'+code+'a.png','wb') as png:
            png.write(image)
        img = _img.imread('/Users/tiagoquintas/Sites/concelhodiario/locais/'+code+'a.png')
        imgb = _n.copy(img)
        x,y,z = img.shape
        q = lambda i: round(i/255,3)
        for ii in range(x):
            for jj in range(y):
                if (q(245)<=img[ii,jj][0]<=q(255) 
                and q(230)<=img[ii,jj][1]<=q(240)
                and q(200)<=img[ii,jj][2]<=q(215)):
                    img[ii,jj]=[q(250), q(235), q(215), 1.]
                    imgb[ii,jj]=[q(21), q(21), q(21), 1.]
                elif (q(150)<=img[ii,jj][0]
                and q(5)<=img[ii,jj][1]<=q(50)
                and q(5)<=img[ii,jj][2]<=q(50)):
                    img[ii,jj]=[1., 0., 0., 1.]
                    imgb[ii,jj]=[1., 0., 0., 1.]
                else:
                    img[ii,jj]=[0., 0., 0., 0.]
                    imgb[ii,jj]=[0., 0., 0., 0.]
                if ((ii>=x-240 and jj<=192)
                or (jj==273 and ii==223)
                or (jj==308 and ii==392)
                or (jj==256 and ii==469)
                or (jj==375 and ii==480)
                or (388<=jj<=389 and ii==508)
                or (jj==196 and ii==504)
                or (jj==210 and ii==497)
                or (jj==334 and ii==544)):
                    img[ii,jj]=[0., 0., 0., 0.]
                    imgb[ii,jj]=[0., 0., 0., 0.]
        _img.imsave('/Users/tiagoquintas/Sites/concelhodiario/locais/'+code+'.png',img)
        _img.imsave('/Users/tiagoquintas/Sites/concelhodiario/locais/'+code+'b.png',imgb)
"""
print('Done')
