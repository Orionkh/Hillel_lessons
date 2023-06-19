def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"

    return wrapper


def make_italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"

    return wrapper


def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"

    return wrapper


@make_underline
@make_italic
@make_bold
def hello_world():
    return "hello world"


primer = hello_world()
print(primer)
