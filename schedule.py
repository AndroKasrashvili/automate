
class Schedule:

    def __init__(self, time, touch_type, x, y):
        self.time = time
        self.touchType = touch_type
        self.x = x
        self.y = y

    @classmethod
    def from_json(cls, schedule_dict: dict) -> 'Schedule':
        return cls(time=schedule_dict['time'],
                   touch_type=schedule_dict['touchType'],
                   x=schedule_dict['x'],
                   y=schedule_dict['y']
                   )




