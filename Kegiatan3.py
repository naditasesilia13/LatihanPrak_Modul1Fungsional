# Fungsi ini digunakan untuk menghitung nilai akhir berdasarkan nilai UTS dan UAS
def hitung_nilai_akhir(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir

# Menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa):
    data_nilai_akhir = {} 
    for nama, nilai in data_mahasiswa.items():
        uts, uas = nilai['uts'], nilai['uas']
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Menampilkan nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Mahasiswa 1': {'uts': 80, 'uas': 75},
        'Mahasiswa 2': {'uts': 75, 'uas': 80},
        'Mahasiswa 3': {'uts': 70, 'uas': 90},
    }
  
    data_nilai_akhir = hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if _name_ == "_main_":
    main()
     
