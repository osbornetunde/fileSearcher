

def main():
	print_header()
	folder = get_folder_from_user()
	if not folder:
		print("Sorry we cant search that location.")
		return

	text = get_search_text_from_user()
	if not text:
		print("We can't search for nothing!")

def print_header():
	pass

def get_folder_from_user():
	pass

def get_search_text_from_user():
	pass

def search_file():
	pass

if __name__ = __main__:
	main()