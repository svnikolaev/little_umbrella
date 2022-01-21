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

    try:
        _msg = template_sting
        logger.info(_msg)
    except NameError:
        logger.error('Can not get the template_string')


if __name__ == "__main__":
    import subprocess
    run_service = BASEDIR.joinpath('run_service.py')
    service = Path(__file__).parent.name
    args = '-nvt'  # no create logfile, verbose, testing
    print(f'TEST RUN of service "{service}" with args "{args}":\n')
    subprocess.call(['python', run_service, args, service])
    print('\nTEST RUN finished')
