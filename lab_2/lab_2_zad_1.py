set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
                'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
                'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])

a = set_gene1
b = set_gene2
c = set_gene3

print (a & b & c)
print(a & b)
print(a & c)
print(b & c)
print(a - (b | c))
print(b - (a | c))
print(c - (a | b))
