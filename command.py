from schedule import Schedule


class Command:
    def __init__(self, cmd_type, command_id, touch_schedule):
        self.type = cmd_type
        self.commandId = command_id
        self.touchSchedule = touch_schedule

    @classmethod
    def from_json(cls, command_dict: dict) -> 'Command':
        return cls(cmd_type=command_dict['type'],
                   command_id=command_dict['commandId'],
                   touch_schedule=[Schedule.from_json(schedule_dict) for schedule_dict in command_dict['touchSchedule']]
                   )
