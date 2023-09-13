#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import pandas as pd
#import json

#path="C:\\Users\\raman\\Downloads\\csgo\\csgo\\CCT-Online-Finals-1\\2579048_events.jsonl"

#df=pd.read_json(path,lines=True)

#df.shape


#df.info()
#(df.head())
#df.columns

#events=pd.DataFrame()
#for index,row in df.iterrows():
#    events=pd.concat([events,pd.json_normalize(row['events'])])
#    events.reset_index(drop=True,inplace=True)
    
#events
    


# In[1]:


import json
import pandas as pd
json_dicts1=[]
data1="C:\\Users\\raman\\Downloads\\csgo\\csgo\\CCT-Online-Finals-1\\2579048_events.jsonl"
with open(data1) as f:
    lines=f.read().splitlines()
    
    for line in lines:
        json_dicts1.append(json.loads(line))
    
    
df1=pd.DataFrame(json_dicts1)    
df1
#df1.columns
#df1.shape


# In[2]:


events = pd.DataFrame()
for index, row in df1.iterrows():
    events = pd.concat([events,pd.json_normalize(row['events'])])
events.reset_index(drop=True,inplace=True) 
#events

x=events.loc[events['type']=='game-ended-round']


#x.to_excel('game-ended-round.xlsx',index=False)
x

#y=x.loc[x['target']=='']


# In[3]:


target_state_teams = pd.DataFrame()
for index, row in x.iterrows():
    target_state_teams = pd.concat([target_state_teams,pd.json_normalize(row['target.state.teams'])])
target_state_teams.reset_index(drop=True,inplace=True) 
y=target_state_teams
#y.to_excel('target_state_teams.xlsx',index=False)
y


# In[4]:


target_state_teams_players=pd.DataFrame()
for index,row in y.iterrows():
    target_state_teams_players=pd.concat([target_state_teams_players,pd.json_normalize(row['players'])])
target_state_teams_players.reset_index(drop=True,inplace=True)
z=target_state_teams_players
#z.to_excel('target_state_teams_players.xlsx',index=False)
z


# In[5]:


x.shape


# In[6]:


y.shape


# In[7]:


z.shape


# In[186]:


r3salt = z.loc[(z['name']=='r3salt')]
r3salt.reset_index(drop=True,inplace=True)
r3salt['round_id']=range(1,len(r3salt)+1)
cols=r3salt.columns.to_list()
cols=['round_id']+cols[:-1]
r3salt=r3salt[cols]
#r3salt
#r3salt_and_kills.to_excel("r3salt.xlsx",index=False)


# In[116]:


zorte=z.loc[(z['name']=='zorte')]
zorte.reset_index(drop=True,inplace=True)
zorte['round_id']=range(1,len(zorte)+1)
cols=zorte.columns.to_list()
cols=['round_id']+cols[:-1]
zorte=zorte[cols]
#zorte
#cols
#zorte_and_kills.to_excel("zorte.xlsx",index=False)


# In[203]:


shalfey=z.loc[(z['name']=='shalfey')]
shalfey.reset_index(drop=True,inplace=True)
shalfey['round_id']=range(1,len(shalfey)+1)
cols=shalfey.columns.to_list()
cols=['round_id']+cols[:-1]
shalfey=shalfey[cols]
#shalfey
#shalfey_and_kills.to_excel("shalfey.xlsx",index=False)


# In[205]:


Jerry=z.loc[(z['name']=='Jerry')]
Jerry.reset_index(drop=True,inplace=True)
Jerry['round_id']=range(1,len(Jerry)+1)
cols=Jerry.columns.to_list()
cols=['round_id']+cols[:-1]
Jerry=Jerry[cols]
#Jerry
#jerry_and_kills.to_excel("jerry.xlsx",index=False)


# In[206]:


Krad=z.loc[(z['name']=='Krad')]
Krad.reset_index(drop=True,inplace=True)
Krad['round_id']=range(1,len(Krad)+1)
cols=Krad.columns.to_list()
cols=['round_id']+cols[:-1]
Krad=Krad[cols]
#Krad
#krad_and_kills.to_excel("krad.xlsx",index=False)


# In[207]:


Kylar=z.loc[(z['name']=='Kylar')]
Kylar.reset_index(drop=True,inplace=True)
Kylar['round_id']=range(1,len(Kylar)+1)
cols=Kylar.columns.to_list()
cols=['round_id']+cols[:-1]
Kylar=Kylar[cols]
#Kylar

#kylar_and_kills.to_excel("kylar.xlsx",index=False)



# In[208]:


Goofy=z.loc[(z['name']=='Goofy')]
Goofy.reset_index(drop=True,inplace=True)
Goofy['round_id']=range(1,len(Goofy)+1)
cols=Goofy.columns.to_list()
cols=['round_id']+cols[:-1]
Goofy=Goofy[cols]
#Goofy
#goofy_and_kills.to_excel("goofy.xlsx",index=False)


# In[209]:


hades=z.loc[(z['name']=='hades')]
hades.reset_index(drop=True,inplace=True)
hades['round_id']=range(1,len(hades)+1)
cols=hades.columns.to_list()
cols=['round_id']+cols[:-1]
hades=hades[cols]
#hades
#hades_and_kills.to_excel("hades.xlsx",index=False)


# In[210]:


KEi=z.loc[(z['name']=='KEi')]
KEi.reset_index(drop=True,inplace=True)
KEi['round_id']=range(1,len(KEi)+1)
cols=KEi.columns.to_list()
cols=['round_id']+cols[:-1]
KEi=KEi[cols]
#KEi
#kei_and_kills.to_excel("kei.xlsx",index=False)


# In[211]:


mynio=z.loc[(z['name']=='mynio')]
mynio.reset_index(drop=True,inplace=True)
mynio['round_id']=range(1,len(mynio)+1)
cols=mynio.columns.to_list()
cols=['round_id']+cols[:-1]
mynio=mynio[cols]
#mynio
#mynio_and_kills.to_excel("mynio.xlsx",index=False)


# In[41]:


y
#y.info()
#y.describe()
y.isnull().sum()
y.groupby('name')['kills'].sum()
#y.groupby('side')['damageDealt'].sum()


# In[40]:


y[y['name']=='forZe'].groupby('side')['kills'].sum()


# In[42]:


y[y['name']=='9INE'].groupby('side')['kills'].sum()


# In[148]:


y['K/D']=y['kills']/y['deaths']

team_KD=y[y['name']=='forZe'].groupby('name')['K/D'].mean()
#team_KD.plot(kind='bar')
#plt.xlabel("won")
#plt.ylabel("kills")
#plt.xticks(rotation=45)
#plt.show()
#y['K/D']
team_KD


# In[321]:


datum=[pd.DataFrame(r3salt),
       pd.DataFrame(zorte),
       pd.DataFrame(shalfey),
       pd.DataFrame(Jerry),
       pd.DataFrame(Krad),
       pd.DataFrame(Kylar),
       pd.DataFrame(Goofy),
       pd.DataFrame(hades),
       pd.DataFrame(KEi),
       pd.DataFrame(mynio)]

# def round_details(df,p1,p2):
#     req_columns=['round_id','name','kills','deaths','damageDealt','damageTaken','headshots']
#     data_dict={p1:[],p2:[]}
   

#     for index,row in df.iterrows():
#         player_name=row['name']

#         if player_name == p1:
#             round_data = {col: row[col] for col in req_columns}
#             data_dict[p1].append(round_data)
        
#         elif player_name == p2:
#             round_data = {col: row[col] for col in req_columns}
#             data_dict[p2].append(round_data)
        
#         # if round_id != current_round:
#         #     # if current_player:
#         #     #     data_list.append({f'round_id': current_round,**round_data_1[current_player]})
#         #     #     data_list.append({f'round_id': current_round,**round_data_2[current_player]})
#         #     current_round=round_id
#         #     print("called")

#         #player_name=row['name']
#         #if player_name==p1:
#          #       current_player=player_name
#          #       round_data_1[current_player].update({col:row[col] for col in req_columns})
        
#         #if player_name==p2:
#          #    current_player=player_name
#           #   round_data_2[current_player].update({col:row[col] for col in req_columns})
                    
#    # if current_player:
#     #    data_list.append({f'round_id': round_id,**round_data_1[current_player]})
#      #   data_list.append({f'round_id': round_id,**round_data_2[current_player]})
#     return data_dict
    

# p1='r3salt'
# p2='Kaylar'

# round_data_list=[]


# for df_name,df in zip(['r3salt','zorte','shalfey','Jerry','Krad','Kylar','Goofy','hades','KEi','mynio'],datum):
#     round_details_gen=round_details(df,p1,p2)

#     if any(round_details_gen[p1]) or any(round_details_gen[p2]):
#        if round_details_gen[p1]:
#            data_dict={"pid":p1,"data":round_details_gen[p1]}
#            round_data_list.append(data_dict)

#        if round_details_gen[p2]:
#            data_dict={"pid":p2,"data":round_details_gen[p2]}
#            round_data_list.append(data_dict)
        

#print("Raw round_data_dict:")
#print(round_data_dict)

# Filter out entries with empty lists for both p1 and p2 from the beginning and end
#filtered_round_data_dict = {key: value for key, value in round_data_dict.items() if any(value[p1]) or any(value[p2])}

#print("\nFiltered round_data_dict:")
#print(filtered_round_data_dict)



#filtered_round_data_dict=[{key:value for key,value in round_data_dict.items() if any (value)}]
    #for round_data in round_details_gen:
#print(filtered_round_data_dict)
#filtered_round_data_dict = {key: value for key, value in round_data_dict.items() if any(value[p1]) or any(value[p2])}
#print(round_data_list)


# In[ ]:


#[{"pid":"Jerry","data":[]},{"pid":"mynio","data":[]}]


# In[319]:


# def player_names(data):
#     name=set()

#     for df in data:
#         if 'name' in df.columns:
#             name.update(df['name'].unique())
#     return list(name)

# players=player_names(datum)
# print(players)


# In[ ]:





# In[ ]:




