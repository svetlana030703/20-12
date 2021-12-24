def make_bold(k):
    def wrap():
        return "<u>"+k()+"</u>"
    return wrap
make_bold('Hello')