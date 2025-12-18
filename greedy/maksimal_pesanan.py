# Jebakan: Pesanan ID 2 durasinya cuma 2 jam (4-6), sangat pendek.
# Tapi kalau diambil, dia memblokir ID 1 (selesai jam 5) dan ID 3 (mulai jam 5).
input_trap_1 = [
    (1, 1, 5),   # Ambil ini (selesai jam 5)
    (2, 4, 6),   # JANGAN ambil ini (meski pendek, dia bikin crash jadwal)
    (3, 5, 10)   # Ambil ini (mulai pas jam 5)
]
# Jebakan: ID 1 mulai paling pagi (jam 0), tapi selesainya lamaaaa banget (jam 10).
input_trap_2 = [
    (1, 0, 10),  # Mulai 0, tapi memblokir semuanya
    (2, 1, 3),   # Selesai cepat -> Prioritas 1
    (3, 3, 5),   # Bisa diambil setelah no 2 -> Prioritas 2
    (4, 5, 9)    # Bisa diambil setelah no 3 -> Prioritas 3
]

# Jebakan: Semuanya "bersentuhan" waktunya.
input_trap_3 = [
    (1, 0, 2),
    (2, 2, 4),  # Mulai tepat saat ID 1 selesai
    (3, 4, 6),  # Mulai tepat saat ID 2 selesai
    (4, 6, 8)   # Mulai tepat saat ID 3 selesai
]

def urus_pesanan(database):
    # urutkan ke yang paling cepat selesai
    database.sort(key=lambda x: x[2]) 

    # waktu sekarang
    waktu_sekarang = 0
    daftar_pesanan = []

    for x in database:
        if x[1] >= waktu_sekarang:
            waktu_sekarang = x[2]
            daftar_pesanan.append(x[0])

    print(len(daftar_pesanan))
    hasil = [x for x in daftar_pesanan]
    print(f'id pesanan yang berhasil diantar : {hasil}')
    

urus_pesanan(database)
