

from views import home_view, debit_view, kredit_view, info_saldo_view

def loadView(loc):
    try:
        match loc:
            case 0:
                home_view.Main()
            case 1:
                debit_view.Main()
            case 2:
                kredit_view.Main()
            case 3:
                info_saldo_view.Main()
    except:
        t = input("\n Exit the program? [Y/n] : ")
        if(t == 'Y'):
            print("Goodbye :'")
            exit()
        else:
            home_view.Main(0)
