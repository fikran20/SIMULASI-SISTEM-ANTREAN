import random
import time

class Nasabah:
    def __init__(self, id_nasabah, menit_datang):
        self.id = id_nasabah
        self.menit_datang = menit_datang
        # Waktu yang dibutuhkan untuk dilayani (2 sampai 5 menit)
        self.durasi_layanan = random.randint(2, 5) 
        self.menit_mulai_dilayani = 0
        self.menit_selesai = 0

def jalankan_simulasi(durasi_simulasi=30):
    antrean = []
    riwayat_nasabah_selesai = []
    id_counter = 1
    
    # Representasi 2 Teller: menyimpan sisa waktu sibuk (0 berarti senggang)
    teller_A_sisa_waktu = 0
    teller_B_sisa_waktu = 0

    print(f"=== SIMULASI ANTREAN BANK DIMULAI ({durasi_simulasi} MENIT) ===")
    print("-" * 60)

    for menit in range(1, durasi_simulasi + 1):
        print(f"\n[Menit ke-{menit}]")

        # 1. Update status teller (kurangi sisa waktu sibuk)
        if teller_A_sisa_waktu > 0: teller_A_sisa_waktu -= 1
        if teller_B_sisa_waktu > 0: teller_B_sisa_waktu -= 1

        # 2. Simulasi kedatangan nasabah secara acak (Peluang 50%)
        if random.random() < 0.5:
            nasabah_baru = Nasabah(id_counter, menit)
            antrean.append(nasabah_baru)
            print(f" -> Nasabah #{nasabah_baru.id} datang (Butuh {nasabah_baru.durasi_layanan} menit).")
            id_counter += 1

        # 3. Proses antrean ke Teller yang kosong
        # Cek Teller A
        if teller_A_sisa_waktu == 0 and len(antrean) > 0:
            nasabah = antrean.pop(0)
            nasabah.menit_mulai_dilayani = menit
            teller_A_sisa_waktu = nasabah.durasi_layanan
            riwayat_nasabah_selesai.append(nasabah)
            print(f" ✅ Teller A mulai melayani Nasabah #{nasabah.id}")

        # Cek Teller B
        if teller_B_sisa_waktu == 0 and len(antrean) > 0:
            nasabah = antrean.pop(0)
            nasabah.menit_mulai_dilayani = menit
            teller_B_sisa_waktu = nasabah.durasi_layanan
            riwayat_nasabah_selesai.append(nasabah)
            print(f" ✅ Teller B mulai melayani Nasabah #{nasabah.id}")

        # Tampilkan status saat ini
        print(f" Status Antrean saat ini: {len(antrean)} orang menunggu.")
        time.sleep(0.5) # Jeda setengah detik agar simulasi enak ditonton

    # === ANALISIS HASIL SIMULASI ===
    print("\n" + "="*60)
    print("=== LAPORAN HASIL SIMULASI ===")
    print("="*60)  # <-- Sudah diperbaiki di sini
    
    total_nasabah = len(riwayat_nasabah_selesai)
    total_waktu_tunggu = 0
    
    for n in riwayat_nasabah_selesai:
        waktu_tunggu = n.menit_mulai_dilayani - n.menit_datang
        total_waktu_tunggu += waktu_tunggu
        
    avg_waiting_time = total_waktu_tunggu / total_nasabah if total_nasabah > 0 else 0  # <-- Sudah diperbaiki di sini

    print(f"1. Total Nasabah yang sempat masuk ke Teller: {total_nasabah} orang")
    print(f"2. Sisa Nasabah yang masih terjebak di antrean: {len(antrean)} orang")
    print(f"3. Rata-rata waktu tunggu nasabah di antrean: {avg_waiting_time:.2f} menit")

# Menjalankan program
jalankan_simulasi(30)