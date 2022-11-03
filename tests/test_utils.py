from querybot.utils import message_process

def test_get_install_number_from_message():
    message = '\n:mesh:: :small_red_triangle:Support ASAP 13587 - \nMon Sept. 26th 1pm - 4pm\nPlease call !\nlocation: 111 Vernon Ave, Brooklyn NY 11206\nDescription: realign litebeam (signal dropped on Sept.7th)'

    install_number = message_process.get_install_number_from_message(message)

    print(install_number)
    assert install_number == 13587

if __name__ == "__main__":
    test_get_install_number_from_message()