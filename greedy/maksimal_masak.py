input_menu = [
    ("P1", 12),
    ("P2", 5),
    ("P3", 20)
]

input_jebakan = [
    ("Pesanan_A", 100), # Masak 100 menit
    ("Pesanan_B", 50),  # Masak 50 menit
    ("Pesanan_C", 10),  # Masak 10 menit
    ("Pesanan_D", 2)    # Masak 2 menit
]
input_kilat = [
    ("Normal_1", 10),
    ("Instan_A", 0),  # Tinggal ambil
    ("Normal_2", 10),
    ("Instan_B", 0)   # Tinggal ambil
]

def maksimal_masak(seluruh_menu):
    seluruh_menu.sort(key=lambda x:x[1])

    total_waktu = 0
    waktu_tunggu = 0
    urutan_masak = []

    for menu in seluruh_menu:
        total_waktu += menu[1]
        waktu_tunggu +=  total_waktu 

        urutan_masak.append(menu[0])
    
    print(f"total waktu : {waktu_tunggu}")
    print(f"urutan masaknya {urutan_masak}")


maksimal_masak(input_kilat)
