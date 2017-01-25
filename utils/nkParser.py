import re

# regex = re.compile(r'(\w+)( {\n[^}]+name )([a-zA-Z0-9_:/.]+)([^}]+)')
# regex = re.compile(r'({)(.+)(})')

filename = 'B:/nktst.nk'

def parse_nkScript(filename):
	"""
	Parse .nk files, collects a list of nodes (in .nk string format) and their names.
	"""
	# Get .nk contents
    with open(filename,'r') as f:
        data = f.read()
        f.close()
    # print data

    regex = re.compile(r'(\w+)( {\n)(.+?)(\n}\n)', re.DOTALL)
    node_list = re.findall(regex,data)

    print "".join(node_list[-1]) # Example

	for node in node_list:
	    node_string = "".join(node)
	    #print node_string
	    print re.search(r'name ([a-zA-Z0-9_:/.]+)', node_string).group(1)

    return node_list



node_list = parse_nkScript(nuke.root().name())
