import os

curent_dir = os.getcwd()
imge_path = curent_dir + "/static/imagesForPage"
buttons = os.listdir(imge_path)

image_path_images = []
price = []

my_dict = {}

lis_dic = []

for filles in buttons:
  path = imge_path + "/" + filles
  find_imgs = os.listdir(path)
  for imgs in find_imgs:
    pri = imgs.split(".")[0]
    c = f"{filles}/{imgs}"

    lis_dic.append({"btn_nm": filles, "img_path" : c, "price": pri})
    

#print(buttons)
#print(image_path_images)
#print(price)
#print(" ")
print(lis_dic)
