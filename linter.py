from SublimeLinter.lint import Linter, util


class Lua(Linter):
    cmd = 'luac -p ${args} -'
    regex = r'^.+?:.+?:(?P<line>\d+): (?P<message>.+?(?:near (?P<near>\'.+\')|$))'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.lua, source.luae'
    }
