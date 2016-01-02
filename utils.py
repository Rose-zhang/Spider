__author__ = 'Jason-Zhang'


# Acknowledge
# http://ar.newsmth.net/thread-b99daa8fc0a336.html
def parse_js(expr):
	import ast
	m = ast.parse(expr)
	a = m.body[0]

	def parse(node):
		if isinstance(node, ast.Expr):
			return parse(node.value)
		elif isinstance(node, ast.Num):
			return node.n
		elif isinstance(node, ast.Str):
			return node.s
		elif isinstance(node, ast.Name):
			return node.id
		elif isinstance(node, ast.Dict):
			return dict(zip(map(parse, node.keys), map(parse, node.values)))
		elif isinstance(node, ast.List):
			return map(parse, node.elts)
		else:
			raise NotImplementedError(node.__class__)

	return parse(a)
