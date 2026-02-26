from proto.general.functions import bound_power


class dc_schema:
    """
    A DC schema that details the motor frequency and a power scaler that takes
    one argument -- power -- and scales it to a valid throttle.

    The power scaler should intake a power in the range [-100,100] and return
    a throttle in the range [-1,1], along with whatever other modifications
    are necessary to make the motor speed scale as expected.
    """

    def __init__(self, frequency: float, power_scaler):
        self.frequency = frequency
        self.power_scaler = power_scaler


# =============================================================================#
# PRESETS
# =============================================================================#

EE_YELLOW: dc_schema = dc_schema(
    frequency=50,
    power_scaler=lambda power: bound_power(power, (0.3, 1)),
)

N20: dc_schema = dc_schema(
    frequency=50e3,
    power_scaler=lambda power: bound_power(power, (0, 1)),
)
