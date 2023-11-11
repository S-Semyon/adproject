import asyncio
import subprocess

async def worker(program: str, arg: str, *, logger) -> None:
    logger.info(subprocess.run([program, arg], shell=True))

async def start_programs(programs: list[tuple[str, str]], logger) -> None:
    workers = []
    for program in programs:
        workers.append(worker(*program, logger=logger))
    await asyncio.gather(workers) # type: ignore