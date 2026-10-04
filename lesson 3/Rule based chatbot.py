import re,random 
from colorama  import Fore,init
init(autoreset=True)

destinations = {

"beaches": ["Bali", "Maldives", "Phuket"],

"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

"cities": ["Tokyo", "Paris", "New York"]

}

jokes = [

"Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"

]

def normalize_input(text):
  return re.sub(r'\s+',' ',text.strip() lower())

def recommend_destination():
   print (Fore.MAGENTA + "TravelBot: mountains, beaches, or cities?")
   
   preference = input(Fore.BLUE + "You: ")
   preference = normalize_input(preference)
   
   if preference in destinations:
       suggestion = random.choice(destinations[preference])
       print(Fore.PINK + f"TravelBot: How about {suggestion}?")
       print(Fore.YELLOW + "TravelBot: Do you like it? (yes/no)")
       answer = input(Fore.LIME + "You: ").lower()
       if answer == "yes":
           print(Fore.GOLD + f"TravelBot: Great! I hope you have a wonderful trip!{suggestion}")
       if answer == "no":
              print(Fore.AQUA + "TravelBot: No worries! Let's try again.")
              recommend_destination()
              print(Fore.RED+ "TravelBot: Do you like it? (yes/no)")
              answer = input(Fore.GREY + "You: ").lower()
              