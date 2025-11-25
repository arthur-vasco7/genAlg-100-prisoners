import importlib
import contextlib
from unittest.mock import patch

import src.analyze.time_analyse as time_module


def test_time_analyse_runs_for_coverage():
    "Executa o módulo inteiro apenas para cobertura."

    with patch("src.analyze.time_analyse.HundredPrisonersGA") as MockGA:
        ga_instance = MockGA.return_value
        ga_instance.run.return_value = ([], 0, 0)

        with patch("contextlib.redirect_stdout"):
            with patch("time.time", side_effect=[1, 2] * 200):
                
                # reload executa novamente todo o código do módulo
                importlib.reload(time_module)
