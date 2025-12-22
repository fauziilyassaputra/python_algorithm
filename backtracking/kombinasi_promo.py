daftar_promo = [
    {
        "id": "P001",
        "nama": "Promo Weekend Hemat",
        "tipe_syarat": "weekend",       # Syarat khusus
        "kategori": "all",              # Berlaku semua kategori
        "min_pembelian": 50000,
        "diskon_nominal": 10000,
        "diskon_persen": 0
    },
    {
        "id": "P002",
        "nama": "Promo Weekend Ceria",
        "tipe_syarat": "weekend",       # Konflik dengan P001 (sama-sama weekend)
        "kategori": "all",
        "min_pembelian": 20000,
        "diskon_nominal": 5000,
        "diskon_persen": 0
    },
    {
        "id": "P003",
        "nama": "Diskon Pengguna Baru",
        "tipe_syarat": "new_user",
        "kategori": "all",
        "min_pembelian": 0,
        "diskon_nominal": 0,
        "diskon_persen": 10             # Diskon berupa persen
    },
    {
        "id": "P004",
        "nama": "Potongan Fast Food",
        "tipe_syarat": "kategori_spesifik",
        "kategori": "fast_food",        # Harus match dengan item di keranjang
        "min_pembelian": 40000,
        "diskon_nominal": 15000,
        "diskon_persen": 0
    },
    {
        "id": "P005",
        "nama": "Diskon Elektronik",
        "tipe_syarat": "kategori_spesifik",
        "kategori": "elektronik",       # Ini harusnya TIDAK valid (salah kategori)
        "min_pembelian": 100000,
        "diskon_nominal": 50000,
        "diskon_persen": 0
    },
    {
        "id": "P006",
        "nama": "Diskon Gede-Gedean",
        "tipe_syarat": "spesial",
        "kategori": "all",
        "min_pembelian": 10000,
        "diskon_nominal": 60000,        # Sangat besar (untuk tes limit 50% total belanja)
        "diskon_persen": 0
    }
]



def validation(gabungan_sementara, data_keranjang,promo_sekarang, hari, status_user):
    # validasi tipe promo
    if promo_sekarang['kategori'] != 'all':
        if promo_sekarang['kategori'] not in data_keranjang['kategori']:
            return False

    # validasi minimum pembelian
    if data_keranjang['total'] < promo_sekarang['min_pembelian']:
        return False

    # validasi hari
    if promo_sekarang['tipe_syarat'] == 'weekend' and hari != 'weekend':
        return False
    
    # validasi status user
    if promo_sekarang['tipe_syarat'] == 'new_user' and status_user != 'new_user':
        return False
    
    # validasi jangan ada 2 tipe yang sama
    for p in gabungan_sementara:
        if p['tipe_syarat'] == promo_sekarang['tipe_syarat']:
            return False
    
    return True


def hitung_total_diskon(gabungan_sementara, total_belanja):
    total_potongan = 0
    for p in gabungan_sementara:
        if p['diskon_nominal'] > 0:
            total_potongan += p['diskon_nominal']
        elif p['diskon_persen'] > 0:
            total_potongan += (p['diskon_persen'] / 100) * total_belanja
    return total_potongan

def kombinasi_promo(daftar_promo, gabungan_sementara, index_sementara,status_user, data_keranjang,hari, hasil):
    # base case
    if len(gabungan_sementara) > 0:
        potongan = hitung_total_diskon(gabungan_sementara,data_keranjang['total'])
        max_potongan = data_keranjang['total'] * 0.5

        if potongan <= max_potongan:
            hasil.append({
                'kombinasi': list(gabungan_sementara),
                'total_hemat': potongan
            })

    #
    if len(gabungan_sementara) == 2:
        return

    # 
    start_index = 0
    if index_sementara:
        start_index = max(index_sementara) + 1

    for i in range(start_index,len(daftar_promo)):
        promo_sekarang = daftar_promo[i]
        if validation(gabungan_sementara, data_keranjang,promo_sekarang, hari, status_user):
        #
            gabungan_sementara.append(daftar_promo[i])
            index_sementara.add(i)
            #
            kombinasi_promo(daftar_promo, gabungan_sementara, index_sementara,status_user,data_keranjang,hari, hasil)
            #
            gabungan_sementara.pop()
            index_sementara.remove(i)

hari = 'weekend'
data_keranjang = {'total':80000, 'kategori': 'fast_food', 'item': 'minuman'}
status_user = 'new_user'
hasil = []

kombinasi_promo( daftar_promo, [], set(), status_user,data_keranjang, hari,hasil)

# --- TAHAP 1: URUTKAN HASIL (Diskon Terbesar ke Terkecil) ---
# key=lambda x: x['total_hemat'] artinya kita mengurutkan berdasarkan angka hematnya
hasil.sort(key=lambda x: x['total_hemat'], reverse=True)

# --- TAHAP 2: TAMPILKAN DENGAN FORMAT TABEL ---
print("\n" + "="*75)
print(f"{'NO':<4} | {'KOMBINASI PROMO YANG DIPILIH':<45} | {'HEMAT (Rp)':>12}")
print("-" * 75)

if not hasil:
    print(f"{'-':<4} | {'Tidak ada kombinasi promo yang valid':<45} | {'-':>12}")
else:
    for i, data in enumerate(hasil):
       # Kita ambil ['nama'] dari setiap item p yang ada di list
        nama_kombinasi = " + ".join([p['nama'] for p in data['kombinasi']])
        
        # Format angka menjadi format ribuan (contoh: 15000 jadi 15.000)
        nominal_rupiah = f"{int(data['total_hemat']):,}".replace(",", ".")
        
        # Print baris per baris
        # :<4 artinya rata kiri lebar 4 karakter
        # :>12 artinya rata kanan lebar 12 karakter (biar angkanya lurus)
        print(f"{i+1:<4} | {nama_kombinasi:<45} | Rp {nominal_rupiah:>9}")

print("="*75)

    
