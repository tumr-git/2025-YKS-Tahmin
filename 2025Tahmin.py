import tkinter as tk
from tkinter import ttk

def x(netlr, neetler): #ayt tyt

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
            z.append((netler[i] - ort[i]) / stds[i])
            sm += m * (netler[i] - ort[i]) / stds[i]

        k = 400 / sm
        smm = 0

        for i in range(4):
            smm += netler[i] * k * z[i]

        return smm + 100

    def use_2021(netler):
        stds = '7.752 4.210 5.595 4.097'.split()
        ort = '20.404 8.340 6.117 6.212'.split()
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
            z.append((netler[i] - ort[i]) / stds[i])
            sm += m * (netler[i] - ort[i]) / stds[i]

        k = 400 / sm
        smm = 0

        for i in range(4):
            smm += netler[i] * k * z[i]

        return smm + 100

    t_p = ((use_2023(netlr) * 6 / 10 + use_2021(neetler) * 4 / 10) * 1.008 * 1000 // 1) / 1000
    if t_p > 560:
        t_p = 560

    return t_p

# Pencereyi ortala
def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    win.geometry(f'{width}x{height}+{x}+{y}')


# Ana pencere
root = tk.Tk()
root.title("2025 YKS Net Giriş Ekranı")
center_window(root, 480, 550)

# Başlık
title_label = ttk.Label(root, text="Netlerinizi Girin", font=("Helvetica", 16))
title_label.pack(pady=20)

# TYT ve AYT etiketleri ve giriş isimleri
tyt_labels = [
    "TYT Türkçe Neti",
    "TYT Sosyal Neti",
    "TYT Matematik Neti",
    "TYT Fen Neti"
]

ayt_labels = [
    "AYT Matematik Neti",
    "AYT Fizik Neti",
    "AYT Kimya Neti",
    "AYT Biyoloji Neti",
    "OBP(100 üzerinden)"
]
entries = {}

# TYT girişleri
for label in tyt_labels:
    frame = ttk.Frame(root)
    frame.pack(pady=3)
    ttk.Label(frame, text=label, width=25).pack(side="left", padx=5)
    entry = ttk.Entry(frame, width=10)
    entry.pack(side="left")
    entries[label] = entry

# AYT girişleri
for label in ayt_labels:
    frame = ttk.Frame(root)
    frame.pack(pady=3)
    ttk.Label(frame, text=label, width=25).pack(side="left", padx=5)
    entry = ttk.Entry(frame, width=10)
    entry.pack(side="left")
    entries[label] = entry

# Bilgi yazısı
output_label = ttk.Label(root, text="", font=("Helvetica", 12))
output_label.pack(pady=15)

# Gönder butonu işlevi
def submit():
    try:
        l = [entries[label].get() for label in tyt_labels]
        m = [entries[label].get() for label in ayt_labels]

        print("TYT Netleri (l):", l)
        print("AYT Netleri (m):", m)
        outp = str(x(m,l) + float(entries[ayt_labels[4]].get())*6/10)
        output_label.config(text='2024 sıralamasında ' + outp + ' puanına göre yerleşeceğiniz sıra yaklaşık sıranızdır')
    except ValueError:
        print(ValueError)
        output_label.config(text="Lütfen tüm alanlara sayı girin!")


# Gönder butonu
ttk.Button(root, text="Gönder", command=submit).pack(pady=10)

root.mainloop()
