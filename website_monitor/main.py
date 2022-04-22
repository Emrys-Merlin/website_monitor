import logging
from time import sleep

import hydra
from omegaconf import DictConfig
from prometheus_client import Gauge, start_http_server
from requests import get

logger = logging.getLogger(__name__)


def get_website_status(url: str) -> int:
    """Return the status code of a website

    Parameters
    ----------
    url : str
        url to website

    Returns
    -------
    int
        status code
    """
    return get(url).status_code


@hydra.main(config_path='..', config_name='config.yaml')
def main(cfg: DictConfig):

    start_http_server(port=cfg.port)

    gauge = Gauge(
        'http_status_code',
        'HTTP status code of visited websites',
        ['url', 'name'],
    )

    while True:
        for name, url in cfg.websites.items():
            status = get_website_status(url)
            logger.info(f'Status of {name} is {status}')
            logger.debug(f'URL of {name} is {url}')
            gauge.labels(url=url, name=name).set(status)

        sleep(cfg.sleep_time)


if __name__ == "__main__":
    main()
