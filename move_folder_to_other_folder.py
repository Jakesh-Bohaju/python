import os
BASE_DIR = r'C:\Users\jxeni\Desktop\scripting_organizing_file'  # here must be your path
MASTER_FOLDER = r'root'

if not os.path.exists(os.path.join(BASE_DIR,MASTER_FOLDER)):
    os.mkdir(os.path.join(BASE_DIR,MASTER_FOLDER))

for item in os.listdir(BASE_DIR):
    if os.path.isdir(os.path.join(BASE_DIR, item)) and not item == MASTER_FOLDER:
        os.rename(
            os.path.join(BASE_DIR, item),
            os.path.join(BASE_DIR, MASTER_FOLDER, item)
        )
