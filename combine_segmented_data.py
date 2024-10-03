import os

class LengthError(Exception):
    def __init__(self, message, len1, len2):
        self.message = message + "\n" + str(len1) + "\n" + str(len2)
        super().__init__(self.message)

def check_for_dups(folder1, folder2):
    files1 = sorted(os.listdir(folder1))  # List of files in folder1 in alpha order
    files2 = sorted(os.listdir(folder2))  # List of files in folder2 in alpha order
    non_dups = []

    for f in files1:
        if f not in files2:
            non_dups.append(f)
            print(f, "is not in both folders")

    return non_dups

def create_blank_dups(folder1, folder2):
    non_dups = check_for_dups(folder1, folder2)

    if non_dups:
        for f in non_dups:
            new_file_path = os.path.join(folder2, f)
            with open(new_file_path, "w", encoding='utf-8') as newFile:
                pass

        print("Non Dups after create_blank_dups:", len(check_for_dups(folder1, folder2)))
    else:
        print("No Non Dups")


def combine(fileR, fileA):
    try:
        with open(fileR, 'r', encoding='utf-8') as readFile, open(fileA, 'a', encoding='utf-8') as appendFile:
            for line in readFile:
                appendFile.write(line)

        print("Combined", fileR, fileA)

    except:
        print("Excepted", fileR, "or", fileA)




def process_two_folders(folderR, folderA):
    filesR = sorted(os.listdir(folderR))  # List of files in folder1 in alpha order
    filesA = sorted(os.listdir(folderA))  # List of files in folder2 in alpha order
    #print(files1)
    #print(files2)
    if '.DS_Store' in filesR:
        filesR.remove('.DS_Store')
        print("Removed .DS_Store from", folderR, "list")
    
    if '.DS_Store' in filesA:
        filesA.remove('.DS_Store')
        print("Removed .DS_Store from", folderA, "list")
    
    if len(filesR) != len(filesA):
        
        raise LengthError("file list lens don't match!", len(filesR), len(filesA))

    for fileR, fileA in zip(filesR, filesA):
        if fileR == fileA:  # Ensure that the files have the same name
            file_pathR = os.path.join(folderR, fileR)
            file_pathA = os.path.join(folderA, fileA)
            combine(file_pathR, file_pathA)
        else:
            print(f"Warning: {fileR} and {fileA} do not match!")

'''
folderR = './data/labels/new_val'
folderA = './data/labels/val_segmented'

create_blank_dups(folderR, folderA)
create_blank_dups(folderA, folderR)

process_two_folders(folderR, folderA)

'''