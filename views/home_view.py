from . import main_view as view

def Main():
    print("============ SISTEM INFORMASI PENCATATAN KAS RKA ============")
    print("Tambah Uang Masuk")
    print("1> Tambahkan Uang Masuk (Debet)")
    print("2> Tambahkan Uang Keluar (Kredit)")
    print("3> Informasi Catatan Kas")
    menu = int(input("Masukkan Menu [1/2/3] : "))
    view.loadView(menu)