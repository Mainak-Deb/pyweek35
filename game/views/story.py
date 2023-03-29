from typing import Union
from assets import tilemaps, fonts

import arcade.gui

from game.views import BaseView


def get_storybook_ui(
    window: arcade.Window,
) -> Union[arcade.gui.UIWidget, list[arcade.gui.UIWidget]]:
    # Create a vertical BoxGroup to align buttons
    h_box = arcade.gui.UIBoxLayout(vertical=False)

    data = {
        "pages": {
            1: "Welcome to the asylum. \n\nYou're surrounded by darkness and fear.",
            2: "The doctors are after you, and you have to escape before it's too late. \nBut be warned, this asylum holds dark secrets and twisted experiments. \n\nThe path to freedom will not be easy.",
            3: "Watch out for the doctors. Explore the asylum, search for clues, and solve puzzles. Collect batteries to keep your flashlight lit, use any tool you can find to defend yourself.",
            4: "As you delve deeper into the asylum, you'll uncover its dark secrets and learn the truth about what really goes on behind its walls. But will you make it out alive, or will you become just another victim of its madness?",
            5: "But remember, every step you take could be your last. Good luck."
        },
        "cur_page": 1,
        "max_page": 5,
    }
    arcade.load_font(fonts.resolve("Melted Monster.ttf"))
    text_area = arcade.gui.UITextArea(
        x=100,
        y=200,
        width=500,
        height=300,
        text=data["pages"][data["cur_page"]],
        text_color=arcade.csscolor.WHITE,
        font_size=20,
        font_name="Melted Monster"
    )

    # Create the buttons
    prev_button = arcade.gui.UIFlatButton(text="Prev", width=200)
    h_box.add(prev_button.with_space_around(right=20))

    skip_button = arcade.gui.UIFlatButton(text="Skip", width=200)
    h_box.add(skip_button.with_space_around(right=20))

    next_button = arcade.gui.UIFlatButton(text="Next", width=200)
    h_box.add(next_button.with_space_around(right=20))

    @prev_button.event("on_click")
    def on_click_prev(event):
        print("Prev:", event)
        # TODO: Greyout if cur_page = 1
        data["cur_page"] = max(1, data["cur_page"] - 1)
        text_area.text = data["pages"][data["cur_page"]]

    @next_button.event("on_click")
    def on_click_next(event):
        print("Next:", event)
        if data["cur_page"] == data["max_page"]:
            window.show_view(BaseView(window.views).configure("GameView"))
            return
        data["cur_page"] = min(data["max_page"], data["cur_page"] + 1)
        text_area.text = data["pages"][data["cur_page"]]

    @skip_button.event("on_click")
    def on_click_skip(event):
        print("Skip:", event)
        window.show_view(BaseView(window.views).configure("GameView"))

    return [
        arcade.gui.UIAnchorWidget(anchor_x="center", anchor_y="bottom", child=h_box),
        text_area,
    ]
