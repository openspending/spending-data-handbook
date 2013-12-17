import pywordpress
import yaml
from copy import copy
from aux import *

class Bot():
	def __init__(self,configfile,wp_config="wordpress.ini"):
		# Create a new WP instance using the config file.
		self.wp_config = wp_config
		self.wp = pywordpress.Wordpress.init_from_config(self.wp_config)
		# Load up the post configuration YAML file and get the data.
		# Initialize the list of page IDs.
		self.config = yaml.safe_load(open(configfile))
		self.wp_site = self.config['wp-site']
		self.data = self.config['source-tree']
		self.ids = []
		self.titles = {}
		self.sequence = []
		if self.config.has_key("id-sequence"):
			self.sequence = self.config["id-sequence"]

	# Note that I implement all operations on the data tree
	# as operations on immutable objects rather than mutating the
	# tree in place. (This is because I'm used to Clojure and am
	# uncomfortable with mutable data types.)
	def load_data(self):
		"""
		Replace the bot's data tree with a new tree that has a
		"content" attribute for each node, grabbed from the web
		addresses in each node's "name" attribute (merged with
		the config file's "root-name" if appropriate).
		"""
		self.data = apply_to_tree(self.data, lambda x: get_content(x, self.config['root-name']))

	def parse_data(self):
		"""
		Replace the bot's data tree, already decorated with "content"
		attributes, with a new tree whose "content" attributes have been
		stripped of title information and whose "title" attribute has
		been grabbed from the "content" attribute.

		Also build a dictionary of IDs => titles.

		Finally, decorate the bot's data tree with links to "up"
		and "next" pages, as determined by the (optional) ordering
		of IDs in the config file.
		"""
		self.data = apply_to_tree(self.data, parse_content)
		def title_id(node):
			if node.has_key("id"):
				return {node["id"]: node["title"]}
			else:
				return {}
		def merge_dicts(dicts):
			value = {}
			for d in dicts:
				value = dict(value.items() + d.items())
			return value
		self.titles = merge_dicts(treemapseq(self.data, title_id))
		if self.sequence:
			self.data = apply_to_tree(self.data, lambda d: add_links(d, self.sequence, self.titles, self.wp_site))

	def build_pages(self,node):
		"""
		Takes a tree and either creates a new WordPress page or,
		if it already has an "id" attribute, updates the page.
		Propagates the ID of the page to each child of the root.
		Then builds WP pages for *those* subtrees.
		"""
		print "Posting " + node["slug"]
		if node.has_key("parent"):
			if node.has_key("id"):
				self.wp.edit_page(page_id = node["id"],
							title = node['title'],
							wp_slug = node['slug'],
							description = node['content'],
							wp_page_parent_id = node['parent'])
			else:
				node['id'] = self.wp.new_page(title = node['title'],
								wp_slug = node['slug'],
								description = node['content'],
								wp_page_parent_id = node['parent'])
		else:
			if node.has_key("id"):
				self.wp.edit_page(page_id = node["id"],
								title = node['title'],
								wp_slug = node['slug'],
								description = node['content'])
			else:
				node['id'] = self.wp.new_page(title = node['title'],
								wp_slug = node['slug'],
								description = node['content'])
		if node['children']:
			for x in node['children']:
				x['parent'] = node['id']
				self.build_pages(x)
		self.ids.append(node['id'])

	def dump_tree(self):
		"""
		Replaces post.yaml with the updated data tree created in
		the course of posting the pages, pruning its nodes of their
		"title" and "content" attributes first.
		"""
		print "Dumping data tree to post.yaml"
		the_dump = copy(self.config)
		the_dump["source-tree"] = prune_tree(self.data)
		f = open("post.yaml", "w")
		f.write(yaml.dump(the_dump))
		f.close()

	def write_ids(self):
		f = open("kill.yaml", "w")
		f.write(yaml.dump(self.ids))
		f.close()

if __name__ == "__main__":
	b = Bot("post.yaml")
	b.load_data()
	b.parse_data()
	b.build_pages(b.data)
	b.write_ids()
	b.dump_tree()