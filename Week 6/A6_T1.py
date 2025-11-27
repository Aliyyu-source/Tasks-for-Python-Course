def readFile(Filename : str) -> str:
    Filehandler = open(Filename, 'r', encoding="UTF-8")
    Content = ''
    Row = Filehandler.readline()
    while Row != '':
        Content += Row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content
   

def main() -> None:
    print("Program starting.")
    print("This program can read a file")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename)
    print("#### START \" ####" .format(Filename))
    print(FileContent)
    print("#### END \"{}\" ####".format(Filename))
    print("Program ending")
    return None

if __name__ ==  "_main_"



