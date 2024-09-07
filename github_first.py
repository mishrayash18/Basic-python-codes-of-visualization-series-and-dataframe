'''import pandas as pd
s1= pd.Series([4,5,6,7,8])
print("the series is:")
print(s1)

import pandas as pd
s2=pd.Series([1,2,3,4], index=('a','b','c','d'))
print(s2)

import pandas as pd
section=['A','B','C','D']
contri=[4000,2000,2500,3000]
s3=pd.Series(data=contri, index=section)
print(s3)
print(s3.head(2))
print(s3.hasnans)

import pandas as pd
dict1={'section':['A','B','C','D'], 'contri':[4000,2000,2500,3000]}
s1=pd.DataFrame(dict1,index=[1,2,3,4])
print(s1)

import pandas as pd
sales={'yr1':{'qtr1':34500,'qtr2':24300,'qtr3':45000}, 'yr2':{'qtr1':23000,'qtr2':55000,'qtr3':65000}}
dict1=pd.DataFrame(sales)
print(dict1)

import pandas as pd
import matplotlib.pyplot as plt
week=[1,2,3,4]
marks=[25,45,64,12]
plt.plot(week,marks)
plt.xlabel('week')
plt.ylabel('marks')
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt
week=[1,2,3,4]
marks=[25,66,78,90]
plt.bar(week,marks, width=[0.7,0.5,0.6,0.4], color=['gold','cyan','green','red'])
plt.xlabel('week')
plt.ylabel('marks')
plt.show()
        
