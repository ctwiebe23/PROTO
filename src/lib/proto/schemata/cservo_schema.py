from proto.general.functions    import bound_power

class cservo_schema:
    """
    A continuous servo schema that details the motor frequency and a power
    scaler that takes one argument -- power -- and scales it to a valid
    throttle.

    The power scaler should intake a power in the range [-100,100] and return
    a throttle in the range [-1,1], along with whatever other modifications
    are necessary.
    """

    def __init__( self, frequency: int, power_scaler ):
        self.frequency      = frequency
        self.power_scaler   = power_scaler

#=============================================================================#
# PRESETS
#=============================================================================#

FS90R: cservo_schema = cservo_schema(
    frequency=50,
    power_scaler=lambda power : 0.8 if power > 0 else -1,
)
