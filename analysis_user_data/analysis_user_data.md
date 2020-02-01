```python
import pandas as pd
import numpy as np

import pymysql

from sqlalchemy import create_engine
```


```python
engine = create_engine('mysql+pymysql://root:open@localhost:3306/dataset-workbench')
```


```python
df = pd.read_sql_query('SELECT * FROM user', engine)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>semester_id</th>
      <th>class_number</th>
      <th>course_id</th>
      <th>course_name</th>
      <th>inst_id_curr</th>
      <th>inst_name_curr</th>
      <th>high_school_name</th>
      <th>school_type</th>
      <th>shift</th>
      <th>...</th>
      <th>year_stoped_work</th>
      <th>other_degree</th>
      <th>inst_name_prev</th>
      <th>name_other_degree</th>
      <th>year_started_prev_degree</th>
      <th>year_stoped_prev_degree</th>
      <th>sex</th>
      <th>year_birth</th>
      <th>civil_status</th>
      <th>have_kids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-1#102#1088</td>
      <td>2016-1</td>
      <td>102</td>
      <td>13</td>
      <td>Física - Bacharelado</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>Escola Estadual Prof Ruth Prestes</td>
      <td>public school</td>
      <td>morning shift</td>
      <td>...</td>
      <td>2016</td>
      <td>no</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>single</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-1#102#1175</td>
      <td>2016-1</td>
      <td>102</td>
      <td>8</td>
      <td>Engenharia de Materiais</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>Fucapi</td>
      <td>private school</td>
      <td>morning shift</td>
      <td>...</td>
      <td>None</td>
      <td>no</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>single</td>
      <td>no</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-1#102#1278</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>Centro Educacional La Salle</td>
      <td>private school</td>
      <td>None</td>
      <td>...</td>
      <td>2016</td>
      <td>no</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>single</td>
      <td>no</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-1#102#1279</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>Colegio Militar da Policia Militar</td>
      <td>public school</td>
      <td>morning shift</td>
      <td>...</td>
      <td>None</td>
      <td>yes</td>
      <td>IFAM</td>
      <td>Analise e Desenvolvimento de Sistema</td>
      <td>2016.0</td>
      <td>2016.0</td>
      <td>male</td>
      <td>1997.0</td>
      <td>single</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-1#102#1280</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
df.shape
```




    (2566, 30)




```python
df.index
```




    RangeIndex(start=0, stop=2566, step=1)




```python
df.columns
```




    Index(['user_id', 'semester_id', 'class_number', 'course_id', 'course_name',
           'inst_id_curr', 'inst_name_curr', 'high_school_name', 'school_type',
           'shift', 'graduation_year', 'has_pc', 'has_internet', 'speed_internet',
           'prev_exp_lang', 'language', 'worked', 'company_name', 'share_pc',
           'year_started_work', 'year_stoped_work', 'other_degree',
           'inst_name_prev', 'name_other_degree', 'year_started_prev_degree',
           'year_stoped_prev_degree', 'sex', 'year_birth', 'civil_status',
           'have_kids'],
          dtype='object')




```python
df.count()
```




    user_id                     2566
    semester_id                 2566
    class_number                2566
    course_id                   2566
    course_name                 2566
    inst_id_curr                2566
    inst_name_curr              2566
    high_school_name            1793
    school_type                 2426
    shift                       2403
    graduation_year             2426
    has_pc                      2426
    has_internet                2031
    speed_internet              1935
    prev_exp_lang               2426
    language                     818
    worked                      2426
    company_name                 467
    share_pc                    2031
    year_started_work            640
    year_stoped_work             636
    other_degree                2426
    inst_name_prev               302
    name_other_degree            302
    year_started_prev_degree     417
    year_stoped_prev_degree      417
    sex                         2136
    year_birth                  2136
    civil_status                2426
    have_kids                   2426
    dtype: int64




```python
df.loc[df['shift'].isnull() == True]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>semester_id</th>
      <th>class_number</th>
      <th>course_id</th>
      <th>course_name</th>
      <th>inst_id_curr</th>
      <th>inst_name_curr</th>
      <th>high_school_name</th>
      <th>school_type</th>
      <th>shift</th>
      <th>...</th>
      <th>year_stoped_work</th>
      <th>other_degree</th>
      <th>inst_name_prev</th>
      <th>name_other_degree</th>
      <th>year_started_prev_degree</th>
      <th>year_stoped_prev_degree</th>
      <th>sex</th>
      <th>year_birth</th>
      <th>civil_status</th>
      <th>have_kids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>2016-1#102#1278</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>Centro Educacional La Salle</td>
      <td>private school</td>
      <td>None</td>
      <td>...</td>
      <td>2016</td>
      <td>no</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>single</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-1#102#1280</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016-1#102#1286</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>Fundação Nokia</td>
      <td>private school</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>no</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>single</td>
      <td>no</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016-1#102#1287</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016-1#102#1289</td>
      <td>2016-1</td>
      <td>102</td>
      <td>7</td>
      <td>Engenharia Mecânica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>Colégio Dom Bosco</td>
      <td>private school</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>no</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>single</td>
      <td>no</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1974</th>
      <td>2018-2#206#3755</td>
      <td>2018-2</td>
      <td>206</td>
      <td>1</td>
      <td>Ciência da Computação</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1987</th>
      <td>2018-2#206#3874</td>
      <td>2018-2</td>
      <td>206</td>
      <td>19</td>
      <td>Engenharia Elétrica</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>2018-2#207#3731</td>
      <td>2018-2</td>
      <td>207</td>
      <td>20</td>
      <td>Física - Licenciatura</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2050</th>
      <td>2018-2#208#3753</td>
      <td>2018-2</td>
      <td>208</td>
      <td>18</td>
      <td>Matemática Aplicada</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2057</th>
      <td>2018-2#208#3873</td>
      <td>2018-2</td>
      <td>208</td>
      <td>1</td>
      <td>Ciência da Computação</td>
      <td>1</td>
      <td>Universidade Federal do Amazonas</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>163 rows × 30 columns</p>
</div>



## Quantidade de valores nulos por característica


```python
null_values = df.isnull().sum().sort_values(ascending=True)
null_values
```




    user_id                        0
    semester_id                    0
    class_number                   0
    course_id                      0
    course_name                    0
    inst_id_curr                   0
    inst_name_curr                 0
    other_degree                 140
    worked                       140
    civil_status                 140
    has_pc                       140
    prev_exp_lang                140
    have_kids                    140
    school_type                  140
    graduation_year              140
    shift                        163
    year_birth                   430
    sex                          430
    has_internet                 535
    share_pc                     535
    speed_internet               631
    high_school_name             773
    language                    1748
    year_started_work           1926
    year_stoped_work            1930
    company_name                2099
    year_started_prev_degree    2149
    year_stoped_prev_degree     2149
    inst_name_prev              2264
    name_other_degree           2264
    dtype: int64




```python
null_labels = null_values.keys()
null_labels
```




    Index(['user_id', 'semester_id', 'class_number', 'course_id', 'course_name',
           'inst_id_curr', 'inst_name_curr', 'other_degree', 'worked',
           'civil_status', 'has_pc', 'prev_exp_lang', 'have_kids', 'school_type',
           'graduation_year', 'shift', 'year_birth', 'sex', 'has_internet',
           'share_pc', 'speed_internet', 'high_school_name', 'language',
           'year_started_work', 'year_stoped_work', 'company_name',
           'year_started_prev_degree', 'year_stoped_prev_degree', 'inst_name_prev',
           'name_other_degree'],
          dtype='object')




```python
%matplotlib inline
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 20))
plt.barh(null_labels, null_values, color='green')
plt.show()

```


![png](output_11_0.png)


## Gráfico de pizza


```python
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = null_values
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots(figsize=(15, 20))

#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#        shadow=True, startangle=90)
ax1.pie(x=sizes, shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.lengend()

plt.show()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-120-1025b11f5857> in <module>
         12 ax1.pie(x=sizes, shadow=True, startangle=90)
         13 #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ---> 14 plt.lengend()
         15 
         16 plt.show()


    AttributeError: module 'matplotlib.pyplot' has no attribute 'lengend'



![png](output_13_1.png)


## Distribuição de alunos por curso


```python
course_counts = df['course_name'].value_counts().values
course_counts
```




    array([240, 230, 219, 218, 215, 206, 194, 188, 168, 165, 138, 118,  78,
            70,  35,  27,  26,  12,  10,   8,   1])




```python
labels = course_counts.keys()
labels
```




    Index(['Engenharia de Materiais', 'Engenharia Mecânica', 'Engenharia Elétrica',
           'Matemática - Licenciatura Noturno', 'Física - Bacharelado',
           'Engenharia Química', 'Estatística', 'Engenharia de Petróleo e Gás',
           'Engenharia de Produção', 'Física - Licenciatura',
           'Ciência da Computação', 'Matemática - Bacharelado',
           'Matemática - Licenciatura Diurno', 'Matemática Aplicada',
           'Sistemas de Informação', 'Geologia', 'Engenharia da Computação',
           'Pós-graduação em Informática', 'Engenharia de Software',
           'Extra - Alunos desperiodizados',
           'Integrado - Técnico de Nível Médio em Informática'],
          dtype='object')




```python
plt.figure(figsize=(10, 10))
plt.barh(labels, course_counts)
plt.show()
```


![png](output_17_0.png)


## Informações sobre internet e PCs


```python
df.columns
```




    Index(['user_id', 'semester_id', 'class_number', 'course_id', 'course_name',
           'inst_id_curr', 'inst_name_curr', 'high_school_name', 'school_type',
           'shift', 'graduation_year', 'has_pc', 'has_internet', 'speed_internet',
           'prev_exp_lang', 'language', 'worked', 'company_name', 'share_pc',
           'year_started_work', 'year_stoped_work', 'other_degree',
           'inst_name_prev', 'name_other_degree', 'year_started_prev_degree',
           'year_stoped_prev_degree', 'sex', 'year_birth', 'civil_status',
           'have_kids'],
          dtype='object')



### Quantidade de usuário com pc, interne e sua velocidade


```python
df1 = df[['has_pc', 'share_pc', 'has_internet', 'speed_internet']]
df1.count()
```




    has_pc            2426
    share_pc          2031
    has_internet      2031
    speed_internet    1935
    dtype: int64




```python
df1[(df1['has_pc'].isnull() == False) &\
    (df1['has_internet'].isnull() == False) &\
    (df1['speed_internet'].isnull() == False)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>has_pc</th>
      <th>has_internet</th>
      <th>speed_internet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>1</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>5</th>
      <td>yes</td>
      <td>yes</td>
      <td>low-speed</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2559</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>2560</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>2562</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>2563</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
    <tr>
      <th>2564</th>
      <td>yes</td>
      <td>yes</td>
      <td>high-speed</td>
    </tr>
  </tbody>
</table>
<p>1935 rows × 3 columns</p>
</div>



## Usuários com PC em casa


```python
values = list(df1['has_pc'].value_counts())
values.append(df1['has_pc'].isnull().sum())
labels = ['yes', 'no', 'não resp.']

print(dict(zip(labels, values)))
```

    {'yes': 2031, 'no': 395, 'não resp.': 140}



```python
fig1, ax1 = plt.subplots(figsize=(10, 10))

ax1.pie(x=values, labels=labels,autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
```


![png](output_25_0.png)


## Usuários que compatilham pc em casa


```python
values = list(df1['share_pc'].value_counts())
values.append(df1['share_pc'].isnull().sum())
labels = ['yes', 'no', 'não resp.']

dict(zip(labels, values))
```




    {'yes': 1253, 'no': 778, 'não resp.': 535}




```python
fig1, ax1 = plt.subplots(figsize=(10, 10))

ax1.pie(x=values, labels=labels,autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
```


![png](output_28_0.png)


## Usuários com internet em casa


```python
values = list(df1['has_internet'].value_counts())
values.append(df1['has_internet'].isnull().sum())
labels = ['yes', 'no', 'não resp.']

dict(zip(labels, values))
```




    {'yes': 1935, 'no': 96, 'não resp.': 535}




```python
fig1, ax1 = plt.subplots(figsize=(10, 10))

ax1.pie(x=values, labels=labels,autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
```


![png](output_31_0.png)


## Velocidade da internet dos usuários


```python
values = list(df1['speed_internet'].value_counts())
values.append(df1['speed_internet'].isnull().sum())
labels = ['high-speed', 'low-speed', 'não resp.']

dict(zip(labels, values))
```




    {'high-speed': 1700, 'low-speed': 235, 'não resp.': 631}




```python
fig1, ax1 = plt.subplots(figsize=(10, 10))

ax1.pie(x=values, labels=labels,autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
```


![png](output_34_0.png)


## Usuários com PC e internet em casa


```python

```
