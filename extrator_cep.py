endereco = ("Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120")


import re # Regular Expression -- RegEx

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)