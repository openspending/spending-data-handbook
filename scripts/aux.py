import re
import urllib2
from copy import copy

def apply_to_tree(tree,f):
	"""
	Recursively apply a function f to a dictionary representing a tree.

	Dictionary must be in the form:
	{
		children: [...]
		...
	}
	"""
	newtree = f(copy(tree))
	if newtree.has_key("children") and newtree['children']:
		newtree['children'] = [apply_to_tree(x,f) for x in newtree['children']]
	return newtree

def treemapseq(tree,f):
	"""
	Recursively apply a function to every node of a tree.
	Accumulate the returns into a sequence. 
	"""
	result = []
	unvisited = [copy(tree)]
	while unvisited:
		now = unvisited.pop()
		result.append(f(now))
		if now.has_key("children") and now["children"]:
			unvisited += now["children"]
	return result

def get_content(node,root=""):
	"""
	Takes a tree dictionary whose root has a 'url' attribute, returns
	a new tree whose root has an additional 'content' attribute containing
	the string read from the given URL.
	"""
	newnode = copy(node)
	name = newnode['name']
	if re.findall(r'^/.*',name):
		newnode['content'] = urllib2.urlopen(root + name.split("/")[1]).read()
	else:
		newnode['content'] = urllib2.urlopen(name).read()
	return newnode

def parse_content(node):
	"""
	Takes a tree dictionary and reconfigures its root in two ways:
	- extracts a new "title" attribute from its "content"
	- fixes "content" to omit metadata
	"""
	newnode = copy(node)
	try_title = re.search(r'(?<=^# ).*\n', newnode["content"])
	# strip out any title-level lines.
	try_content = re.sub(r'^# .*\n', r'', newnode["content"], flags=re.MULTILINE)
	if try_title:
		newnode['title'] = re.sub(r'"', r'', try_title.group(0)).strip()
	else:
		newnode['title'] = "Untitled"
	if try_content:
		newnode['content'] = try_content.strip()
	else:
		newnode['content'] = "No content"	
	return newnode

def get_next(item,array):
	if not array.count(item):
		return None
	else:
		ind = array.index(item)
		if ind == (len(array) - 1):
			return None
		else:
			return array[array.index(item) + 1]

def add_links(node,order,titledict,site):
	newnode = copy(node)
	if not node.has_key("id"):
		return newnode
	else:
		if get_next(newnode["id"],order) and titledict.has_key(get_next(newnode["id"],order)):
			newnode["content"] += "\n\n**Next**: [" + titledict[get_next(newnode["id"],order)] + "](" + site + "?page_id=" + str(get_next(newnode["id"],order)) + ")"
		if newnode.has_key("parent") and titledict.has_key(newnode["parent"]):
			newnode["content"] += "\n\n**Up**: [" + titledict[newnode["parent"]] + "](" + site + "?page_id=" + str(newnode["parent"]) + ")"
		return newnode

def prune_node(node):
	"""
	Takes a node decorated with "content" and "title" and throws
	that crap out.
	"""
	newnode = copy(node)
	if newnode.has_key("content"):
		newnode.pop("content")
	if newnode.has_key("title"):
		newnode.pop("title")
	return newnode

def test_prune(node):
	"""
	For debugging purposes...
	"""
	newnode = copy(node)
	if newnode.has_key("content"):
		newnode["content"] = "true"
	else:
		newnode["content"] = "FALSE"
	return newnode

def prune_tree(node):
	newnode = copy(node)
	return apply_to_tree(newnode,prune_node)
#	return apply_to_tree(newnode,test_prune)