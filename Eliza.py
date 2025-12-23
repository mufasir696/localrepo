letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def is_variable(pattern):
    return(type(pattern) is str 
           and pattern[0]=='?' 
           and len(pattern)>1 
           and pattern[1]!='*'
           and pattern[1] in letters 
           and pattern!=''
)
def match_var(var,value,binding):
    bindings=binding.get(var)
    if not bindings:
        binding.update({var:value})
        return binding
    if value==binding[var]:
        return binding
    return False
bindy={}
print(match_var("?a",10,bindy))
print(match_var("?b",20,bindy))
print(match_var("?b",40,bindy))
def contain_token(pattern):
    return type(pattern)is list and len(pattern)>0
print(contain_token([1,2,3]))
def match_pattern(pattern,input,binding=None):
    if binding is False:
        return False
    if binding is None:
        binding={}
    if pattern==input:
        return binding
    if is_variable(pattern):
        var=pattern[1:]
        return match_var(var,[input],binding)
    elif contain_token(pattern)and contain_token(input):
        return match_pattern(pattern[1:],input[1:],match_pattern(pattern[0],input[0],binding))
    else:
        return False
pattern = ['a', '?d', '?e']
input   = ['a', 'b', 'c']
print(match_pattern(pattern, input))
