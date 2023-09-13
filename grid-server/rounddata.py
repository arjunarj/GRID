import pandas as pd
from GRID_ker import r3salt,zorte,shalfey,Jerry,Krad,Kylar,Goofy,hades,KEi,mynio
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

def round_details(df,p1,p2):
    req_columns=['round_id','name','kills','deaths','damageDealt','damageTaken','headshots']
    data_dict={p1:[],p2:[]}
   

    for index,row in df.iterrows():
        player_name=row['name']

        if player_name == p1:
            round_data = {col: row[col] for col in req_columns}
            data_dict[p1].append(round_data)
        
        elif player_name == p2:
            round_data = {col: row[col] for col in req_columns}
            data_dict[p2].append(round_data)
        
        # if round_id != current_round:
        #     # if current_player:
        #     #     data_list.append({f'round_id': current_round,**round_data_1[current_player]})
        #     #     data_list.append({f'round_id': current_round,**round_data_2[current_player]})
        #     current_round=round_id
        #     print("called")

        #player_name=row['name']
        #if player_name==p1:
         #       current_player=player_name
         #       round_data_1[current_player].update({col:row[col] for col in req_columns})
        
        #if player_name==p2:
         #    current_player=player_name
          #   round_data_2[current_player].update({col:row[col] for col in req_columns})
                    
   # if current_player:
    #    data_list.append({f'round_id': round_id,**round_data_1[current_player]})
     #   data_list.append({f'round_id': round_id,**round_data_2[current_player]})
    return data_dict
    

p1='r3salt'
p2='Kaylar'

round_data_list=[]


for df_name,df in zip(['r3salt','zorte','shalfey','Jerry','Krad','Kylar','Goofy','hades','KEi','mynio'],datum):
    round_details_gen=round_details(df,p1,p2)

    if any(round_details_gen[p1]) or any(round_details_gen[p2]):
       if round_details_gen[p1]:
           data_dict={"pid":p1,"data":round_details_gen[p1]}
           round_data_list.append(data_dict)

       if round_details_gen[p2]:
           data_dict={"pid":p2,"data":round_details_gen[p2]}
           round_data_list.append(data_dict)
        

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
print(round_data_list)
