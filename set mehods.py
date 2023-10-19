a : set = {'santoor','lux','lifebuoy','cinthol'}
b : set = {'santoor','lux','dettol','medimex'}
print (a.intersection_update(b))
print(a)
print(b)

a : set = {'77','jj','iuiui','788'}
b : set = {'2sd','as1','bsr8','788','jj'}
print(a.isdisjoint(b))

a : set = {"djjs",'kjisjc','khd','jid','jhdioo'}
b : set = {'hs','ds','dsk','ba','bsr','br','jkjksd'}
print(a.isdisjoint(b))


a : set = {"shyam","raj","samrat","vinay","divya"}
b : set ={'66y','uu7','77h','88u','vinay','divya'}
print(a.difference(b))

# symmetric difference
a : set = {'bipc','mpc','cec','mec','cca'}
b : set = {'doc','enginner','char.account''mec','jurnalist','mpc'}
a.symmetric_difference_update(b)
print(a)
print(b)


#issubset
s : set = {"tables","chairs",'lap','books','desk','fans','wooden','tree'}
r : set = {"row &columns",'wooden','semiconductors','tree','wooden','iron'}
print(a.issubset(b))

s : set = {'kaja','putharekulu','milk','double ka mita','a1 sweets'}
r : set = {'faluda','putharekulu','milk','double ka mita','a1 sweets'}
print(s.issubset(s))

#symmeteic_diffeence_update
a : set ={'ap219','ts143','nzb44','nella8','kphb3'}
z : set ={'kukatpally','ts143','kphb3','jntu','miyapur'}
print(a.symmetric_difference_update(z))
print(a)
print(z)


a : set = {'a','b','c'}
b : set = {'b','c','d'}
print(a.issuperset(b))

a : set = {'a','b','c'}
b : set = {'b'}
print(a.issuperset(b))

