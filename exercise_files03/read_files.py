##############################
#プログラムの解説(1)

import openpyxl as excel, glob

#ファイル一覧を読み込む対象のディレクトリを指定
target_dir = "./salesfiles"
#保存先のファイル名を指定
save_file = "matome.xlsx"

#メイン処理
def read_files():
    #売上一覧を書き込むブックを用意する
    book = excel.Workbook()
    main_sheet = book.active
    #globを使ってファイルの一覧を得る
    files = glob.glob(target_dir + "/*.xlsx")
    #各Excelのブックを次々と読んでいく
    for fname in files:
        read_book(main_sheet, fname)
    book.save(save_file)

##############################
#プログラムの解説(2)

#ブックを開いて中身を読み込む
def read_book(main_sheet, fname):
    print("read file:", fname)
    #Excelブックを読み込む
    book = excel.load_workbook(fname, data_only=True)
    sheet = book.active
    #売上データのある範囲を読み込む(Noの列はまとめ対象外)
    for row in sheet["B4":"G999"]:
        #セルの値をリストとして得る
        values = [cell.value for cell in row]
        if values[0] == None:
            break
        #メインシートに値をコピー
        main_sheet.append(values)

##############################
#プログラムの解説(3)

#メインプログラムを実行
#これによりメイン処理部分がモジュールとしても使用可能となる
if __name__ == "__main__":
    read_files()
