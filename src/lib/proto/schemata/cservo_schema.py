from proto.general.functions    import bound_power

class cservo_schema:
    """
    A continuous servo schema that details the motor frequency and a power
    scaler that takes one argument -- power -- and scales it to a valid power.
    """
    
    def __init__( self, frequency: int, power_scaler ):
        self.FREQUENCY      = frequency
        self.POWER_SCALER   = power_scaler

#=============================================================================#
# PRESETS
#=============================================================================#

FS90R: cservo_schema = cservo_schema(
    frequency=50,
    power_scaler=lambda power : bound_power(
        power,
        (0.1,0.8) if power > 0 else (0.3,1),
    ),
)
