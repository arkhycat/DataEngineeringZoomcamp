#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

url="https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
df_zones = pd.read_csv(url)


# In[5]:


from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')


# In[6]:


df_zones.to_sql(name="zones", con = engine, if_exists="replace")


# In[16]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[18]:


df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)


# In[19]:


first = True

for df_chunk in df_iter:
    if first:
        # Create table schema (no data)
        df_chunk.head(0).to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_chunk))

