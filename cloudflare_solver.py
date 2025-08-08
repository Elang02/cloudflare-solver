
from seleniumbase import SB
import time

def solve_cloudflare_captcha(url):
    with SB(uc=True) as sb:
        for i in range(10):
            sb.uc_open_with_reconnect(url)
            sb.wait_for_ready_state_complete(timeout=15)
            sb.uc_gui_click_captcha()
            time.sleep(20)
            cookies = sb.get_cookies()
            cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
            if 'cf_clearance' in cookies_dict:
                print('Captcha Solved')
                break
            else:
                print(sb.driver.page_source)
                print(sb.get_cookies())
                continue
        sb.driver.quit()
        return cookies_dict

cookies = solve_cloudflare_captcha('https://buzz.tips/')
print(cookies)