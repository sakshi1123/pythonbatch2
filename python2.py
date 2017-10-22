def cstodict(cs):
    return dict(item.split("=") for item in cs.split(";"))
    
d= cstodict("abc=de;fg=hi")
print d

