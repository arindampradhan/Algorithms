
# The keys of the dictionary above are the nodes of our graph
# An edge can be seen as a 2-tuple with nodes as elements, i.e. ("a","b")


graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }



# This code generates edges in terms of touples
def generate_edges(graph):
	edges = []
	for node in graph:
		for neighbour in graph[node]:
			edges.append((node,neighbour))

	return edges

print (generate_edges(graph))


# The following Python function calculates the isolated nodes
#  see f

def find_isolated_nodes(graph):
	isolated = []
	for node in graph:
		if not graph[node]:
			isolated += node
	print isolated
	return isolated

def recursive_dfs(graph,start,path = []):
	for node in graph[start]:
		if not node in path:
			path=recursive_dfs(graph,node,path)
	return




def iterative_dfs(graph,start,path=[]):
	q=[start]
	while q:
	v=q.pop(0)
	if v not in path:
		path=path+[v]
		q=graph[v]+q
	return path

def iterative_bfs(graph,start,path=[]):
	q=[start]
	while q:
		v = q.pop(0)
		if not v in path:
		q=q+graph[v]
	return path






