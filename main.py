import eel
eel.init('web')


@eel.expose
def test():
    return "test"


eel.start('index.html')
