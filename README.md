# catgameGTK
yup. i just recode my "catgame" project to python :3

![shields.io badge](https://img.shields.io/badge/linux-e6b30e?labelColor=e6b30e&style=plastic&logoColor=FFFFFF&logo=linux)
![shields.io badge](https://img.shields.io/badge/GTK_3.0-106dc4?labelColor=106dc4&style=plastic&logoColor=FFFFFF&logo=gtk)
![shields.io badge](https://img.shields.io/badge/cat_smile-:3-482c63?labelColor=6d1bbf&style=plastic)

![preview](https://github.com/user-attachments/assets/e73510fc-1b4b-4906-b7fc-32f62fdc93ec)

## how to install
### from .deb file
1. download .deb file from latest release
2. install deb package. recommended:
```bash
sudo apt install ./catgamegtk.deb
```
3. all done!
### from source code
1. run this command if you have apt:
```bash
sudo apt install python3-gi python3-requests python3-notify2
```
or this commands if you have pip (pipx):
```bash
pip install PyGObject
pip install requests
pip install notify2
```
2. just "git clone" this repository (or download source code from release) to some folder in your home directory.
3. go to game folder and run catgamegtk file
```bash
./catgamegtk
```
4. all done!


#### create .desktop file

you also need to create a .desktop file for app! just create org.Igor360.catgameGTK.desktop and paste this intro file:

```
[Desktop Entry]
Type=Application
Name=catgameGTK
Comment=tamogochi but on PyGObject!
Icon=/part/to/icon.png
Exec=./catgamegtk
Path=/path/to/gamefolder
Actions=
Categories=Game;#
```

replace /path/to/gamefolder with real path to game folder! like this:

```
Path=/home/igor/catgameGTK
```

also do this with /part/to/icon.png

```
Icon=/home/igor/catgameGTK/data/icon.png
```

# roadmap

i create some markdown table :3

|version|innovation|status|
|-|-|-|
|1.9|big UI upgrade!|all done!|
|2.0|seal mode🦭 and shadows|not started|
|2.1|new hats!|not started|
|2.2|custom hats!|not started|
|2.3|mini games!|not started|
|2.4|big update of cats feelings!|not started|
|2.5|CUSTOM CATS!!!!|not started|
|2.6|new settings (using Gtk.TreeView)|not started|
