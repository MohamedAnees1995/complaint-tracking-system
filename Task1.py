# Write this program with logic

str = "AI technology is widely used throughout industry, government, and science. Some high-profile applications include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); interacting via human speech (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., ChatGPT and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go).[2] However, many AI applications are not perceived as AI: A lot of cutting edge AI has filtered into general applications, often without being called AI because once something becomes useful enough and common enough it's not labeled AI anymore."

# Lets initialize the variables

new_str = " "
ai_count = 0
i = 0

#Loop through the string
while i<len(str):
    if str[i:i+2] == "AI": # Check if "AI" is present in the current index
        ai_count = ai_count + 1
        new_str = new_str + "Artificial Intelligence"
        i= i + 2 # Move the index past the replaced substring because we moved 2 characters
    else:
        new_str = new_str + str[i] #If AI is not present append the current character to the next string
        i = i + 1 # Move to the next character
    
print("The updated string is :\n", new_str)
print("\nThe number of occurrences of AI in this string is :", ai_count)
        
        
        


