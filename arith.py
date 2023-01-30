import mainpackage as mp
print(mp.x)
print(mp.mainpackdemo())
print("-------------")
import mainpackage.sub_pack1 as ms1
print(ms1.sub1)
print(ms1.subpack1demo())
print("-------------")
from mainpackage.sub_pack1 import addsub as sa
print(sa.add(2,3))
print(sa.sub(2,3))
print("-------------")
import mainpackage.sub_pack2 as ms2
print(ms2.sub2)
print(ms2.subpack2demo())
from mainpackage.sub_pack2 import muldiv as md
print(md.mul(5,3))
print(md.div(5,3))