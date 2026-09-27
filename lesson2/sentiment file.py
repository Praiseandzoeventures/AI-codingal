import  colorama  
from  colorama  import Fore, Style
from textblob import TextBlob
colorama.init()
print (f'{Fore.AQUA} 🐍 Welcome to  sentiment Spy!🐍 {Style.RESET_ALL}')
User_name=input(f"{Fore.MAGENTA}Please enter your name : {Style.RESET_ALL}").strip()
if User_name:
    user_name='MYSTERY AGENT'
conversation_history=[] 

print(f'\n{Fore.RED}Hello, Agent {User_name}! {Style.RESET_ALL}')
print(f'{Fore.YELLOW}I am your sentiment spy, I will analyze your sentences  with TextBlob and show you the results.{Style.RESET_ALL}')
print(
f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n"
)
