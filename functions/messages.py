import tkinter.messagebox

popup_message_dic = {
    'empty_city_search_field': 'Please add a city first.',
    'invalid_city_name':'Please add a valid city name.',
    'api_weather_current':'Failed current weather API query.',
    'api_weather_5_day':'Failed 5 days forecast API query.',
    'no_latitude_longitude':'No coordinates in the DB for the selected city.\n\nThe last available data will be displayed.'
    }

def error_pop_up(window_title, popup_message_dic_key):
    tkinter.messagebox.showinfo( window_title, f"{popup_message_dic[popup_message_dic_key]}")     # tkinter.messagebox.showinfo ( popup window title, message )

# EXAMPLE
# error_pop_up('Error','empty_city_search_field')
# messages.error_pop_up('Error','empty_city_search_field')