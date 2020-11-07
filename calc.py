class ParseError:
    def __init__(self, message):
        self.message = message


def read_in_float(num):
    try:
        if num.endswith("w") or num.endswith("W"):
            num = num.replace("w", '').replace("W", '')
            return float(num) * 10000
        if num.endswith("k") or num.endswith("K"):
            num = num.replace("k", '').replace("K", '')
            return float(num) * 1000
        return float(num)
    except ValueError:
        raise ParseError("Invalid number {}, the valid format like: 20, 2k, 2.5w, ...".format(num))


def read_in_int(num):
    return int(read_in_float(num))


def read_in_time_in_ms(ts):
    try:
        if ts.endswith("ms"):
            ts = ts.replace("ms", "")
            return float(ts)
        if ts.endswith("s"):
            ts = ts.replace("s", "")
            return float(ts) * 1000
        return float(ts)
    except ValueError:
        raise ParseError("Invalid time {}, the valid format like: 10ms, 10.1s, ...".format(ts))


class CalcArg:
    def __init__(self):
        self.rank = None
        self.batch = None
        self.fps = None
        self.step_time = None

    def none_num(self):
        num = 0
        for name in CalcArg.get_args_stars():
            if getattr(self, name) is None:
                num += 1
        return num

    @staticmethod
    def get_args_stars():
        return {
            "rank": ("r", "R", "p", "P"),
            "batch": ("b", "B"),
            "fps": ("f", "F"),
            "step_time": ("t", "T")
        }

    @staticmethod
    def get_args_reader():
        return {
            "rank": read_in_int,
            "batch": read_in_int,
            "fps": read_in_float,
            "step_time": read_in_time_in_ms
        }

    @staticmethod
    def parse_ele(ele, arg):
        for arg_name, starts in CalcArg.get_args_stars().items():
            for start in starts:
                if ele.startswith(start):
                    ele = ele.replace(start, '')
                    setattr(arg, arg_name, CalcArg.get_args_reader()[arg_name](ele))
                    return

    @staticmethod
    def from_query(query):
        arg = CalcArg()
        for ele in query.split():
            CalcArg.parse_ele(ele, arg)
        return arg


def calc_step_time(arg: CalcArg):
    return "{:.2f}ms".format(1 / (arg.fps / arg.rank / arg.batch) * 1000)