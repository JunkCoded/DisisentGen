import dearpygui.dearpygui as dpg
import pyperclip
#import dearpygui.demo as demo

w, h = 600, 300

dpg.create_context()
dpg.create_viewport(title='DisisentGen', width=w, height=h)

def show_password():
    print('show')

def hide_password():
    print('hide')

def copy_password():
    pyperclip.copy(dpg.get_value('password'))

with dpg.window(label='DisisentGen', tag='main_window'):
    dpg.add_input_text(tag='password', label="Password", password=True)
    dpg.add_button(tag='show', label='Show', callback=show_password)
    dpg.add_button(tag='hide', label='Hide', show=False, callback=hide_password)
    dpg.add_button(tag='copy', label='Copy', callback=copy_password)

dpg.set_primary_window('main_window', True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
