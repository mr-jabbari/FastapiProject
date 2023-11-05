from Tests import test_root
import pytest
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pkg_resources")

if __name__ == '__main__':
    pytest.main(["-v", __file__])
