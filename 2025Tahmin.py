netlr = []
neetler = []
def use_2023(netler):
    stds = '7.665 3.291 2.773 2.790'.split()
    ort = '6.904 2.176 1.483 1.887'.split()
    z = []
    sm = 0
    for i in range(4):
        stds[i] = float(stds[i])
        ort[i] = float(ort[i])
        netler[i] = float(netler[i])

    m = 0

    for i in range(4):
        if i == 0:
            m = 40
        elif i == 2 or i == 3:
            m = 13
        else:
            m = 14
        z.append((netler[i]-ort[i])/stds[i])
        sm += m*(netler[i]-ort[i])/stds[i]

    k = 400 / sm
    smm = 0

    for i in range(4):
        smm += netler[i]*k*z[i]

    return smm + 100
def use_2021(netler):
    stds = '7.752 4.210 5.595 4.097'.split()
    ort = '20.404 8.340 7.117 6.212'.split()
    z = []
    sm = 0
    for i in range(4):
        stds[i] = float(stds[i])
        ort[i] = float(ort[i])
        netler[i] = float(netler[i])

    m = 0

    for i in range(4):
        if i % 2 == 0:
            m = 40
        else:
            m = 20
        z.append((netler[i]-ort[i])/stds[i])
        sm += m*(netler[i]-ort[i])/stds[i]

    k = 400 / sm
    smm = 0

    for i in range(4):
        smm += netler[i]*k*z[i]

    return smm + 100

neetler.append(input('TYT türkçe netiniz: '))
neetler.append(input('TYT sosyal netiniz: '))
neetler.append(input('TYT matematik netiniz: '))
neetler.append(input('TYT fen netiniz: '))

netlr.append(input('AYT matematik netiniz: '))
netlr.append(input('AYT fizik netiniz: '))
netlr.append(input('AYT kimya netiniz: '))
netlr.append(input('AYT biyoloji netiniz: '))

obp = input("100 üzerinden OBP'niz: ")

t_p = ((use_2023(netlr)*6/10 + use_2021(neetler)*4/10 + float(obp)*6/10)*1.008*1000//1) / 1000
if t_p > 560:
    t_p = 560

print('2024 sıralamasında ' , t_p ,' puanına göre yerleşeceğiniz sıra yaklaşık sıranızdır')

input('Press enter to close the window')
