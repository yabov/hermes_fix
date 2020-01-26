class CallbackRegistrar:
    class CALLBACK_PRIORITY:
        FIRST = 0
        HIGH = 100
        NORMAL = 200
        LOW = 300
        LAST = 400
        BEFORE = -1
        AFTER = 1

    def __init__(self, loop):
        self.priority_callback_map = {}
        self.loop = loop

    def add_callback(self, msg_class, callback, priority, check_func=None, one_time=False, timeout=None, timeout_cb=None):
        priority_cb = CallbackWrapper(
            priority, callback, check_func, self.loop, timeout=timeout, timeout_cb=timeout_cb)
        if one_time:
            priority_cb.clean_up_func = lambda: self.remove_callback(
                msg_class, priority, callback)

        if msg_class is None:  # None will be used to register a callback for all messages
            if None not in self.priority_callback_map:
                self.priority_callback_map[None] = [priority_cb]
            else:
                self.priority_callback_map[None].append(priority_cb)
        else:
            if msg_class._msgtype not in self.priority_callback_map:
                self.priority_callback_map[msg_class._msgtype] = [priority_cb]
            else:
                self.priority_callback_map[msg_class._msgtype].append(
                    priority_cb)

    def get_callbacks(self, msg):
        temp_list = self.priority_callback_map.get(
            None, []) + self.priority_callback_map.get(msg._msgtype, [])
        temp_list.sort()
        return temp_list

    def remove_callback(self, msg_class, priority, callback):
        if msg_class is None:
            self.priority_callback_map[None].remove(
                CallbackWrapper(priority, callback, None))
        else:
            self.priority_callback_map[msg_class._msgtype].remove(
                CallbackWrapper(priority, callback, None))


class CallbackWrapper:
    def __init__(self, priority, callback, check_func=None, loop=None, clean_up_func=None, timeout=None, timeout_cb=None):
        self.priority = priority
        self.callback = callback
        self.check_func = check_func or (lambda x: True)
        self.clean_up_func = clean_up_func
        self.loop = loop
        self.timer_handle = None
        self.timeout_cb = timeout_cb
        if timeout:
            self.loop.call_soon_threadsafe(self.schedule_timer, timeout)

    def schedule_timer(self, timeout):
        self.timer_handle = self.loop.call_later(timeout, self.timeout_cb)

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority and self.callback == other.callback

    def __call__(self, session_name, msg):
        if self.check_func(msg) or msg is None:
            if self.timer_handle:
                self.timer_handle.cancel()
            if self.clean_up_func:
                self.clean_up_func()
            return self.callback(session_name, msg)

        return None

    def __repr__(self):
        return f"{self.priority},{self.callback}"
