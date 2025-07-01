import tkinter as tk
from tkinter import ttk

def hesapla():
    try:
        frekans = float(entry.get())
        tip = tip_combobox.get()
        k = 0.95
        c = 300

        if tip == "Tam Dalga":
            L = (k * c) / frekans
        elif tip == "Yarım Dalga":
            L = (k * c) / (2 * frekans)
        elif tip == "Çeyrek Dalga":
            L = (k * c) / (4 * frekans)
        else:
            sonuc_label.config(text="Anten tipi seçin.")
            return

        uzun_kol = L * 0.67
        kisa_kol = L * 0.33

        sonuc = f"""📡 {frekans} MHz - {tip}
Toplam Uzunluk : {L:.2f} m
Uzun Kol (67%) : {uzun_kol:.2f} m
Kısa Kol (33%) : {kisa_kol:.2f} m"""
        sonuc_label.config(text=sonuc)

        # --- Çizim ---
        canvas.delete("all")
        orta_x = 150
        olcek = 20  # 1 m = 20 piksel
        u_px = int(uzun_kol * olcek)
        k_px = int(kisa_kol * olcek)
        toplam_y = u_px + k_px + 80  # boşlukla birlikte

        # Dinamik canvas yüksekliği
        canvas.config(height=toplam_y)

        y0 = toplam_y // 2

        # Uzun kol (yukarı)
        canvas.create_line(orta_x, y0, orta_x, y0 - u_px, width=5, fill="blue")
        canvas.create_text(orta_x + 60, y0 - u_px // 2, text=f"Uzun Kol\n{uzun_kol:.2f} m", fill="blue", font=("Arial", 9))

        # Balun kutusu
        canvas.create_rectangle(orta_x - 18, y0 - 10, orta_x + 18, y0 + 10, fill="orange")
        canvas.create_text(orta_x, y0, text="4:1", fill="black", font=("Arial", 9, "bold"))
        canvas.create_text(orta_x + 60, y0, text="Balun", fill="orange", font=("Arial", 9))

        # Kısa kol (aşağı)
        canvas.create_line(orta_x, y0, orta_x, y0 + k_px, width=5, fill="green")
        canvas.create_text(orta_x + 60, y0 + k_px // 2, text=f"Kısa Kol\n{kisa_kol:.2f} m", fill="green", font=("Arial", 9))

        # Koaksiyel kablo çizgisi
        canvas.create_line(orta_x - 25, y0 + 15, orta_x + 25, y0 + 15, width=2, fill="black")
        canvas.create_text(orta_x, y0 + 30, text="Koaksiyel Giriş", fill="black", font=("Arial", 8))

    except ValueError:
        sonuc_label.config(text="❌ Geçerli sayı girin.")

# Arayüz
pencere = tk.Tk()
pencere.title("OCF Dipol Hesaplayıcı (Kompakt)")
pencere.geometry("370x600")

tk.Label(pencere, text="Frekans (MHz):").pack(pady=5)
entry = tk.Entry(pencere)
entry.pack()

tk.Label(pencere, text="Anten Tipi:").pack(pady=5)
tip_combobox = ttk.Combobox(pencere, values=["Tam Dalga", "Yarım Dalga", "Çeyrek Dalga"])
tip_combobox.pack()
tip_combobox.current(1)

tk.Button(pencere, text="Hesapla", command=hesapla).pack(pady=10)

sonuc_label = tk.Label(pencere, text="", justify="left", font=("Courier", 9))
sonuc_label.pack()

canvas = tk.Canvas(pencere, width=300, height=300, bg="white", bd=2, relief="sunken")
canvas.pack(pady=10)

pencere.mainloop()
