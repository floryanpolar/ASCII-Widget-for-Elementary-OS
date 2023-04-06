#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

EMOJI_LIST = [    ("¯\_(ツ)_/¯", "Shrug"),    ("(╯°□°）╯︵ ┻━┻", "Table Flip"),    ("┬─┬ノ( º _ ºノ)", "Table Fix"),    ("( ͡° ͜ʖ ͡°)", "Lenny Face"),    ("(ಥ﹏ಥ)", "Crying Face"),    ("(ง'̀-'́)ง", "Fight"),    ("(づ｡◕‿‿◕｡)づ", "Hug"),    ("(╬ಠ益ಠ)", "Angry Face"),    ("(⌐■_■)", "Cool Face"),    ("( ͡~ ͜ʖ ͡°)", "Lenny Face"),    ("¯\\(°_o)/¯", "Confused"),    ("(づ￣ ³￣)づ", "Blow Kiss"),    ("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "Excited"),    ("ᕕ( ᐛ )ᕗ", "Flex"),    ("(っ◕‿◕)っ", "Cute Face"),    ("(╯︵╰,)", "Sad Face"),    ("( ͡°⊱ ͡°)", "Magic"),    ("(つ◕౪◕)つ━☆ﾟ.*･｡ﾟ", "Sparkles"),    ("(✿◠‿◠)", "Happy Face"),]

class EmojiWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ASCII Emoji Widget")
        self.set_border_width(10)
        self.set_size_request(300, 400)

        grid = Gtk.Grid()
        self.add(grid)

        row = 0
        col = 0

        for emoji, name in EMOJI_LIST:
            button = Gtk.Button(label=emoji)
            button.connect("clicked", self.on_emoji_clicked, emoji)
            grid.attach(button, col, row, 1, 1)
            col += 1
            if col == 3:
                col = 0
                row += 1

        self.connect("key_press_event", self.on_key_press)

    def on_emoji_clicked(self, button, emoji):
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(emoji, -1)
        self.hide()

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_period and event.state == Gdk.ModifierType.CONTROL_MASK:
            self.show_all()

win = EmojiWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

