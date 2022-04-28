# A Python Algorithm that can be used to Give File Name With Current Date And Time

import os
from datetime import datetime

# Displays Current DateTime
curr_datetime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# print(curr_datetime)

# Select A Folder To Store The files {Not Necessary though}
temp_directory = "temp/" 

# Beginning of the filename that you must want
file_name = "FN_"

splitted_path = os.path.splitext(file_name)

modified_picture_path = splitted_path[0] + curr_datetime + splitted_path[1]
print(modified_picture_path)

final_temp_path = temp_directory + modified_picture_path
print(final_temp_path)


# To create a text File with such function
def CreateTxt():
    with open(final_temp_path+".txt", "a+") as f:
        f.write("Successfully written")
    f.close()


CreateTxt()
