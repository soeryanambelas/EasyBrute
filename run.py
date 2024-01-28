import os
	
if __name__ == "__main__":
	try:os.system("git pull")
	except:pass
	try:os.system("mkdir Live")
	except:pass
	try:os.system("mkdir Chek")
	except:pass
	__import__("Simple").menu()