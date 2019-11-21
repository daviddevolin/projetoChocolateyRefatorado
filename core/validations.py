def pacote_valido(pacote):
    regex = '[a-z]'
    
    valido = regex.match(pacote.id_do_pacote)
    
    return valido