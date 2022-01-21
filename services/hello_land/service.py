import logging
import sys
from pathlib import Path

try:
    from run_service import BASEDIR
except ModuleNotFoundError:
    BASEDIR = Path(__file__).parents[2]
    sys.path.insert(0, str(BASEDIR))
from connectors.template_connector import template_sting

logger = logging.getLogger(__name__)


def main(config: dict) -> None:
    logger.debug(f'Config dict: {config}')
    logger.info(f'basedir: {BASEDIR}')
    logger.info(f'service {__name__} logger.info testing: {template_sting}')
    logger.debug(f'service {__name__} logger.debug testing: {template_sting}')


if __name__ == '__main__':
    import subprocess
    run_service = BASEDIR.joinpath('run_service.py')
    service = Path(__file__).parent.name
    args = '-nvt'  # no create logfile, verbose, testing
    print(f'TEST RUN of service "{service}" with args "{args}":\n')
    subprocess.call(['python', run_service, args, service])
    print('\nTEST RUN finished')
