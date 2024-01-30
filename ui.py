import dearpygui.dearpygui as dpg

w, h = 600, 300

dpg.create_context()
dpg.create_viewport(title='DisisentGen', width=w, height=h)

with dpg.window(label='DisisentGen', tag='main_window'):
    dpg.add_input_text(label="Password", password=True)

dpg.set_primary_window('main_window', True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
