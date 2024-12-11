import streamlit as st
from recipe_generator import generate_post

# Options for length and language
language_options = ["English", "Hinglish", "Hindi", "Gujlish", "Gujarati"]

# Main app layout
def main():
    # Styled header with website name and emoji
    st.markdown("<h1 style='text-align: center; color: #FF5733;'>Khaana Junction 🍽️</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px; color: #555;'>Effortlessly get delicious food recipes in just a few clicks!</p>",
                unsafe_allow_html=True)
    st.markdown("<hr style='border:2px solid #bbb; margin:10px 0;'>",
                unsafe_allow_html=True)

    # Create a container for input fields
    with st.container():
        # Create two columns for the food name and language dropdown
        col1, col2 = st.columns([2, 1])

        with col1:
            # Textbox for Food Name
            st.markdown("<p style='font-size:18px; color:#9b59b6; margin-bottom:2px;'>🍴 <b>Food Name:</b></p>",
                        unsafe_allow_html=True)
            food_name = st.text_input("", placeholder="Enter the name of the dish", label_visibility="collapsed")

        with col2:
            # Dropdown for Language
            st.markdown("<p style='font-size:18px; color:#9b59b6; margin-bottom:2px;'>🌐 <b>Language:</b></p>",
                        unsafe_allow_html=True)
            selected_language = st.selectbox("", options=language_options, label_visibility="collapsed")

        # Generate Button below inputs
        st.markdown("<div style='text-align: center; margin-top:10px;'>", unsafe_allow_html=True)
        if st.button("✨ Generate Recipe ✨"):
            if food_name.strip():
                # Generate and display the post
                post = generate_post(food_name, selected_language)
                st.markdown("<hr style='border:1px solid #ccc; margin:20px 0;'>",
                            unsafe_allow_html=True)

                # Output section with styled container
                st.markdown(f"""
                    <div style='
                        padding:15px; 
                        border-radius:10px; 
                        background-color:var(--bg-secondary, rgba(255, 240, 220, 0.8)); 
                        color:var(--text-primary, #333);
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);'>
                        <p style='font-size:16px; line-height:1.6;'>{post}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Please enter a food name before generating the recipe.")

    # Footer with a quote
    st.markdown("<hr style='border:2px solid #bbb; margin:20px 0;'>",
                unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; font-size:16px; color: #888;'>
            "Cooking is an art, and every recipe is a story waiting to be told." 🍳
        </p>
    """, unsafe_allow_html=True)

    # Background styling for light and dark mode (without image)
    st.markdown("""
        <style>
            :root {
                --bg-primary: #ffffff;
                --bg-secondary: rgba(255, 240, 220, 0.8);
                --text-primary: #000000;
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    --bg-primary: #121212;
                    --bg-secondary: rgba(30, 30, 30, 0.9);
                    --text-primary: #e0e0e0;
                }
            }

            body {
                background-color: var(--bg-primary);
                color: var(--text-primary);
            }

            div[role="main"] {
                background: var(--bg-secondary);
                border-radius: 10px;
                padding: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }

            h1, p {
                color: var(--text-primary);
            }
        </style>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
