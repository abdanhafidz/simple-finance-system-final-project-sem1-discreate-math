from repositories import datakas as kas_data
def add(param):
    kas = kas_data.kas
    saldo_before = kas[len(kas)-1]['saldo']
    saldo_current = saldo_before - param['kredit']
    data2 = kas[len(kas)-1 + 1] = {
        "id_transaksi":len(kas)-1 + 1,
        "tgl":param['tgl'],
        "debet":0,
        "kredit":param['kredit'],
        "keterangan":param['ket'],
        "saldo":saldo_current
    }
    return data2




    