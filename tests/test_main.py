from unittest.mock import patch
from src.main import main
import runpy

def test_main_runs_without_errors():
    "Tests that calling main() does not raise any exception."

    try:
        main()
    except Exception as e:
        assert False, f"main() raised an unexpected exception: {e}"

def test_main_output_format(capsys):
    "Tests that main() prints valid formatted output to stdout."

    main()  # run the function

    captured = capsys.readouterr().out

    # Check expected substrings
    assert "The best Fitness" in captured
    assert "Num Generation" in captured
    assert "Nums Boxes" in captured

def test_main_if_block_runs_as_script():
    "Execute the module as a script (sets __name__ == '__main__')."
    runpy.run_module("main", run_name="__main__")