from colorama import Fore
def add(site):
  a = ("http://"+site)
  print(Fore.YELLOW+a)
  with open('res.txt', 'a') as writer:
	      writer.write("http://"+site+"\n")
  
target = input(Fore.WHITE+"Input your list :")
for site in open(target, 'r').read().splitlines():
  add(site)
