from . import main_view as view
from repositories import datakas as kas_data
import pandas
def Main():
    print("============ INFORMASI KEUANGAN @ SISTEM INFORMASI PENCATATAN KAS RKA ============")
    print("Catatan Kas :")
    print(pandas.DataFrame(kas_data.kas))
    view.loadView(0)
