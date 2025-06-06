str ='''AI technology is widely used throughout industry, government, and science. Some high-profile applications include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); interacting via human speech (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., ChatGPT and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go).[2] However, many AI applications are not perceived as AI: A lot of cutting edge AI has filtered into general applications, often without being called AI because once something becomes useful enough and common enough it's not labeled AI anymore.'''

# Make a new string and replace AI with "Artificial Intelligence" and count the no of occurence of AI.

new_str = " " 
ai_count = 0 #Initialize the count to 0 for word "AI"
i = 0        #Initialize the characters in the string

while i<len(str):
    if str[i:i+2] == "AI":     #We take 2 consecutive index and check for string "AI"
        ai_count+=1            #When we found the string AI we increment the counter by 1
        new_str+= "Artifical Intelligence" # We convert the string AI to "Artificial Intelligence" and add it to new string
        i+=2                      #We move by 2 index after this condition is completed
    else:
        new_str+= str[i]        #We add other characters in the string when we find character other than AI
        i+=1                    # We increment the index by 1 and move ahead

print("The updated string is :\n", new_str)
print("\n The No of occurrences of AI is :",ai_count)