from services import adddebit_service as serviceDebit
from views import main_view as view
import pandas
def add(param):
    try:
        data = serviceDebit.add(param)
        print("Debet Data Successfully Added!, \n INFO : \n", pandas.DataFrame(data,index=[0]))
    except Exception as err:
        print("Error : ",err)
        view.loadView(0)
