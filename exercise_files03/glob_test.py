import glob
target_dir = "./salesfiles"
files = glob.glob(target_dir + "/*.xlsx")
print(files)
