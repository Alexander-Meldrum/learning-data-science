import numpy as np
import matplotlib.pyplot as plt

questions = {
 "Q1" : "I would never audition to be on a game show.",
 "Q2" : "I am not much of a flirt.",
 "Q3" : "I have to psych myself up before I am brave enough to make a phone call.",
 "Q4" : "I would hate living with room mates.",
 "Q5" : "I mostly listen to people in conversations.",
 "Q6" : "I reveal little about myself.",
 "Q7" : "I spend hours alone with my hobbies.",
 "Q8" : "I prefer to eat alone.",
 "Q9" : "I have trouble finding people I want to be friends with.",
 "Q10" : "I prefer to socialize 1 on 1, than with a group.",
 "Q11" : "I sometimes speak so quietly people sometimes have trouble hearing me.",
 "Q12" : "I do not like to get my picture taken.",
 "Q13" : "I can keep a conversation going with anyone about anything.",
 "Q14" : "I want a huge social circle.",
 "Q15" : "I talk to people when waiting in lines.",
 "Q16" : "I act wild and crazy.",
 "Q17" : "I am a bundle of joy.",
 "Q18" : "I love excitement.",
 "Q19" : "I'd like to be in a parade.",
 "Q20" : "I am a flamboyant person.",
 "Q21" : "I am good at making impromptu speeches.",
 "Q22" : "I naturally emerge as a leader.",
 "Q23" : "I am spontaneous.",
 "Q24" : "I would enjoy being a sports team coach.",
 "Q25" : "I have a strong personality.",
 "Q26" : "I am excited by many different activities.",
 "Q27" : "I spend most of my time in fantasy worlds.",
 "Q28" : "I often feel lucky.",
 "Q29" : "I don't make eye contact when I talk with people.",
 "Q30" : "I have a monotone voice.",
 "Q31" : "I am a touchy feely person.",
 "Q32" : "I would like to try bungee jumping.",
 "Q33" : "I tend to be admired by others.",
 "Q34" : "I make big physical movements whenever I get excited.",
 "Q35" : "I am brave.",
 "Q36" : "I am always in the moment.",
 "Q37" : "I am involved with my community.",
 "Q38" : "I am good an entertaining children.",
 "Q39" : "I like formal occasions.",
 "Q40" : "I would have to be lost for a very long time before asking help.",
 "Q41" : "I do not care about sports.",
 "Q42" : "I prefer individual sports to team sports.",
 "Q43" : "My parents know nothing about my love life.",
 "Q44" : "I mostly listen to people in conversations.",
 "Q45" : "I never leave the door to my room open.",
 "Q46" : "I make a lot of hand motions when I talk.",
 "Q47" : "I take lots of pictures of my activities.",
 "Q48" : "When I was a child, I put on fake concerts and plays with my friends.",
 "Q49" : "I really like dancing.",
 "Q50" : "I would have difficulty describing myself to someone.",
 "Q51" : "My life would not make a good story.",
 "Q52" : "I am hesitant to give suggestions.",
 "Q53" : "I tire out quickly.",
 "Q54" : "I never tell people the important things about myself.",
 "Q55" : "I avoid going to unknown places.",
 "Q56" : "Going to the doctor is always awkward for me.",
 "Q57" : "I have not kept up with my old friends over the years.",
 "Q58" : "I have not been joyful for quite some time.",
 "Q59" : "I hate to ask for help.",
 "Q60" : "If I were to die, I would not want there to be a memorial for me.",
 "Q61" : "I hate shopping.",
 "Q62" : "I love to do impressions.",
 "Q63" : "I would be pleased if asked to speak at a funeral.",
 "Q64" : "I would never go to a dance club.",
 "Q65" : "I find it very hard to tell people I find them attractive.",
 "Q66" : "I hate people.",
 "Q67" : "I was an outcast in school.",
 "Q68" : "I would enjoy being a librarian.",
 "Q69" : "I am usually not single.",
 "Q70" : "I am able to stand up for myself.",
 "Q71" : "I would go surfing regularly if I lived on a beach.",
 "Q72" : "I have wanted to be a stand-up comedian.",
 "Q73" : "I am a high status person.",
 "Q74" : "I work out regularly.",
 "Q75" : "I laugh a lot.",
 "Q76" : "I like pranks.",
 "Q77" : "I am happy with my life.",
 "Q78" : "I am never at a loss for words.",
 "Q79" : "I feel healthy and vibrant most of the time.",
 "Q80" : "I love large parties.",
 "Q81" : "I am quiet around strangers.",
 "Q82" : "I don't talk a lot.",
 "Q83" : "I keep in the background.",
 "Q84" : "I don't like to draw attention to myself.",
 "Q85" : "I have little to say.",
 "Q86" : "I often feel blue.",
 "Q87" : "I am not really interested in others.",
 "Q88" : "I make people feel at ease.",
 "Q89" : "I don't mind being the center of attention.",
 "Q90" : "I start conversations.",
 "Q91" : "I talk to a lot of different people at parties."
}
questions = np.array(list(questions.values()))

data = np.genfromtxt('dataset.csv',dtype=int,delimiter='\t')
data = data[1:,:]


print(data)
print(data.shape)
print(data.dtype)

# Get the distribution of introverts, extroverts and not identify
ie_colum = data[:,-1]
#print(ie_colum)

answer, count = np.unique(ie_colum, return_counts=True)
total = count.sum()

print(answer, count)
print("No Answer:", round(count[0]/total*100,2))
print("Introverts:", round(count[1]/total*100,2))
print("Extroverts:", round(count[2]/total*100,2))
print("Not Identify", round(count[3]/total*100,2))

# Calculate mean
time_elapsed = data[:,2:3*91+1:3]
# Clean data above 2min
time_elapsed[time_elapsed>120000] = 120000
mean_elapsed = time_elapsed.mean(axis=0)

# print(time_elapsed)
# print(mean_elapsed)
# print(mean_elapsed.shape)

# questions_sorted = questions[mean_elapsed.argsort()]
# print(questions_sorted[:5])
# print(questions_sorted[:-6:-1])



len_vectorize = np.vectorize(len)
length_of_questions = len_vectorize(questions)
plt.scatter(length_of_questions, mean_elapsed)

# Fit a linear line to data, a*x + b
a,b = np.polyfit(length_of_questions,mean_elapsed,1)
plt.plot(length_of_questions,a*length_of_questions + b, color='r')

plt.xlabel("Length of questions")
plt.ylabel("mean_elapsed")
plt.show()



# Sort Intro and Extroverts, Slice using bool expression
introverts = data[data[:,281] == 1]
extroverts = data[data[:,281] == 2]
print("Average age of introverts in test", introverts[:,280].mean())
print("Average age of extroverts in test", extroverts[:,280].mean())
introverts_ratings = introverts[:,0:91*3:3]
extroverts_ratings = extroverts[:,0:91*3:3]
introverts_avg_ratings = introverts_ratings.mean(axis=0)
extroverts_avg_ratings = extroverts_ratings.mean(axis=0)
print("Introverts highest rating:", questions[introverts_avg_ratings.argmax()])
print("Extroverts highest rating:", questions[extroverts_avg_ratings.argmax()])
print("Introverts lowest rating:", questions[introverts_avg_ratings.argmin()])
print("Extroverts lowest rating:", questions[extroverts_avg_ratings.argmin()])