from ..logging import logger
from ..settings import Settings
from ..templates import templates
from os import system

class Master_Creating_Scripts:
    def __init__(self, logger: logger, settings: Settings) -> None: # type: ignore
        self.logger = logger
        self.settings = settings

    def create_script(self, 
                      name_script: str,
                      startup_programs: list[tuple[str, str]] = [],
                      template: list = []
                      ) -> None:
        """Мастер создания сценариев"""
        scripts = self.settings.load("scripts")
        if not scripts:
            scripts = {}
        scripts[name_script] = {"startup_programs": startup_programs, "template": template}
        self.settings.save("scripts", scripts)
        self.logger.info("[Master_Creating_Scripts] Script creating")
    
    def start_script(self, name_script: str) -> None:
        script = self.settings.load("scripts")[name_script] # type: ignore
        for template in script["template"]: 
            template[template].start()
            self.logger.info(f"[Master_Creating_Scripts] Template start {template}")
        for program in script["startup_programs"]: 
            system(f'"{program[0]}" "{program[1]}"')
            self.logger.info(f"[Master_Creating_Scripts] Script start {program}")
        
