本周做了127（单词接龙）、208（实现trie树）、547（朋友圈）、37接数独。征对性的练习了一下双向BFS、trie树、并查集等几个知识点，另外总结了一下双向BFS的模板，把Trie树和并查集的模板也放进来了，便于查看。

# Trie 树代码模板(Python)
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word  # 这里可以赋任意值
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True

****

#并查集代码模板(Python)  


def init(p): 

	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 

	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 

	root = i
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root

#bidirectional BFS 模板代码模板(Python)  

def BID_BFS(graph, start, end):

	front={start}
	back={end}
	while front:
		next_front=set()
		for node in front:
			porcess(node)
			new_nodes=generate_new_node(node)
			for new_node in new_nodes:
				if new_node in back:'
					return
				next_front.add(new_node)
		front=next_front
		if len(front)>len(back):
			front,back=back,front
	return