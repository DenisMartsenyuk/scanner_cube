class Handler(object):
    def check_update(self, update: str, chat):
        ''' Check that handler is able to handle this update '''
        pass

    def handle_update(self, update: str, chat):
        pass


class DefaultHandler(Handler):
    def __init__(self):
        pass

    def check_update(self, update: str, chat):
        return True

    def handle_update(self, update: str, chat):
        print(update)


class CallbackHandler(Handler):
    def __init__(self, callback):
        self.callback = callback

    def handle_update(self, update: str, chat):
        self.callback(update, chat)


def partition_update(s: str):
    ''' [Type]: [data] -> (Type, data) '''
    type_part, data_part = s.split(':')
    type_part = type_part[type_part.find('['):]
    type_part = type_part[:type_part.find(']') + 1]
    type_part = type_part[1:-1]
    data_part = data_part[data_part.find('['):]
    data_part = data_part[:data_part.find(']') + 1]
    data_part = data_part[1:-1]
    return type_part, data_part


class CommandTypeHandler(CallbackHandler):
    def __init__(self, command_name: str, callback):
        super(CommandTypeHandler, self).__init__(callback)
        self.command_name = command_name

    def check_update(self, update: str, chat):
        return update.startswith('[%s]:' % self.command_name)

