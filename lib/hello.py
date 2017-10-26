# Default is "World"
# Author: Scott Humber (scott@somewhere.com)
import sys
from greeter import Greeter

name = sys.argv[1] if len(sys.argv) > 1 else 'World'
greeter = Greeter(name)
print greeter.greet()