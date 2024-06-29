import pytest
from time import sleep
from selenium import webdriver
from Base_page.input_baidu import BaiduPage
from util.utils import read_yaml
import allure

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    # 这个 fixture 使用 yield 语句在测试用例执行前初始化浏览器，在测试用例执行完后关闭浏览器
    driver.quit()


# 通过 @pytest.mark.usefixtures("driver") 将 fixture 应用于测试类，确保 driver 在整个测试类中可用。
@pytest.mark.usefixtures("driver")
class TestBaidu:
    @allure.feature('输入模块')
    @pytest.mark.parametrize("data", read_yaml("input_data.yaml")["search_terms"])
    def test_baidu_search_case(self, driver, data):
        search_term = data["term"]
        expected_title = data["expected_title"]
        index = data["index"]

        page = BaiduPage(driver)
        page.open()
        page.search_input(search_term)
        page.search_button()
        sleep(2)
        # 获取当前页面的标题
        actual_title = driver.title
        # assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        try:
            # 断言标题是否与预期相符
            assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"
        except AssertionError as e:
            # 捕获断言错误并打印提示信息，而不是抛出错误
            # 捕获断言错误并打印更详细的提示信息
            print(f"参数{index}：'{search_term}'断言失败:")
            print("预期：" + expected_title)
            print("实际：" + actual_title)
            # 打印出当前参数信息
            print(f"参数信息：{data}")
            # 将 AssertionError 抛出，这样 pytest 仍能够正确识别测试失败
            raise e  # 可以选择注释掉这行，以便只打印信息，而不抛出错误






if __name__ == '__main__':
    pytest.main()

