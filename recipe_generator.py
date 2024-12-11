from llm_help import llm

def generate_post(name,language):
    prompt = get_prompt(name,language)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(name,language):

    prompt =f'''Generate a detailed and accurate food recipe using the information provided below. Adhere to these instructions with precision:

    1) **Name:** {name}
    2) **Language:** {language}
       - If the language is **Hinglish**, the recipe must use a mix of Hindi and English words, written entirely in the English script only. It should feel natural and conversational, similar to this example:
         **Name:** Chai  
         **Recipe:**  
         - **Mandatory Ingredients:**  
           1 cup of doodh 🥛 (milk), 1 teaspoon of chai patti (tea leaves) ☕️, 1/2 cup of paani (water) 💧, 2 teaspoons of cheeni (sugar) 🍬.  
         - **Instructions:**  
           1. Ek chhoti kadhai (small pan) le aur usme paani aur chai patti daal do.  
           2. Paani ko ubalne do (boil the water) for 2 minutes.  
           3. Usme doodh aur cheeni mila ke 5 minute tak paka lo (cook for 5 minutes).  
           4. Chai ko chhanni se chhankar (strain using a strainer) ek cup mein daalo.  
           5. Garma-garam chai ka maza lo (Enjoy your hot cup of tea)! ☕️✨  
       - If the language is **Gujglish**, the recipe must use a mix of Gujarati and English words, written entirely in the English script. Avoid unnecessary complexity and ensure clarity.
       - If the language is **Gujarati**, the recipe must be written in proper and natural Gujarati, free of spelling or grammatical errors. Use standard Gujarati vocabulary that fits a recipe context.
       - If the language is **Hindi**, the recipe must be written in proper and natural Hindi, free of spelling or grammatical errors. Use standard Hindi vocabulary that fits a recipe context.
    3) **Emojis:** Enhance the appeal of the recipe by adding contextually relevant emojis, such as 🍴 for serving, 🥣 for mixing, 🌶️ for spicy, etc.
    4) **Output Structure:** 
       - **Mandatory Ingredients:** Clearly list all mandatory ingredients required for the recipe. Keep it concise and precise.
       - **Optional Ingredients:** List optional ingredients separately, highlighting their optional nature.
       - **Recipe Instructions:** Provide clear, step-by-step instructions to prepare the dish. Use short and direct sentences for better comprehension.
       - **Additional Tips:** Include helpful tips for preparation, serving, or customization of the dish.
        - At the end of the recipe, include a small funny and loving note that creates a good impression on the reader it should be different every time, such as:  
         "Pyaar aur mehnat se banayi hui recipe ka maza alag hi hota hai. Try it and thank us later! 😉❤️"  
    
    **Critical Notes:**
    - Ensure the recipe output is realistic and reflects common cooking practices.
    - Avoid generating nonsensical or irrelevant content, especially in Gujlish and Gujarati.
    - Maintain cultural authenticity and appropriateness for all languages.
    - The recipe should be practical, engaging, and free of any factual errors.
    - The ingredients should be written on Separate lines so it is easily readable. 
    - And add the area (state or country) name from were the recipe belongs to at the beginning after the name of recipe,such as:  
        Chai 
        
        Did you know that Dal Dhokli is a popular dish from Gujarat, India?
        for all recipe asked, you can style as per requirement, and change the language ass per selection for this line .
    Ensure the final output is well-structured, contextually accurate, and engaging for users.
    '''

    return prompt


if __name__ == "__main__":
    print(generate_post("Poutine", "Hinglish"))
