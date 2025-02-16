from proto.schemata.board_schema    import MAKERPI_RP2040, PI_PICO
from proto.schemata.cservo_schema   import FS90R
from proto.schemata.dc_schema       import EE_YELLOW
from proto.schemata.system_schema   import system_schema

# the schema for the system as a whole -- includes the board schema, motor
# schemata, etc.
SYSTEM: system_schema = system_schema(
    board=MAKERPI_RP2040,
    cservo=FS90R,
    dc=EE_YELLOW,
)
