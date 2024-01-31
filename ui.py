import dearpygui.dearpygui as dpg
import pyperclip

w, h = 600, 300

dpg.create_context()
dpg.create_viewport(title='DisisentGen', width=w, height=h)


def toggle_show_password():
    if dpg.is_item_visible('password_showed'):  # hide
        dpg.hide_item('password_showed')
        dpg.show_item('password')
        dpg.set_item_label('toggle_show', 'Show')
    else:  # show
        dpg.hide_item('password')
        dpg.show_item('password_showed')
        dpg.set_item_label('toggle_show', 'Hide')


def copy_password():
    pyperclip.copy(dpg.get_value('password'))


charset = {'letters': True, 'numbers': True, 'chars': True}  # default charset values
special_charset = {'punctuation': True, 'mathChars': True, 'otherChars': True}
definition_charset = {
    'letters': 'qwertyuiopasdfghjklzxcvbnm', 'numbers': '0123456789',
    'punctuation': '!?:;.,\"', 'mathChars': '%*+=-/', 'otherChars': '@#$^&()_№|<>'
}


def switch_charset(charset_type, new_bool):
    charset[charset_type] = new_bool

    if charset_type == 'chars' and not new_bool:
        for i in special_charset:
            special_charset[i] = False
            dpg.set_value(i, False)
            dpg.disable_item(i)
    elif charset_type == 'chars' and new_bool:
        for i in special_charset:
            special_charset[i] = True
            dpg.set_value(i, True)
            dpg.enable_item(i)

    update_custom_charset()


def switch_special_charset(charset_type, new_bool):
    special_charset[charset_type] = new_bool
    update_custom_charset()


def update_custom_charset():
    all_charset = ''

    for i in charset:
        if i == 'chars': continue
        if charset[i]:
            all_charset += definition_charset[i]

    for i in special_charset:
        if special_charset[i]:
            all_charset += definition_charset[i]

    dpg.set_value('custom_charset', all_charset)


def filter_custom_charset():  # костыль из-за https://github.com/hoffstadt/DearPyGui/issues/643
    new_str = dpg.get_value('custom_charset')
    stripped = "".join(dict.fromkeys(new_str))
    if stripped != new_str:
        dpg.set_value('custom_charset', stripped)
        return


with dpg.item_handler_registry(tag='custom_charset_handler') as handler:
    dpg.add_item_deactivated_after_edit_handler(callback=filter_custom_charset)


def custom_charset_callback(_, new_str):
    _updated = False

    for group_chars in definition_charset:  # update checkboxes if manually removed/added their chars
        for char in definition_charset[group_chars]:  # check each char, because don't care about permutation
            if new_str.find(char) == -1:
                dpg.set_value(group_chars, False)
                _updated = True
                break
        else:
            dpg.set_value(group_chars, True)

    if _updated:
        pass
        # TODO: there we use custom charset
    else:
        pass
        # TODO: there we DONT use custom charset


with dpg.window(label='DisisentGen', tag='main'):
    dpg.add_input_text(tag='password', label="Password", hint='Generated password will be here', password=True)
    dpg.add_input_text(tag='password_showed', label="Password", source='password', show=False)

    with dpg.group(horizontal=True):
        dpg.add_button(tag='toggle_show', label='Show', callback=toggle_show_password)
        dpg.add_button(tag='copy', label='Copy', callback=copy_password)

    with dpg.group(horizontal=True):
        dpg.add_checkbox(tag='letters', label='Letters', default_value=charset['letters'], callback=switch_charset)
        dpg.add_checkbox(tag='numbers', label='Numbers', default_value=charset['numbers'], callback=switch_charset)
        dpg.add_checkbox(tag='chars', label='Special characters', default_value=charset['chars'],
                         callback=switch_charset)

    with dpg.collapsing_header(label="Extra settings"):
        with dpg.group(horizontal=True):
            dpg.add_checkbox(tag='punctuation', label="!?:;.,\"", default_value=special_charset['punctuation'],
                             callback=switch_special_charset)
            dpg.add_checkbox(tag='mathChars', label="%*+=-/", default_value=special_charset['mathChars'],
                             callback=switch_special_charset)
            dpg.add_checkbox(tag='otherChars', label="@#$^&()_№|<>", default_value=special_charset['otherChars'],
                             callback=switch_special_charset)

        dpg.add_input_text(tag='custom_charset', label='Custom charset',
                           hint='Enter a charset or use the checkboxes',
                           no_spaces=True, callback=custom_charset_callback)
        dpg.bind_item_handler_registry('custom_charset', "custom_charset_handler")

update_custom_charset()

dpg.set_primary_window('main', True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
