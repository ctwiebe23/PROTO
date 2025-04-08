class servo_schema:
    """
    A servo schema that details the duty cycle and frequency.
    """

    def __init__(self, duty_cycle: int, frequency: int):
        self.duty_cycle = duty_cycle
        self.frequency = frequency


# =============================================================================#
# PRESETS
# =============================================================================#

SMRAZA_S51: servo_schema = servo_schema(
    duty_cycle=2**15,
    frequency=50,
)
