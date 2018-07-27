from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


from customed_selenium.auth_proxy import create_proxyauth_extension
from headers import UserAgent


def generate_chrome_options(
    image=False, js=True, *, headers='common_android', proxy=None,
    extension_path=None,
):
    options = ChromeOptions()

    ua = UserAgent()
    current_headers = getattr(ua, headers)()
    argument_ua = "user-agent={}".format(current_headers)
    options.add_argument(argument_ua)

    argument_dis_notifications = "--disable-notifications"
    options.add_argument(argument_dis_notifications)

    argument_exp_dis_image = ("prefs", {'profile.managed_default_content_settings.images': 2})
    if not image:
        options.add_experimental_option(*argument_exp_dis_image)

    argument_exp_dis_js = ("prefs", {'profile.managed_default_content_settings.javascript': 2})
    if not js:
        options.add_experimental_option(*argument_exp_dis_js)

    # extension_path = '/home/parallels/Downloads/GoogleHelper_1.2.0.crx'
    if extension_path:
        options.add_extension(extension_path)

    # proxy = "socks5://104.207.159.40:9100"
    if proxy:
        if proxy.get('password'):
            proxyauth_plugin_path = create_proxyauth_extension(
                proxy_host=proxy['ip'],
                proxy_port=int(proxy['port']),
                proxy_username=proxy['user'],
                proxy_password=proxy['password'],
            )
            options.add_extension(proxyauth_plugin_path)
        else:
            argument_proxy = "--proxy-server={}://{}:{}".format(
                proxy['scheme'], proxy['ip'], proxy['port']
            )
            options.add_argument(argument_proxy)
    return options
