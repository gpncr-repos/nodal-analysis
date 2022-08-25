import numpy as np
import pytest


@pytest.fixture
def generate_data_for_tests():
    return {
        "vlp": {
            "q_liq": [0, 30, 60, 90, 120, 150],
            "p_wf": [200, 190, 180, 175, 185, 200]
        },
        "ipr": {
            "q_liq": [0, 30, 60, 90, 120, 150],
            "p_wf": [200, 180, 160, 140, 120, 100]
        }
    }


def test_calc_model_success(api_client, generate_data_for_tests):
    response = api_client.post("nodal/calc",
                               json=generate_data_for_tests)
    assert response.status_code == 200
    result = response.json()
    assert result
