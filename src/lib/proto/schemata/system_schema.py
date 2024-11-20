from proto.schemata.board_schema    import board_schema
from proto.schemata.cservo_schema   import cservo_schema
from proto.schemata.dc_schema       import dc_schema

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
    ):
        self.BOARD  = board
        self.CSERVO = cservo
        self.DC     = dc
