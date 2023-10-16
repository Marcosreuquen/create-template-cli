import argparse
from app.main import get_args


def test_get_args():
    # Test case 1: Valid type and output directory provided
    args = get_args(["type1", "type2"])
    assert args.type == "type1"
    assert args.output == "./dist"

    # Test case 2: Valid type provided, default output directory used
    args = get_args(["type1", "type2"])
    assert args.type == "type2"
    assert args.output == "./dist"

    # Test case 3: Valid type and custom output directory provided
    args = get_args(["type1", "type2"])
    assert args.type == "type1"
    assert args.output == "/path/to/output"

    # Test case 4: Required argument missing
    try:
        get_args(["type1", "type2"])
        assert False, "Expected argparse.ArgumentError"
    except argparse.ArgumentError:
        pass

    # Test case 5: Invalid type provided
    try:
        get_args(["type1", "type2"])
        assert False, "Expected argparse.ArgumentError"
    except argparse.ArgumentError:
        pass
