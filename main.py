import subprocess
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import time


def store(button):
    cdata = os.path.expanduser("~/.local/share/catdata")
    info_dialog = Gtk.MessageDialog(
        parent=None,
        flags=0,
        message_type=Gtk.MessageType.ERROR,
        buttons=Gtk.ButtonsType.OK,
        text=f"under construction. sorry :("
    )
    
    info_dialog.connect("response", lambda dialog, response: dialog.destroy())
    info_dialog.show()


def infgame(button):
    exit_dialog = Gtk.MessageDialog(
        parent=None,
        flags=0,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text="the game was made in 2024\ni say hello from Russia!\n \ngame is recoded from bash to python"
    )
    exit_dialog.connect("response", lambda dialog, response: dialog.destroy())
    exit_dialog.show()


def pur(event):
    cdata = os.path.expanduser("~/.local/share/catdata")

    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, f"data/{cicon}")
    subprocess.call(['notify-send', '-i', path, name, 'purrrrrr'])


def cond(event):
    cdata = os.path.expanduser("~/.local/share/catdata")

    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()
    condition = cattxt[1].strip()
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, f"data/{cicon}")
    subprocess.call(['notify-send', '-i', path, name, condition])


def game(event):
    cdata = os.path.expanduser("~/.local/share/catdata")

    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()
    games = cattxt[2].strip()
    cicon = "icon.png"
    name = "catgameGTK"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, f"data/{cicon}")
    games = int(games)
    games += 1
    subprocess.call(['notify-send', '-i', path, name, f"{games} game(s)"])
    
    cattxt[2] = f"{games}\n"
    print(cattxt)

    with open(os.path.join(cdata, "cat.txt"), "w") as f:
        f.writelines(cattxt)


def eat(event, image):
    cdata = os.path.expanduser("~/.local/share/catdata")

    with open(os.path.join(cdata, "cat.txt"), encoding="utf-8") as f:
       cattxt = f.readlines()
    cicon = "icon.png"
    name = "catgameGTK"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, f"data/{cicon}")

    subprocess.call(['notify-send', '-i', path, name, "you fed the cat :)"])
    
    cattxt[1] = f"happy and not hungry\n"
    cattxt[3] = "happy.png"
    print(cattxt)

    with open(os.path.join(cdata, "cat.txt"), "w") as f:
        f.writelines(cattxt)
    os.remove(os.path.join(cdata, "eat.txt"))
    teat = int(time.time()) + 10800
    with open(os.path.join(cdata, "teat.txt"), "w") as f:
        f.write(f"{teat}")
    image.set_from_file(os.path.join(current_dir, "data/happy.png"))


def main():
    cdata = os.path.expanduser("~/.local/share/catdata")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    window = Gtk.Window(title="catgameGTK")
    window.set_icon_from_file(os.path.join(current_dir, "data/icon.png"))
    window.set_default_size(500, 250)
    window.set_resizable(False)
    window.connect("destroy", Gtk.main_quit)
    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()
    print(cattxt)
    name = cattxt[0].strip()
    caticon = cattxt[3].strip()
    path = os.path.join(current_dir, f"data/{caticon}")


    if os.path.exists(os.path.join(cdata, "teat.txt")):
        print("a")
        with open(os.path.join(cdata, "teat.txt"), "r", encoding="utf-8") as f:
           teat = f.read()
        teat = int(teat)
        if int(time.time()) >= teat:
            print("b")
            cattxt[1] = f"sad and hungry\n"
            cattxt[3] = "sad.png"
            caticon = "sad.png"
            path = os.path.join(current_dir, "data/sad.png")
            with open(os.path.join(cdata, "cat.txt"), "w") as f:
                f.writelines(cattxt)
            os.remove(os.path.join(cdata, "teat.txt"))


    # Создаем Box для размещения кнопок
    main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)


    # Создаем Grid для размещения кнопок
    menu_grid = Gtk.Grid()


    # Кнопка для создания файла
    create_file_item = Gtk.Button(label="store")
    create_file_item.connect("clicked", store)
    create_file_item.set_hexpand(True)
    menu_grid.attach(create_file_item, 0, 0, 1, 1)


    # Кнопка для выхода
    b_item = Gtk.Button(label="about this game")
    b_item.connect("clicked", infgame)
    b_item.set_hexpand(True)
    menu_grid.attach(b_item, 1, 0, 1, 1)



    # Добавляем Grid в основной Box
    main_box.pack_start(menu_grid, False, True, 0)


    cat_grid = Gtk.Grid()
    cat_grid.set_row_homogeneous(True)


    q_item = Gtk.Image.new_from_file(path)
    q_item.set_hexpand(True)
    cat_grid.attach(q_item, 0, 0, 1, 3)

    inf_item = Gtk.Label(label=f"cat name: {name}")
    inf_item.set_hexpand(True)
    cat_grid.attach(inf_item, 0, 3, 1, 1)

    o_item = Gtk.Button(label="feed the cat")
    o_item.connect("clicked", eat, q_item)
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

    main_box.pack_start(cat_grid, True, True, 0)


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