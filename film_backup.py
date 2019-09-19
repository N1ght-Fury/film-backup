import os

def write_films_to_file(path, film_list):
	sorted_films = []
	with open(path, 'r') as f:
		sorted_films = f.readlines()
		for name in film_list:
			if (not check_if_film_exists(name)):
				sorted_films.append(name)

		sorted_films.sort()

	with open(path, 'w+') as f:
		for name in sorted_films:
			f.write(name)

def check_if_film_exists(name):
	with open(r'C:\Users\Google Drive\Notes\films.txt', 'r') as f:
		films = f.readlines()

		for i in films:
			if (i == name):
				return True

	return False

def get_film_names(path):
	film_names = []
	for i in os.listdir(path):
		film_names.append(i + '\n')

	return film_names

def start_backup_and_sync(path):
	os.startfile(path)

def main():
	path = r'C:\Users\Google Drive\Notes\films.txt'
	films = get_film_names(os.getcwd())
	write_films_to_file(path, films)
	start_backup_and_sync(r'C:\Program Files\Google\Drive\googledrivesync.exe')

if __name__ == '__main__':
	main()