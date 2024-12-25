import subprocess
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import time
import requests
import random
import zipfile
from io import BytesIO
import shutil

version = "1.7"
versiona = "release 1.7"
cdata = os.path.expanduser("~/.local/share/catdata")
current_dir = os.path.dirname(os.path.abspath(__file__))


def pushn(p, n, m):
    subprocess.call(['notify-send', '-i', p, n, m])
    return


def upgrader():
    username = "lgor360"
    repo = "catgameGTK"

    url = f'https://api.github.com/repos/{username}/{repo}/releases/latest'

    response = requests.get(url)
    if response.status_code == 200:
        release_data = response.json()
        zipball_url = release_data['zipball_url']

        download_path = os.path.dirname(os.path.abspath(__file__))

        zip_response = requests.get(zipball_url)
        if zip_response.status_code == 200:
            if os.path.isfile(os.path.join(current_dir, "data/settings.txt")):
                with open(os.path.join(current_dir, "data/settings.txt"), "r", encoding="utf-8") as f:
                    conf = f.readlines()
                
            shutil.rmtree(download_path)
            os.makedirs(download_path, exist_ok=True)
            with zipfile.ZipFile(BytesIO(zip_response.content)) as zip_file:
                zip_file.extractall(download_path) 

            extracted_folder = os.path.join(download_path, os.listdir(download_path)[0])
        
            github_folder = os.path.join(extracted_folder, ".github")
            if os.path.exists(github_folder):
                shutil.rmtree(github_folder)

            for item in ["LICENSE", "README.md"]:
                item_path = os.path.join(extracted_folder, item)
                if os.path.isfile(item_path):
                    os.remove(item_path) 
        
            for item in os.listdir(extracted_folder):
                item_path = os.path.join(extracted_folder, item)
                if item != ".github": 
                    os.rename(item_path, os.path.join(download_path, item))
        
            os.rmdir(extracted_folder) 

            
            with open(os.path.join(download_path, "data/settings.txt"), "w") as f:
                f.writelines(conf)
            
            pushn(os.path.join(current_dir, f"data/icon.png"), "catgameGTK", "game is up-to-date now! restart the game")
        else:
            info_dialog = Gtk.MessageDialog(
                parent=None,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text="ERROR! update cant be download! sorry!"
            )
    else:
        info_dialog = Gtk.MessageDialog(
            parent=None,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text="ERROR! i cant get latest release info on github! sorry!"
        )
    return


def upsure(v):
    warning = Gtk.MessageDialog(
        title="catgameGTK",
        message_type=Gtk.MessageType.WARNING,
        buttons=Gtk.ButtonsType.OK_CANCEL,
        text=f"WAIT! a new version of catgameGTK has been released! please upgrade this game to {v} or you can start update now!"
    )
    warning.format_secondary_text(
        "click OK if u want to start update now"
    )
    response = warning.run()
    if response == Gtk.ResponseType.OK:
        upgrader()
        warning.destroy()
        Gtk.main_quit()
    else:
        warning.destroy()


def check():
    if os.path.exists(os.path.join(current_dir, "data/settings.txt")):
        with open(os.path.join(current_dir, "data/settings.txt"), "r", encoding="utf-8") as f:
            conf = f.readlines()
    else:
        conf = ["1"]
    if not int(conf[0].strip()) == 0:
        response = requests.get('https://api.github.com/repos/lgor360/catgameGTK/releases/latest')

        if response.status_code == 200:
            release_data = response.json()
            v = release_data['tag_name']
            if version > v:
                print("beta (whaaaaaaa)")
                pushn(os.path.join(current_dir, f"data/icon.png"), "catgameGTK", "how do you find this beta version of catgameGTK...")
            elif version < v:
                print("old")
                upsure(v)
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
            cattxt[3] = "sad.png\n"
            caticon = "sad.png"
            path = os.path.join(current_dir, f"data/colors/{cview}/sad.png")
            with open(os.path.join(cdata, "cat.txt"), "w") as f:
                f.writelines(cattxt)
            os.remove(os.path.join(cdata, "teat.txt"))
            q_item.set_from_file(os.path.join(current_dir, f"data/colors/{cview}/sad.png"))

    return


def on_response(dialog, ftype):
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()
    print(ftype)

    if ftype == "catfood":
        eat()
    elif ftype == "desert":
        path = os.path.join(current_dir, f"data/colors/{cview}/{cicon}")
        pushn(path, name, "tasty")

    dialog.destroy()


def sethat(ftype):
    het_item.set_from_file(os.path.join(current_dir, f"data/hats/{ftype}.png"))
    if len(cattxt) >= 6:
        cattxt.remove(cattxt[5])
        print(cattxt)
    cattxt[4] = f"{cattxt[4].strip()}\n"
    cattxt.insert(5, ftype)
    print(cattxt)
    with open(os.path.join(cdata, "cat.txt"), "w") as f:
        f.writelines(cattxt)


def delhat():
    het_item.set_from_pixbuf(None)
    if len(cattxt) >= 6:
        cattxt.remove(cattxt[5])
        cattxt[4] = cattxt[4].strip()
        print(cattxt)
        with open(os.path.join(cdata, "cat.txt"), "w") as f:
            f.writelines(cattxt)


def store(button):
    dialog = Gtk.Dialog("choose the hat", None, 0,)

    l = Gtk.Label(label="select the hat for your cat :3")
    dialog.vbox.pack_start(l, False, True, 10)

    magicianshat = Gtk.Button()
    oi = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, "data/hats/magicianshat.png"))
    oki = oi.scale_simple(140, 140, GdkPixbuf.InterpType.BILINEAR)
    okii = Gtk.Image.new_from_pixbuf(oki)
    magicianshat.add(okii)
    cap = Gtk.Button()
    koi = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, "data/hats/cap.png"))
    koki = koi.scale_simple(140, 140, GdkPixbuf.InterpType.BILINEAR)
    kokii = Gtk.Image.new_from_pixbuf(koki)
    cap.add(kokii)
    delete = Gtk.Button(label="remove the hat")

    delete.connect("clicked", lambda w: delhat())
    magicianshat.connect("clicked", lambda w: sethat("magicianshat"))
    cap.connect("clicked", lambda w: sethat("cap"))

    dialog.action_area.pack_start(magicianshat, True, True, 0)
    dialog.action_area.pack_start(cap, True, True, 0)
    dialog.action_area.pack_start(delete, True, True, 0)

    dialog.set_default_size(200, 70)
    dialog.set_resizable(False)
    dialog.show_all()


def sseti(dialog, se):
    s = se.get_active()
    if s == True:
        svalue = "1"
    elif s == False:
        svalue = "0"
    print(svalue)
    with open(os.path.join(current_dir, "data/settings.txt"), "w") as f:
        f.writelines(f"{svalue}")

    dialog.destroy()


def deletecat(func):
    pushn(os.path.join(current_dir, f"data/colors/{cview}/{cattxt[3].strip()}"), cattxt[0].strip(), "what?..")
    warning = Gtk.MessageDialog(
        title="catgameGTK",
        message_type=Gtk.MessageType.WARNING,
        buttons=Gtk.ButtonsType.OK_CANCEL,
        text="are you sure want to delete your cat?"
    )
    warning.format_secondary_text(
        "you cant undo this!!!!"
    )
    response = warning.run()
    if response == Gtk.ResponseType.OK:
        pushn(os.path.join(current_dir, f"data/colors/{cview}/sad.png"), cattxt[0].strip(), "oh...")
        time.sleep(1)
        warning.destroy()
        pushn(os.path.join(current_dir, f"data/icon.png"), "catgameGTK", "deleting your cat...")
        inf_item.set_text("cat name: cat_name")
        q_item.set_from_file(os.path.join(current_dir, "data/colors/cview/happy.png"))
        het_item.set_from_file(os.path.join(current_dir, "data/colors/cview/happy.png"))
        pushn(os.path.join(current_dir, f"data/colors/{cview}/cat_status.png"), "cat_name", "AAAAAAAAAAAAAAAAAA")
        if os.path.exists(os.path.join(cdata, "teat.txt")):
            os.remove(os.path.join(cdata, "teat.txt"))
        os.remove(os.path.join(cdata, "cat.txt"))
        os.rmdir(os.path.expanduser("~/.local/share/catdata"))
        pushn(os.path.join(current_dir, f"data/icon.png"), "catgameGTK", "success!")
        Gtk.main_quit()
    else:
        warning.destroy()


def rencat(func):
    dialog = Gtk.Dialog("your cat name", None, 0,
                        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                          Gtk.STOCK_OK, Gtk.ResponseType.OK))


    input_box = Gtk.Entry()
    dialog.vbox.pack_start(input_box, True, True, 0)


    dialog.set_default_size(200, 70)
    dialog.set_resizable(False)
    dialog.show_all()

    response = dialog.run()

    if response == Gtk.ResponseType.OK:
        user_input = input_box.get_text()
        cattxt[0] = f"{user_input}\n"
        print(cattxt)
        with open(os.path.join(cdata, "cat.txt"), "w") as f:
            f.writelines(cattxt)
        inf_item.set_text(f"cat name: {user_input}")
    dialog.destroy()


def setti(event):
    if os.path.exists(os.path.join(current_dir, "data/settings.txt")):
        with open(os.path.join(current_dir, "data/settings.txt"), "r", encoding="utf-8") as f:
            conf = f.readlines()
    else:
        with open(os.path.join(current_dir, "data/settings.txt"), "w") as f:
            f.write("1")
        with open(os.path.join(current_dir, "data/settings.txt"), "r", encoding="utf-8") as f:
            conf = f.readlines()

    dialog = Gtk.Dialog("settings", None, 0)
    # hi for programmers! oh! i want to say you what you are the best because you find this message! bye :3

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
    upgra = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
    box.set_homogeneous(True)
    dialog.vbox.add(box)
    box.add(upgra)

    l = Gtk.Label(label="check for updates")
    l.set_hexpand(True)
    button_ok = Gtk.Button(label="save")
    button_ok.set_hexpand(True)
    button_cancel = Gtk.Button(label="cancel")
    button_cancel.set_hexpand(True)
    updates = Gtk.Switch()
    updates.set_hexpand(True)
    updates.set_active(bool(int(conf[0].strip())))
    rename = Gtk.Button(label="rename your cat")
    rename.set_hexpand(True)
    delcat = Gtk.Button(label="delete your cat (save data)")
    delcat.set_hexpand(True)

    button_ok.connect("clicked", lambda w: sseti(dialog, updates))
    button_cancel.connect("clicked", lambda w: on_response(dialog, "cancel"))
    delcat.connect("clicked", lambda w: deletecat("settings"))
    rename.connect("clicked", lambda w: rencat("settings"))

    upgra.add(l)
    upgra.add(updates)
    box.add(rename)
    box.add(delcat)
    dialog.action_area.add(button_cancel)
    dialog.action_area.add(button_ok)

    dialog.set_default_size(240, 70)
    dialog.set_resizable(False)
    dialog.show_all()


def what(event):
    dialog = Gtk.Dialog("feed the cat", None, 0,)

    l = Gtk.Label(label="choose the food")
    dialog.vbox.pack_start(l, False, True, 10)

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

    button_ok.connect("clicked", lambda w: on_response(dialog, "catfood"))
    button_cancel.connect("clicked", lambda w: on_response(dialog, "desert"))

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
    ab.set_version(versiona)
    ab.set_comments("the game was made in 2024\ni say hello from Russia!\n \ngame is recoded from bash to python")
    ab.set_authors(["Igor360"])
    ab.set_website("https://github.com/lgor360/catgameGTK")
    ab.set_license(license)
    ic = GdkPixbuf.Pixbuf.new_from_file(os.path.join(current_dir, "data/icon.png"))
    icon = ic.scale_simple(150, 150, GdkPixbuf.InterpType.BILINEAR)
    ab.set_logo(icon)
    ab.connect("response", lambda dialog, response: dialog.destroy())
    ab.show()


def pur(event):
    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    path = os.path.join(current_dir, f"data/colors/{cview}/{cicon}")
    pushn(path, name, "purrrrrrrr")


def cond(event):
    condition = cattxt[1].strip()
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    path = os.path.join(current_dir, f"data/colors/{cview}/{cicon}")
    pushn(path, name, condition)


def game(event):
    games = cattxt[2].strip()

    path = os.path.join(current_dir, f"data/icon.png")
    games = int(games)
    games += 1
    pushn(path, "catgameGTK", f"{games} game(s)")
    
    cattxt[2] = f"{games}\n"

    with open(os.path.join(cdata, "cat.txt"), "w") as f:
        f.writelines(cattxt)


def eat():
    cicon = cattxt[3].strip()
    name = cattxt[0].strip()

    path = os.path.join(current_dir, f"data/colors/{cview}/happy.png")
    
    q_item.set_from_file(os.path.join(current_dir, f"data/colors/{cview}/happy.png"))
    cattxt[1] = f"happy and not hungry\n"
    cattxt[3] = "happy.png\n"

    with open(os.path.join(cdata, "cat.txt"), "w") as f:
        f.writelines(cattxt)
    teat = int(time.time()) + 10800
    with open(os.path.join(cdata, "teat.txt"), "w") as f:
        f.write(f"{teat}")
    pushn(path, name, "yummy!")


def main():
    global cattxt
    with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
       cattxt = f.readlines()
    print(cattxt)
    global cview

    if 4 == len(cattxt):
        cattxt[3] = f"{cattxt[3]}\n"
        randome = random.randint(1, 3)
        cattxt.insert(4, f"{randome}")
        with open(os.path.join(cdata, "cat.txt"), "w") as f:
            f.writelines(cattxt)
        with open(os.path.join(cdata, "cat.txt"), "r", encoding="utf-8") as f:
            cattxt = f.readlines()
        print(cattxt[4])
        cview = cattxt[4].strip()
    else:
        cview = cattxt[4].strip()

    check()

    window = Gtk.ApplicationWindow(application=app, title="catgameGTK")
    # window.set_icon_from_file(os.path.join(current_dir, "data/icon.png"))
    window.set_default_size(500, 250)
    window.set_resizable(False)
    # window.connect("destroy", Gtk.main_quit)
    name = cattxt[0].strip()
    caticon = cattxt[3].strip()
    print(f"data/colors/{cview}/{caticon}")
    path = os.path.join(current_dir, f"data/colors/{cview}/{caticon}")

    main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)

    bb = Gtk.Box()
    menu_grid = Gtk.ActionBar()

    create_file_item = Gtk.Button(label="hats")
    create_file_item.connect("clicked", store)
    menu_grid.pack_start(create_file_item)

    b_item = Gtk.Button(label="about this game")
    b_item.connect("clicked", infgame)
    menu_grid.pack_start(b_item)

    se_item = Gtk.Button(label="\u2699")
    se_item.connect("clicked", setti)
    menu_grid.pack_end(se_item)

    bb.pack_start(menu_grid, True, True, 0)
    main_box.pack_start(bb, False, True, 0)

    s = Gtk.Separator()
    s.set_size_request(-1, 2.5)
    main_box.add(s)

    cat_grid = Gtk.Grid()
    cat_grid.set_row_homogeneous(True)

    global het_item
    het_item = Gtk.Image()

    if 6 == len(cattxt):
        het_item.set_from_file(os.path.join(current_dir, f"data/hats/{cattxt[5]}.png"))
        print(os.path.join(current_dir, f"data/hats/{cattxt[5]}.png"))

    het_item.set_hexpand(True)
    cat_grid.attach(het_item, 0, 0, 1, 3)

    global q_item
    q_item = Gtk.Image.new_from_file(path)
    q_item.set_hexpand(True)
    cat_grid.attach(q_item, 0, 0, 1, 3)
    ceat()

    global inf_item
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

    window.add(main_box)

    window.show_all()
    Gtk.main()


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

    response = dialog.run()

    if response == Gtk.ResponseType.OK:
        user_input = input_box.get_text()
        print(f"cat name: {user_input}")
        randome = random.randint(1, 3)

        if os.path.isdir(cdata):
            print("pikimiki")
        else:
            os.makedirs(os.path.join(shdata, "catdata"), exist_ok=True)

        if user_input == "i dont care":
            with open(os.path.join(cdata, "cat.txt"), "w") as f:
                f.write("jax\nsad and hungry\n0\nsad.png\n10-1-24\ncap")
        else:
            with open(os.path.join(cdata, "cat.txt"), "w") as f:
                f.write(f"{user_input}\nsad and hungry\n0\nsad.png\n{randome}")
            
        dialog.destroy()
        main()
    else:
        dialog.destroy()


def start():
    if os.path.exists(os.path.join(cdata, "cat.txt")):
        main()
    else:
        install()


def on_activate(u):
    start()


app = Gtk.Application(application_id="org.Igor360.catgameGTK")
app.connect("activate", on_activate)
app.run(None)
