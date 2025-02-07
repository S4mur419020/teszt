def cigar_party(cigars, is_weekend):
    if is_weekend:
       if cigars>=40:
         eredmeny=True
       else:
         eredmeny=False
    else:
       if cigars>=40 and cigars<=60:
         eredmeny=True
       else:
         eredmeny=False
    return eredmeny
