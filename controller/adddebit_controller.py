from services import adddebit_service as serviceDebit
from views import main_view as view
def add(param):
    try:
        serviceDebit.add(param)
        return True
    except Exception as err:
        print("Error : ",err)
        view.loadView(0)
