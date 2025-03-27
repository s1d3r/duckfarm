import requests
import logging

from models import FlagStatus, SubmitResult

logger = logging.getLogger(__name__)

TIMEOUT = 5

def submit_flags(flags, config):
    host = config['SYSTEM_HOST']
    port = config['SYSTEM_PORT']
    team_id = config['TEAM_TOKEN']
    base_url = f"http://{host}:{port}/flag"

    for item in flags:
        flag = item.flag
        params = {'teamid': team_id, 'flag': flag}
        try:
            response = requests.get(base_url, params=params, timeout=TIMEOUT)
            status_code = response.status_code
            response_text = response.text.strip()
        except requests.exceptions.RequestException as e:
            logger.warning("Failed to submit flag %s: %s", flag, e)
            yield SubmitResult(flag, FlagStatus.QUEUED, str(e))
            continue

        if status_code == 200:
            status = FlagStatus.ACCEPTED
        elif status_code in (400, 403):
            status = FlagStatus.REJECTED
        else:
            logger.warning("Unexpected status code %d for flag %s: %s", status_code, flag, response_text)
            status = FlagStatus.QUEUED

        yield SubmitResult(flag, status, response_text)
