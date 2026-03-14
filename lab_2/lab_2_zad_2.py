lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']

if 'FGFR4' in lista_gene1 and 'FGERA4' in lista_gene1:
    ind = lista_gene1.index('FGFR4')
    print(ind)
    ind2 = lista_gene1.index('FGERA4')
    print(ind2)
else:
    print('Nie ma takich elementow')
