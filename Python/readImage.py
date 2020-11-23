import numpy as np
from PIL import Image


# Resize the image to fit 30x32 format RGB
# img = np.array(Image.open('Images\\character_left.png'))
# img = img[0:30, 0:32]
# Image.fromarray(img).save('Images\\resized.png')

# Open and manipulate the resized file
png_file = Image.open('Images\\character_right.png')
data = np.asarray(png_file)

# Remove alpha channel data from data matrix
data = data[:,:,:3]

# Convert data matrix to contain binary elements
data = data * (15/255)
data = np.rint(data).astype(np.int32)

# outF = open("C:\\Users\\David_vd_Laan\\Documents\\David\\TU_Delft\\20-21\\Q2\\EE2L11\\ModulesVHDL\\Grass_tile.txt", "w")
print('case v_timer is')
for i in range(0,30):
    print('when "', format(i, "05b"), '"=>')
    print("CASE h_timer IS")
    for j in range(0,32):
# CASE OPTION -- Takes less space than other options (preferred)
        print('when "', format(j, "05b"), '"=>')
        print('Red <="',format(data[i][j][0], "04b"),'";')
        print('Green <="',format(data[i][j][1], "04b"),'";')
        print('Blue <="',format(data[i][j][2], "04b"),'";')

# ROM OPTION -- Takes more space, so not adviced.
        # var1 = format(data[i][j][0], "04b")
        # var2 = format(data[i][j][1], "04b")
        # var3 = format(data[i][j][2], "04b")
        # sentence = '"'+var1+var2+var3+'",'
        # sentence.strip()
        # outF.write(sentence)
        # outF.write("\n")
#
# outF.close()
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
