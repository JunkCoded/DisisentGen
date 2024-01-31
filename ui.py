import dearpygui.dearpygui as dpg
import pyperclip
#import dearpygui.demo as demo

w, h = 600, 300

dpg.create_context()
dpg.create_viewport(title='DisisentGen', width=w, height=h)


def toggle_show_password():
    if dpg.is_item_visible('password_showed'):  # hide
        dpg.hide_item('password_showed')
        dpg.show_item('password')
        dpg.set_item_label('toggle_show', 'Show')
    else:   # show
        dpg.hide_item('password')
        dpg.show_item('password_showed')
        dpg.set_item_label('toggle_show', 'Hide')


def copy_password():
    pyperclip.copy(dpg.get_value('password'))


with dpg.window(label='DisisentGen', tag='main'):
    dpg.add_input_text(tag='password', label="Password", password=True)
    dpg.add_input_text(tag='password_showed', label="Password", source='password', show=False)

    with dpg.group(horizontal=True):
        dpg.add_button(tag='toggle_show', label='Show', callback=toggle_show_password)
        dpg.add_button(tag='copy', label='Copy', callback=copy_password)


dpg.set_primary_window('main', True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
