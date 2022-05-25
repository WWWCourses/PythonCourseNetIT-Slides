import os

def get_server_root_path():
	return os.path.dirname(os.path.abspath(__file__))

SERVER_ROOT_PATH = get_server_root_path()

def get_file_path(filename):
	return os.path.abspath(filename)

if __name__=='__main__':
	# print(__file__)
	# file_path = get_file_path('front-end/login.html')
	# print(file_path)
	# get_server_root_path()

	path = os.path.join('./front-end', '/index.html')
	print(path)