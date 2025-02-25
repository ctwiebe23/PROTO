from proto.schemata.board_schema    import board_schema, MAKERPI_RP2040, PI_PICO
from proto.schemata.cservo_schema   import cservo_schema, FS90R
from proto.schemata.dc_schema       import dc_schema, EE_YELLOW
from proto.schemata.servo_schema    import servo_schema, SMRAZA_S51

class system_schema:
    """
    A system schema that details the components used in the system as a whole;
    a 'top-level' schema.
    """

    def __init__(
        self,
        board:  board_schema    = None,
        cservo: cservo_schema   = None,
        dc:     dc_schema       = None,
        servo:  servo_schema    = None,
    ):
        self.board  = board
        self.cservo = cservo
        self.dc     = dc
        self.servo  = servo

#=============================================================================#
# PRESETS
#=============================================================================#

PROTO_DEV_1: system_schema = system_schema(
    board=MAKERPI_RP2040,
    cservo=FS90R,
    dc=EE_YELLOW,
    servo=SMRAZA_S51,
)

PROTO_DEV_PICO: system_schema = system_schema(
    board=PI_PICO,
    cservo=FS90R,
    servo=SMRAZA_S51,
)
