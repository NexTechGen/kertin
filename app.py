from flask import Flask, render_template
import os

curent_dir = os.getcwd()
imge_path = curent_dir + "/static/imagesForPage"
buttons = os.listdir(imge_path)

list_of_images = []

for filles in buttons:
  path = imge_path + "/" + filles
  find_imgs = os.listdir(path)
  for imgs in find_imgs:
    pri = imgs.split(".")[0]
    c = f"{filles}/{imgs}"

    list_of_images.append({"btn_nm": filles, "img_path" : c, "price": pri})

#print("butt", buttons)
#print(list_of_images)

app = Flask(__name__)


@app.route("/")
def sarjaan():
  return render_template("home.html")  # home.html or home_bootstrap.html


@app.route("/project.html")
def projects():
  return render_template("includes/project.html",
                         fil_buttons=buttons,
                         images_file=list_of_images)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
