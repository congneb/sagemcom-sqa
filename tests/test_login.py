import pytest
from pages.login_page import LoginPage
from pages.wifi_page import WifiPage
from utils.ssh_client import get_ubus_tr181_ssid

def test_case_1_login(page, gateway_info):
    login_pg = LoginPage(page, gateway_info["url"])
    login_pg.navigate()
    login_pg.login(gateway_info["user"], gateway_info["pass"])
    
    # Verify login thành công (check URL hoặc element đặc trưng)
    assert "/dashboard" in page.url or page.is_visible("text=Logout")

def test_case_2_change_ssid_and_verify_ubus(page, gateway_info):
    new_ssid_name = "prplOS_Test_5G"
    
    # Step 1: UI Action
    login_pg = LoginPage(page, gateway_info["url"])
    login_pg.navigate()
    login_pg.login(gateway_info["user"], gateway_info["pass"])
    
    wifi_pg = WifiPage(page)
    page.goto(f"{gateway_info['url']}/network/wifi") # Link trực tiếp page wifi
    wifi_pg.change_ssid(new_ssid_name)
    
    # Step 2: DUT Verification (TR-181 via ubus)
    ubus_output = get_ubus_tr181_ssid(
        gateway_info["ssh_host"], 
        gateway_info["user"], 
        gateway_info["pass"]
    )
    
    assert new_ssid_name in ubus_output, f"SSID trên DUT không khớp! Thực tế: {ubus_output}"
