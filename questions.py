'''
Using Python 2.7, or 3.3-3.5 syntax/semantics, please fill out the bodies of
the included functions to include implementations of what is described in the
docstrings.
'''
import re 

def list_of_integers():
    '''Returns a list of integers from 17 to 100 that are evenly divisible by 11.'''
    list = []
    for i in range(17,100):
        if (i % 11 == 0):
            list.append(i)  
    return list 

print "\n"
print "===== list_of_integers ====="
print list_of_integers()
print "============================"
print "\n"
    

def dict_mapping():
    '''
    Returns a dictionary mapping integers to their 2.75th root for all integers
    from 2 up to 100 (including the 2.75th root of 100).
    '''
    nth = 2.75
    dict = {x: x**(1/nth) for x in range(2,101)}
  
    return dict

print "\n"
print "====== dict_mapping() ======"
print dict_mapping()
print "============================"
print "\n"

def find_ips(ips):
    '''
    Returns a list of ip addresses of the form 'x.x.x.x' that are in the input
    string and are separated by at least some whitespace.
    >>> find_ips('this has one ip address 127.0.0.1')
    ['127.0.0.1']
    >>> find_ips('this has zero ip addresses 1.2.3.4.5')
    []
    '''
    # Need to import re
    # First, to filter down the addresses with 4 sets of numbers use count() to find total 3 '.'s after splitting
    split_string = ips.split(" ")
    filtered_string = []
    valid_ip = []
    for string in split_string:
      if (string.count(".") == 3):
        filtered_string.append(string)
    
    for ip in filtered_string:
        checked = re.findall( r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',ip)
        if len(checked) != 0:
            valid_ip.extend(checked)
    
    return valid_ip


s1 = "192.168.0.1 sample string 255.255.255.255 255.255.255.256 123.32.102.2 hello 674.11.10.2 world 10.0.0.1 1.2.3.4.5"
s2 = "192.168.0.1000 sample string 255.255.255.256 hello 674.11.10.2 world 1.2.3.4.5"


print "\n"
print "======== find_ips() ========"
print(find_ips(s1))
print "============================"
print "\n"


def generate_cubes_until(modulus):
    '''
    Generates the cubes of integers greater than 0 until the next is 0 modulo
    the provided modulus.
    >>> list(generate_cubes_until(25))
    [1, 8, 27, 64]
    '''
    list = []
    index = 1 
    while True:
      if (index**3 % modulus == 0):
        return list 
      else:
        list.append(index**3)
        index+=1

print "\n"
print "======== generate_cubes_until() ========"
print generate_cubes_until(25)
print "========================================"
print "\n"

def total_size(filenames):
    '''
    Given a list of filenames in Apache Common Log format, return a mapping
    of the total number of responses of different types to the total number of
    bytes returned by all responses of that type.
    >>> total_size(['/var/log/httpd.log', '/var/log/httpd.log.1'])
    {'200': 7362899, '404': 28710, ...}

    The format can be found: https://en.wikipedia.org/wiki/Common_Log_Format
    And an example line of common log format is:
    127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
    '''
    library = {}
    # total byte counter
    total = 0

    for filename in filenames:

        # Open a file
        file = open(filename, "rw+")
        # print "Name of the file: ", file.name

        line = file.readlines()
        # print "Read Line: %s" % (line)
        
        for x in line:
            # print x 
            status = re.findall( r'\b(" "1[0-9][0-9]|2[0-9][0-9]|3[0-9][0-9]|4[0-9][0-9]|5[0-9][0-9]" ")\s\b',x)
            byte = re.findall( r'\b(\d+$)\b',x)
            
            for y in status:
                
                library.setdefault(y,0)
                
                for z in byte:
                    total += int(z)
                    library[y] += int(z)
                
        file.close()

    return library 

# log1.log and log2.log files are local files I created to test =)
result = total_size(["log1.log","log2.log"])

print "\n"
print "======== total_size() ========"
print "Here's the total byte count of each response status: ", result
print "=============================="
print "\n"

def check_type(typ):
    '''
    Write a function decorator that takes an argument and returns a decorator
    that can be used to check the type of the argument to a 1-argument function.
    Should raise a TypeError if the wrong argument type was passed.
    >>> @check_type(int)
    ... def test(arg):
    ...   print arg
    ...
    >>> test(4)
    4
    >>> test(4.5) # raises TypeError because 4.5 isn't an int type
    '''

    def decorator(f):
        def wrapper(arg):
            if (isinstance(arg, typ)):
                f(arg)                
            else:   
                try:
                    raise TypeError    
                except TypeError:
                    print("Argument and data type don't match")
                
        return wrapper 
    return decorator

@check_type(int)
def test(arg):
    print(arg)



print "\n"
print "======== check_type() ========"
print "test(4): " , test(4), #4
print "test(4.5): ", test(4.5) #TypeError: argument and datatype don't match
print "=============================="
print "\n"


def left_turn(one, two, three):
    '''
    Given three points return True if they form a left turn, False if they do not
    >>> left_turn([0, 0], [2, 2], [2, 3])
    True
    '''

    '''
        1. use 'one' and 'two' coordinates to find direction and slope and which quadrant it ends, assuming 'one' always starts from [0,0]
        2. use 'one' and 'three' coordinates to get the slope 
        3. Compare two slope. If the second_slope is greater than the first_slope, it is taking left turn.
    '''
    # Destruct each x,y-coordinates
    first_x, first_y = one
    second_x, second_y = two
    third_x, third_y = three
    
    # calculate y and x for slope
    first_slope_y = second_y - first_y
    first_slope_x = second_x - first_x
    second_slope_y = third_y - first_y 
    second_slope_x = third_x - first_x 

    # slope using coordinates 
    first_slope = float(first_slope_y) / first_slope_x
    second_slope = float(second_slope_y) / second_slope_x

    return True if second_slope > first_slope else False


print "\n"
print "======== left_turn() ========"
print "left_turn([0, 0], [2, 2], [2, 3]): ",left_turn([0, 0], [2, 2], [2, 3]) 
print "left_turn([0, 0], [-2, 2], [-3, 2]): ", left_turn([0, 0], [-2, 2], [-3, 2])
print "left_turn([0, 0], [-2, -2], [-2, -3]: ",left_turn([0, 0], [-2, -2], [-2, -3])
print "left_turn([0, 0], [2, -2], [3, -2]): ",left_turn([0, 0], [2, -2], [3, -2])
print "=============================="
print "\n"