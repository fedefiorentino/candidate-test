import re

p = re.compile(r'  initial begin\n((    \S*\[\S*\] = \S*;\n)*)  end\n')

with open('testcase.v','rt') as original:
	texto = original.read()

with open('memdump1.mem', 'wt') as dump:
	dumper = re.split(r'\n', texto)
	for i in dumper:
		aux = re.search(r'(?<=\] = 8\'h)\w+', i)
		if aux:
			dump.write(aux.group(0)+'\n')

with open('modified.v', 'wt') as final:
	modified = p.sub('  $readmemh("memdump1.mem", mem);\n', texto)
	final.write(modified)

