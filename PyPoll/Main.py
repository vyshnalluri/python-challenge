import os
import csv
import operator

row_count = 0
csv_path = 'C:/Users/nallu/OneDrive/Desktop/python-challenge/PyPoll/Resources/election_data.csv'
candidate_list = []
candidate_votes = []
candidates_vote_percent = []
candidate_votes_sorted = []

candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0
winner_candidate = ""

#open and read from csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
   
    # pop header from csv reader
    csv_header = next(csv_reader)
    print(csv_header)

    for eachrow in csv_reader:
        #calculate the changes in profit/losses
        if row_count == 0:
            candidate_list = [eachrow[2]]
        else:
            if eachrow[2] not in candidate_list:
                candidate_list.append(eachrow[2])
           
        row_count += 1




with open(csv_path) as csv_file:
    temp_csv_reader = csv.reader(csv_file, delimiter=',')
       # pop header from csv reader
    temp_csv_header = next(temp_csv_reader)
    #print(temp_csv_header)
    
    for temprow in temp_csv_reader:
            #print("----------------------------------------")
        if temprow[2] == candidate_list[0]:
            candidate1_votes = candidate1_votes + 1
        elif temprow[2] == candidate_list[1]:
            candidate2_votes = candidate2_votes + 1
        elif temprow[2] == candidate_list[2]:
            candidate3_votes = candidate3_votes + 1
        elif temprow[2] == candidate_list[3]:
            candidate4_votes = candidate4_votes + 1
        

print("--------------------------------------")
candidate_votes = [candidate1_votes, candidate2_votes, candidate3_votes, candidate4_votes]
candidates_vote_percent = [round((candidate1_votes/row_count),3)*100,
                            round((candidate2_votes/row_count),3)*100,
                            round((candidate3_votes/row_count),3)*100,
                            round((candidate4_votes/row_count),3)*100
                          ]



print(f"-----------------{candidate_votes}")


candidate_votes_sorted = [candidate_votes[0],candidate_votes[1],candidate_votes[2],candidate_votes[3]] 

candidate_votes_sorted.sort(reverse=True)


if candidate_votes_sorted[0] == candidate_votes[0]:
    winner_candidate = candidate_list[0]
elif candidate_votes_sorted[0] == candidate_votes[1]:
    winner_candidate = candidate_list[1]
elif candidate_votes_sorted[0] == candidate_votes[2]:
    winner_candidate = candidate_list[2]
elif candidate_votes_sorted[0] == candidate_votes[3]:
    winner_candidate = candidate_list[3]    


print(candidate_list)
print(candidate_votes)
print(candidate_votes_sorted)
print(candidates_vote_percent)



           # print(eachrow[2])
#             if each_candidate == eachrow[2]:
#                 candidate_votes = candidate_votes + 1
            
#         candidate_list.extend([each_candidate,candidate_votes])              
# print(candidate_list)    
print("--------------------------------------")
        



print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {row_count}")
print("----------------------------------------")
print(f"{candidate_list[0]}: {round(candidates_vote_percent[0],3)}% ({candidate1_votes})")
print(f"{candidate_list[1]}: {round(candidates_vote_percent[1],3)}% ({candidate2_votes})")
print(f"{candidate_list[2]}: {round(candidates_vote_percent[2],3)}% ({candidate3_votes})")
print(f"{candidate_list[3]}: {round(candidates_vote_percent[3],3)}% ({candidate4_votes})")
print("----------------------------------------")
print(f"Winner: {winner_candidate}")
print("----------------------------------------")