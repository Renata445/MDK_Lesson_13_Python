def start(func):
    def render_input(field):
        return '<p>' + func(field)
    return render_input

def end(func):
    def render_input1(field):
        return func(field) + '</p>'
    return render_input1

@start
@end
def result(field):
    return f'<input id="id_{field}" name="{field}">'

username = result('username')
print(username)