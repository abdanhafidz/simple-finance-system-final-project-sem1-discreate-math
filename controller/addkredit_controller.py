from services import addkredit_service as serviceKredit
from views import main_view as view
import pandas
def add(param):
    try:
        data = serviceKredit.add(param)
        print("Kredit Data Successfully Added!, \n INFO : \n", pandas.DataFrame(data,index=[0]))
    except Exception as err:
        print("Error : ",err)
        view.loadView(0)
