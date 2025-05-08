def analyze_expenses(*args,**kwargs):
    
    total_args = sum(args)
    total_kwargs = sum(kwargs.values())
    total = total_args + total_kwargs
    print("total exp",total)
    print("unamed expences:",len(args))
    print("named expences:",len(kwargs))
    
    
analyze_expenses(20, 45, 35, taxi=15, resto=40, cinema=25)

