import getpass
url = dict(
    base = 'https://host.example.com/boxplorer',
    choices = 'https://host.example.com/boxplorer/choices/',
)

auth = dict(
    user = getpass.getuser(),
    password = getpass.getpass(),
)
dest_dir = '/tmp/'
