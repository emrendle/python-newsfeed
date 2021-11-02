# .home syntax directs the program to find the module named home in the current directory
# then we want to import the bp object but we rename it to home for practicality's sake
# this allows us to simply import home in the app's init file and call it home

from .home import bp as home
from .dashboard import bp as dashboard