# importing necessary libiraries
#---------------------------------------------------------------------------------------------------------------
from termcolor import colored
from sys import exit
import requests
# ----------------------------- Start of programme -------------------------------------------------------------------------------
start='''                                     
	 ______     __  __     ______     ______     __  __     ______     __  __    
	/\  ___\   /\ \_\ \   /\  ___\   /\  ___\   /\ \/ /    /\  __ \   /\ \/ /    
	\ \ \____  \ \  __ \  \ \  __\   \ \ \____  \ \  _"-.  \ \ \/\ \  \ \  _"-.  
	 \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
	  \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/ 
	 
		                                    
               Coded By Mutawakkil Abduldafe
    '''
print(colored(start,'magenta'))
print(colored('   NOTES : your list should be out of https:// at the start of domain because the program adds it automaticly ','yellow'))

# asking filename and output filename

site_file= str(input('Your sites filename please : '))
output_file=str(input('Your output filename please : '))
# --------------------------------- Handling Inputs and requesting the sites ---------------------------------------------------------------------------
# observing the working sites given in filenme and storing the 200 responses of them at output_file you've chosen
with open (output_file,'w') as o:
	with open(site_file,'r') as f:
		for site in f.readlines():
			try:
				site= site.strip('\n')
				sitecolor=colored(site,'cyan')
				site="https://"+site
				request = requests.get(site,timeout=3)
				print(sitecolor,' ==> ',colored(request.status_code,'yellow'))
				if request.ok == True:
					site='\n'+site
					o.write(site)
				else:
					o.write('either no host has 200 response or you connection is bad check the connection please')
						
			except:
						print(colored(site,'red'),colored('isnt up','red'))

exit()		
# ------------------------------------------- End , Hope you like it ! ---------------------------------------------------------------------	
