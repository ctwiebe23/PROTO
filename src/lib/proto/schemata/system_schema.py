from proto.schemata.board_schema    import board_schema, MAKERPI_RP2040
from proto.schemata.cservo_schema   import cservo_schema, FS90R
from proto.schemata.dc_schema       import dc_schema, EE_YELLOW

class system_schema:
    """
    A system schema that details the components used in the kit as a whole.
    """
    
    def __init__(
        self,
        board:  board_schema    = None,
        cservo: cservo_schema   = None,
        dc:     dc_schema       = None,
    ):
        self.BOARD  = board
        self.CSERVO = cservo
        self.DC     = dc

#=============================================================================#
# PRESETS
#=============================================================================#

PROTO_DEV_V1: system_schema = system_schema(
    board=MAKERPI_RP2040,
    cservo=FS90R,
    dc=EE_YELLOW,
)
