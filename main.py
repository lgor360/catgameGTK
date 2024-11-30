import subprocess
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import time
import requests
import asyncio

version = "1.2"
cdata = os.path.expanduser("~/.local/share/catdata")
current_dir = os.path.dirname(os.path.abspath(__file__))

def pushn(p, n, m):
    subprocess.call(['notify-send', '-i', p, n, m])
    return


def check():
    response = requests.get('https://api.github.com/repos/lgor360/catgameGTK/releases/latest')

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        release_data = response.json()
        v = release_data['tag_name']
        if version > v:
            print("beta (whaaaaaaa)")
            pushn(os.path.join(current_dir, f"data/icon.png"), "catgameGTK", "how do you find this beta version of catgameGTK...")
        elif version < v:
            print("old")
            info_dialog = Gtk.MessageDialog(
                parent=None,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text=f"WAIT! a new version of catgameGTK has been released! please upgrade this game to {v}"
            )
    
            info_dialog.connect("response", lambda dialog, response: dialog.destroy())
            info_dialog.show()


    else:
        print(f'error: {response.status_code} - {response.text}')
    return


def ceat():
    if os.path.exists(os.path.join(cdata, "teat.txt")):
        with open(os.path.join(cdata, "teat.txt"), "r", encoding="utf-8") as f:
           teat = f.read()
        teat = int(teat)
        if int(time.time()) >= teat:
            cattxt[1] = f"sad and hungry\n"
            cattxt[3] = "sad.png"
            caticon = "sad.png"
            path = os.path.join(current_dir, "data/sad.png")
            with open(os.path.join(cdata, "cat.txt"), "w") as f:
                f.writelines(cattxt)
            os.remove(os.path.join(cdata, "teat.txt"))
            q_item.set_from_file(os.path.join(current_dir, f"data/sad.png"))

    return


def on_response(dialog, ftype):
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    if ftype == "catfood":
        print("catfood")
        eat()
    elif ftype == "desert":
        print("desert")
        path = os.path.join(current_dir, f"data/{cicon}")
        pushn(path, name, "tasty")


    dialog.destroy()


def store(button):
    info_dialog = Gtk.MessageDialog(
        parent=None,
        flags=0,
        message_type=Gtk.MessageType.ERROR,
        buttons=Gtk.ButtonsType.OK,
        text="under construction. sorry :("
    )
    
    info_dialog.connect("response", lambda dialog, response: dialog.destroy())
    info_dialog.show()


def what(event):
    dialog = Gtk.Dialog("feed the cat", None, 0,)

    l = Gtk.Label(label="choose the food")
    dialog.vbox.pack_start(l, False, True, 0)

    button_ok = Gtk.Button()
    oi = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, "data/cf.png"))
    oki = oi.scale_simple(135, 165, GdkPixbuf.InterpType.BILINEAR)
    okii = Gtk.Image.new_from_pixbuf(oki)
    button_ok.add(okii)
    button_cancel = Gtk.Button()
    koi = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, "data/d.png"))
    koki = koi.scale_simple(135, 165, GdkPixbuf.InterpType.BILINEAR)
    kokii = Gtk.Image.new_from_pixbuf(koki)
    button_cancel.add(kokii)

    # Обработка нажатий кнопок
    button_ok.connect("clicked", lambda w: on_response(dialog, "catfood"))
    button_cancel.connect("clicked", lambda w: on_response(dialog, "desert"))


    # Добавляем кнопки в диалог
    dialog.action_area.pack_start(button_ok, True, True, 0)
    dialog.action_area.pack_start(button_cancel, True, True, 0)

    dialog.set_default_size(200, 70)
    dialog.set_resizable(False)
    dialog.show_all()


def infgame(button):
    with open(os.path.join(current_dir, "data/license.txt"), "r", encoding="utf-8") as f:
       license = f.read()

    ab = Gtk.AboutDialog()
    ab.set_program_name("catgameGTK")
    ab.set_version("release 1.2")
    ab.set_comments("the game was made in 2024\ni say hello from Russia!\n \ngame is recoded from bash to python")
    ab.set_authors(["Igor360"])
    ab.set_website("https://github.com/lgor360/catgameGTK")
    ab.set_license(license)
    ab.set_logo(GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, "data/icon.png")))
    ab.connect("response", lambda dialog, response: dialog.destroy())
    ab.show()


def pur(event):
    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    path = os.path.join(current_dir, f"data/{cicon}")
    pushn(path, name, "purrrrrrrr")


def cond(event):
    condition = cattxt[1].strip()
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    path = os.path.join(current_dir, f"data/{cicon}")
    pushn(path, name, condition)


def game(event):
    games = cattxt[2].strip()
    cicon = "icon.png"
    # hi for programmers! oh! i want to say you what you are the best because you find this message! bye :3
    name = "catgameGTK"

    path = os.path.join(current_dir, f"data/{cicon}")
    games = int(games)
    games += 1
    pushn(path, name, f"{games} game(s)")
    
    cattxt[2] = f"{games}\n"
    print(cattxt)

    with open(os.path.join(cdata, "cat.txt"), "w") as f:
        f.writelines(cattxt)


def eat():
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    path = os.path.join(current_dir, f"data/{cicon}")
    pushn(path, name, "yummy!")
    
    cattxt[1] = f"happy and not hungry\n"
    cattxt[3] = "happy.png"
    print(cattxt)

    with open(os.path.join(cdata, "cat.txt"), "w") as f:
        f.writelines(cattxt)
    teat = int(time.time()) + 10800
    with open(os.path.join(cdata, "teat.txt"), "w") as f:
        f.write(f"{teat}")
    q_item.set_from_file(os.path.join(current_dir, "data/happy.png"))


def main():
    global cattxt
    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()

    check()

    window = Gtk.Window(title="catgameGTK")
    window.set_icon_from_file(os.path.join(current_dir, "data/icon.png"))
    window.set_default_size(500, 250)
    window.set_resizable(False)
    window.connect("destroy", Gtk.main_quit)
    name = cattxt[0].strip()
    caticon = cattxt[3].strip()
    path = os.path.join(current_dir, f"data/{caticon}")

    # Создаем Box для размещения кнопок
    main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)

    ceat()

    bb = Gtk.Box()
    # Создаем Grid для размещения кнопок
    menu_grid = Gtk.ActionBar()


    # Кнопка для создания файла
    create_file_item = Gtk.Button(label="store")
    create_file_item.connect("clicked", store)
    menu_grid.pack_start(create_file_item)


    # Кнопка для выхода
    b_item = Gtk.Button(label="about this game")
    b_item.connect("clicked", infgame)
    menu_grid.pack_start(b_item)

    # Кнопка для выхода
    se_item = Gtk.Button(label="\u2699")
    se_item.connect("clicked", store)
    menu_grid.pack_end(se_item)


    # Добавляем Grid в основной Box
    bb.pack_start(menu_grid, True, True, 0)
    main_box.pack_start(bb, False, True, 0)

    s = Gtk.Separator()
    s.set_size_request(-1, 2.5)
    main_box.add(s)

    cat_grid = Gtk.Grid()
    cat_grid.set_row_homogeneous(True)

    global q_item
    q_item = Gtk.Image.new_from_file(path)
    q_item.set_hexpand(True)
    cat_grid.attach(q_item, 0, 0, 1, 3)

    inf_item = Gtk.Label(label=f"cat name: {name}")
    inf_item.set_hexpand(True)
    cat_grid.attach(inf_item, 0, 3, 1, 1)

    o_item = Gtk.Button(label="feed the cat")
    o_item.connect("clicked", what)
    o_item.set_hexpand(True)
    cat_grid.attach(o_item, 1, 0, 1, 1)

    t_item = Gtk.Button(label="give a toy")
    t_item.connect("clicked", game)
    t_item.set_hexpand(True)
    cat_grid.attach(t_item, 1, 1, 1, 1)

    th_item = Gtk.Button(label="pet the cat")
    th_item.connect("clicked", pur)
    th_item.set_hexpand(True)
    cat_grid.attach(th_item, 1, 2, 1, 1)

    th_item = Gtk.Button(label="cat condition")
    th_item.connect("clicked", cond)
    th_item.set_hexpand(True)
    cat_grid.attach(th_item, 1, 3, 1, 1)

    main_box.pack_end(cat_grid, False, True, 0)


    # Добавляем основной Box в окно
    window.add(main_box)


    window.show_all() # Показываем все элементы окна
    Gtk.main() # Запускаем главный цикл приложения


def install():
    shdata = os.path.expanduser("~/.local/share")

    dialog = Gtk.Dialog("your cat name", None, 0,
                        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                         Gtk.STOCK_OK, Gtk.ResponseType.OK))


    input_box = Gtk.Entry()
    dialog.vbox.pack_start(input_box, True, True, 0)


    dialog.set_default_size(200, 70)
    dialog.set_resizable(False)
    dialog.show_all()

    response = dialog.run() # Ждем ответа от пользователя

    if response == Gtk.ResponseType.OK:
        user_input = input_box.get_text()
        print("cat name:", user_input)
        os.makedirs(os.path.join(shdata, "catdata"), exist_ok=True)
        cdata = os.path.expanduser("~/.local/share/catdata")
        with open(os.path.join(cdata, "cat.txt"), "w") as f:
            f.write(f"{user_input}\nsad and hungry\n0\nsad.png")
        dialog.destroy()
        main()
    else:
        dialog.destroy()


def start():
    if os.path.isdir(os.path.expanduser("~/.local/share/catdata")):
        main()
    else:
        install()


start()