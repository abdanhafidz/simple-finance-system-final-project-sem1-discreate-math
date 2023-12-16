from . import main_view as view
from datetime import datetime 
from controller import addkredit_controller as controllerKredit

def Main():
    print("============ ADD KREDIT DATA @ SISTEM INFORMASI PENCATATAN KAS RKA ============")
    print("Tambahkan uang Keluar :")
    try:
        while(True):
            amount = int(input("Besar Uang Keluar = "))
            ket = input("Keterangan = ")
            tgl = str(datetime.now())
            data = {
                "kredit":amount,
                "ket":ket,
                "tgl":tgl
            }
            controllerKredit.add(data)

    except:
        t = input("\nKembali? [Y/n] :")
        if(t == 'Y'):
            view.loadView(0)
        else:
            view.loadView(1)
