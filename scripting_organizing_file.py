import os

EXTENSION = {
    'photos': ['jpg', 'png', 'psd'],
    'documents': ['pdf', 'txt', 'csv', 'xml', 'gradle', 'properties', 'iml'],
    'executable': ['exe'],
    'video': ['mp4'],
    'python': ['py'],
    'compressed_file': ['zip']
}

BASE_DIR = r'C:\Users\jxeni\Desktop\scripting_organizing_file'  # r refer to raw string, that's means \n is \n not new line

# print(os.listdir(BASE_DIR))  # create list file on the folder
# print(os.sep)  # print directory seperator

for folder_name in EXTENSION:
    folder_path = os.path.join(BASE_DIR, folder_name)
    # print(folder_path) # os independent as it use separator itself as per os

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

for file_name in os.listdir(BASE_DIR):
    ext = file_name.split('.')[-1]
    # print(file_name, ext)
    for folder_name, extensions in EXTENSION.items():
        if ext in extensions:
            os.rename(
                os.path.join(BASE_DIR, file_name),  # source, file from base directory
                os.path.join(BASE_DIR, folder_name, file_name)
                # destination, file move to folder name from base directory
            )  # move the file to respective folder
            continue
