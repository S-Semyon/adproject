from .template import Template
from ..sys_control.runusadmin import runadmin
from os import path, name

class Template_DND(Template): 
    def start(self):
        if name == "nt":
            runadmin(path.abspath("project/templates/scripts/dnd_turn.bat"))
        else:
            pass