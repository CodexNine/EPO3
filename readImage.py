import numpy as np
from PIL import Image


# Resize the image to fit 30x32 format RGB
img = np.array(Image.open('grass_tile.png'))
img = img[0:30, 0:32]
Image.fromarray(img).save('resized.png')

# Open and manipulate the resized file
png_file = Image.open('resized.png')
data = np.asarray(png_file)

# Remove alpha channel data from data matrix
data = data[:,:,:3]

# Convert data matrix to contain binary elements
data = data * (15/255)
data = np.rint(data).astype(np.int32)

for i in range(0,30):
    # print('when "', format(i, "05b"), '"=>')
    # print("CASE h_timer IS")
    for j in range(0,32):
        # print('when "', format(j, "05b"), '"=>')
        var1 = format(data[i][j][0], "04b")
        var2 = format(data[i][j][1], "04b")
        var3 = format(data[i][j][2], "04b")
        sentence = '"'+var1+var2+var3+'",'
        sentence.strip()
        print(sentence)
        # for m in range(0,3):
        #     if(m == 0):
        #         print('R_grass <= "',format(data[i][j][m], "04b"), '";')
        #     elif(m == 1):
        #         print('G_grass <= "', format(data[i][j][m], "04b"), '";')
        #     elif(m == 2):
        #         print('B_grass <= "', format(data[i][j][m], "04b"), '";')




# for i in range(0,30):
#     for j in range(0,32):
#         for k in range(0,3):
#             print
