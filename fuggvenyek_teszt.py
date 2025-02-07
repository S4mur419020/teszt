import fuggvenyek

def cigar_party_teszt():
    print("1.teszteset")
    cigars=30
    is_weekend:bool=True
    vart:bool=False
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("2.teszteset")
    cigars=40
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
   
    print("3.teszteset")
    cigars=44.5
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("4.teszteset")
    cigars=60
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("5.teszteset")
    cigars=72
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("6.teszteset")
    cigars=-30
    is_weekend:bool=False
    vart:bool=False
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("7.teszteset")
    cigars=40
    is_weekend:bool=False
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("8.teszteset")
    cigars=48
    is_weekend:bool=False
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("9.teszteset")
    cigars=60
    is_weekend:bool=False
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
    print("10.teszteset")
    cigars=72
    is_weekend:bool=False
    vart:bool=False
    kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
def cigar_party_teszt2():
    cigars_lista=[30,40,44.5,60,72,-30,40,48,60,72]
    is_weekend_lista=[True,True,True,True,True,False,False,False,False,False]
    vart_lista_lista=[False,True,True,True,True,False,True,True,True,False]
    for i in range(1,len(cigars_lista),1):
        print(f"{i+1}. Teszteset")
        cigars=cigars_lista[i]
        is_weekend:bool=is_weekend_lista[i]
        vart:bool=vart_lista_lista[i]
        kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
        print(f"cigi: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmeny: {vart==kapott}")
    
cigar_party_teszt()