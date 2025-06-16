from dataclasses import dataclass
from .adg2128_axis import Axis

@dataclass(frozen=True)
class ADG2128Pin:
    axis: Axis
    channel: int

    def __post_init__(self):
        if self.axis == Axis.X and not (0 <= self.channel <= 11):
            raise ValueError(f'Invalid X channel: {self.channel}')
        if self.axis == Axis.Y and not (0 <= self.channel <= 7):
            raise ValueError(f'Invalid Y channel: {self.channel}')

# Define the bus pins that are used to connect the switch matrices
BUS_PIN_X = ADG2128Pin(Axis.X, 6)
BUS_PIN_Y = ADG2128Pin(Axis.Y, 7)

def get_bus_pin(pin: ADG2128Pin) -> ADG2128Pin:
    """Returns the appropriate bus pin based on the given pin's axis.
    If the pin is on the Y axis, it needs the X bus pin, and vice versa."""
    return BUS_PIN_X if pin.axis == Axis.Y else BUS_PIN_Y