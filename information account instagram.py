import requests, os
from user_agent import generate_user_agent
from colorama import Fore,Style

b0 = Style.RESET_ALL
b1 = Fore.YELLOW
b4 = Fore.LIGHTCYAN_EX
b5 = Fore.LIGHTYELLOW_EX

os.system('cls' if os.name == 'nt' else 'clear')
logo = f"""{b1}
     ____                         __  __ 
    / ___| _   _ _ __   ___ _ __  \ \/ / 
    \___ \| | | | '_ \ / _ \ '__|  \  /  
     ___) | |_| | |_) |  __/ |     /  \  
    |____/ \__,_| .__/ \___|_|    /_/\_\ {b4}v6
{b1}                |_|                     
{b5}Coded By ABOUD SUPER X 747 || Follow me for more.
{b1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {b1}instagram==> {b0}aboud_coding
    {b1}github==> {b0}Dark-Man747

    """
print(logo)

target = input('Enter Target ==> ')

url = f"https://www.instagram.com/{target}/?__a=1&__d=dis"
head = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip,deflate,br',
    'accept-language':'en-US,en;q=0.9,ar;q=0.8',
    'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
    'user-agent': 'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)'#generate_user_agent(),
    }
information = requests.get(url,headers=head).json()

id = (information['graphql']['user']['id'])
name = (information['graphql']['user']['full_name'])
Bio = (information['graphql']['user']['biography'])
Followers = (information['graphql']['user']['edge_followed_by']['count'])
Following = (information['graphql']['user']['edge_follow']['count'])
url = (information['graphql']['user']['external_url'])
private = (information['graphql']['user']['is_private'])
business = (information['graphql']['user']['is_business_account'])
posts = str(information['graphql']['user']["edge_owner_to_timeline_media"]["count"])
re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}",headers=head)
ree = re.json()
dat = ree['date']

print(f"""
{b0}[{b1}+{b0}] {b4}Id {b1}:{b0} {id}
{b0}[{b1}+{b0}] {b4}Name {b1}:{b0} {name}
{b0}[{b1}+{b0}] {b4}Bio {b1}:{b0} {Bio}
{b0}[{b1}+{b0}] {b4}Followers {b1}:{b0} {Followers}
{b0}[{b1}+{b0}] {b4}Following {b1}:{b0} {Following}
{b0}[{b1}+{b0}] {b4}posts {b1}:{b0} {posts}
{b0}[{b1}+{b0}] {b4}date :{b0} {dat}
{b0}[{b1}+{b0}] {b4}Bio link {b1}:{b0} {url}
{b0}[{b1}+{b0}] {b4}Private {b1}:{b0} {private}
{b0}[{b1}+{b0}] {b4}Business Account {b5}:{b0} {business}
""")
