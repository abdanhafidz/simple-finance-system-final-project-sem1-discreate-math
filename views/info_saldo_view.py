from . import main_view as view
from repositories import datakas as kas_data
import pandas
def Main():
    print("============ INFORMASI KEUANGAN @ SISTEM INFORMASI PENCATATAN KAS RKA ============")
    print("Catatan Kas :")
    for i in range(0,len(kas_data.kas)):
        info = kas_data.kas[i]
        print(pandas.DataFrame(info,index=[0]))
    view.loadView(0)
