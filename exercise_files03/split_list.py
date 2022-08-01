##############################
#プログラムの解説(1)

import openpyxl as excel, json
#入出力ファイル名
in_file = "matome.xlsx"
out_file = "matome.json"

#メイン処理
def split_list():
    #Excelシートのデータを顧客ごとに分ける
    customers = read_and_split(in_file)
    #顧客ごとにデータを集計する
    result = {} #集計用の空の辞書を作成
    #顧客の辞書のキーと値に対してループを実行
    for name, rows in customers.items():
        result[name] = calc_customer(rows)
        print(name, result[name]['total'])
    #ファイルに結果を保存
    with open(out_file, "wt") as fp:
        json.dump(result, fp)

##############################
#プログラムの解説(2)

#入力ファイルを読んで顧客ごとに分割
def read_and_split(in_file):
    customers = {} #分割用の空の辞書を作成
    #ブックを開いてシートの全行を読む
    book = excel.load_workbook(in_file)
    sheet = book.active

    #イテレータの作成（すべて読み込むため引数は省略可）
    it = sheet.iter_rows()
    for row in it:
        #シートの一行を取り出してリストに変換
        values = [col.value for col in row]
        name = values[1] #顧客名（B列）を取り出す
        #顧客一覧の辞書の中に顧客名のキーがあるかどうかを調べる
        if name not in customers:
            customers[name] = [] #無ければリストを初期化
        #データを顧客毎に分ける
        customers[name].append(values)
    return customers

##############################
#プログラムの解説(3)

#顧客一人分のデータを集計する
def calc_customer(rows):
    total = 0 #合計金額の初期化
    items = [] #請求の明細用
    #集計処理を行う
    for row in rows:
        #値のリストから各項目のデータを抽出（購入者と金額は使わない）
        (date, _, item, price, cnt, _) = row
        #日付を文字列として保存（月/日）
        date_s = date.strftime("%m/%d")
        #請求書明細の形式で追加
        items.append([date_s, item, price, cnt])
        #合計金額を計算
        total += price*cnt
    #集計結果を辞書形式で返す
    return {'items': items, 'total': total}

#メインプログラムを実行
if __name__ == "__main__":
    split_list() #メイン処理を実行
