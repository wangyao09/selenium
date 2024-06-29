import pytest
import os





if __name__ == '__main__':
    pytest.main(['-vs', './test_cases', "--alluredir=temp"])
    os.system('allure generate ./temp -o ./reports --clean ')





