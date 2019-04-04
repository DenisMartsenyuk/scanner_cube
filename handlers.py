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
        print('Def: ' + update)


class CallbackHandler(Handler):
    def __init__(self, callback):
        self.callback = callback

    def handle_update(self, update: str, chat):
        self.callback(update, chat)


def partition_update(s: str):
    ''' Type data -> (Type, data) '''
    try:
        type_part, _, data_part = s.partition(' ')
    except ValueError as exc:
        raise exc
    return type_part, data_part


class CommandTypeHandler(CallbackHandler):
    def __init__(self, command_name: str, callback):
        super(CommandTypeHandler, self).__init__(callback)
        self.command_name = command_name.lower()

    def check_update(self, update: str, chat):
        update = update.lower()
        try:
            command_name, _ = partition_update(update)
        except ValueError:
            raise Exception('Format')
        return self.command_name == command_name
