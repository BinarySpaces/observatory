from datetime import datetime, timedelta
from typing import Optional

import requests

from src.telescopes.domain import ITelescopeAPI


class LCOTelescopeAPI(ITelescopeAPI):
    """
    LCO (Las Cumbres Observatory) API client.
    Submits observation requests to the LCO network via their REST API.
    """

    def __init__(self, token: Optional[str], proposal_id: str) -> None:
        """Initializes the LCO API client with an authentication token and proposal ID."""
        self.token = token
        self.proposal_id = proposal_id
        self.base_url = 'https://observe.lco.global/api'

    def point(self, ra: float, dec: float) -> bool:
        """Submits an observation request to the LCO network."""
        headers = {
            'Authorization': f'Token {self.token}',
            'Content-Type': 'application/json'
        }

        start_date = datetime.now()
        end_date = start_date + timedelta(days=30)

        short_name = f'Star_{ra:.2f}_{dec:.2f}'

        target = {
            'name': short_name,
            'type': 'ICRS',
            'ra': ra,
            'dec': dec,
            'epoch': 2000
        }

        instrument_config = {
            'exposure_time': 60.0,
            'exposure_count': 1,
            'optical_elements': {'filter': 'V'}
        }

        configuration = {
            'type': 'EXPOSE',
            'instrument_type': '1M0-SCICAM-SINISTRO',
            'target': target,
            'instrument_configs': [instrument_config],
            'acquisition_config': {},
            'guiding_config': {},
            'constraints': {
                'max_airmass': 2.0,
                'min_lunar_distance': 30
            }
        }

        request_group = {
            'name': short_name,
            'proposal': self.proposal_id,
            'ipp_value': 1.05,
            'operator': 'SINGLE',
            'observation_type': 'NORMAL',
            'requests': [{
                'configurations': [configuration],
                'windows': [{
                    'start': start_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'end': end_date.strftime('%Y-%m-%d %H:%M:%S')
                }],
                'location': {'telescope_class': '1m0'}
            }]
        }

        try:
            response = requests.post(
                f'{self.base_url}/requestgroups/',
                headers=headers,
                json=request_group,
                timeout=30
            )

            if response.status_code == 201:
                print('✅ Observation request submitted successfully!')
                print(f'   Request ID: {response.json().get("id")}')
                return True
            else:
                print(f'❌ Failed to submit request. Status: {response.status_code}')
                print(f'   Response: {response.text}')
                return False

        except Exception as e:
            print(f'❌ Error connecting to LCO API: {e}')
            return False
