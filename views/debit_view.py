from . import main_view as view
from datetime import datetime 
from controller import adddebit_controller as controllerDebit

def Main():
    print("============ ADD DEBIT DATA @ SISTEM INFORMASI PENCATATAN KAS RKA ============")
    print("Tambahkan uang masuk :")
    try:
        while(True):
            amount = int(input("Besar Uang Masuk = "))
            ket = input("Keterangan = ")
            tgl = str(datetime.now())
            data = {
                "debet":amount,
                "ket":ket,
                "tgl":tgl
            }
            controllerDebit.add(data)
    except:
        t = input("\nKembali? [Y/n] :")
        if(t == 'Y'):
            view.loadView(0)
        else:
            view.loadView(1)
