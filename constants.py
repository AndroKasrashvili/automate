from enum import Enum


class CommandType(Enum):
    COMMAND = "Command"


class CommandId(Enum):
    SYNTHESIZE_TOUCH_INPUT = "SynthesizeTouchInput"


class TouchType(Enum):
    DOWN = "down"
    UP = "up"

