import streamlit as st

# Language dictionaries
isoko = {
    'hello': 'miguo',
    'food': 'emi',
    'water': 'ami',
    'thank you': 'me do',
    'school': 'sukulu',
    'book': 'buku',
    'love': 'orho',
    'friend': 'omoni',
    'family': 'egweya',
    'money': 'owu',
    'car': 'moto',
    'road': 'ogba',
    'city': 'urho',
    'work': 'irhu',
    'time': 'akpo',
    'day': 'ede',
    'night': 'orho-ude',
    'sun': 'ozuwa',
    'moon': 'uwevwi',
    'child': 'omo'
}

igbo = {
    'hello': 'ndeewo',
    'food': 'nri',
    'water': 'mmiri',
    'thank you': 'daalụ',
    'school': 'ụlọ akwụkwọ',
    'book': 'akwụkwọ',
    'love': 'ịhụnanya',
    'friend': 'enyi',
    'family': 'ezinụlọ',
    'money': 'ego',
    'car': 'ụgbọala',
    'road': 'ụzọ',
    'city': 'obodo',
    'work': 'ọrụ',
    'time': 'oge',
    'day': 'ụbọchị',
    'night': 'abalị',
    'sun': 'anyanwụ',
    'moon': 'ọnwa',
    'child': 'nwa'
}

igala = {
    'hello': 'aloo',
    'food': 'onyi',
    'water': 'omi',
    'thank you': 'oche',
    'school': 'sukulu',
    'book': 'buku',
    'love': 'ohuma',
    'friend': 'omako',
    'family': 'ogijo',
    'money': 'owo',
    'car': 'moto',
    'road': 'ogba',
    'city': 'otu',
    'work': 'ogba',
    'time': 'ojo',
    'day': 'ojo',
    'night': 'odu',
    'sun': 'ene',
    'moon': 'ole',
    'child': 'oma'
}

hausa = {
    'hello': 'sannu',
    'food': 'abinci',
    'water': 'ruwa',
    'thank you': 'na gode',
    'school': 'makaranta',
    'book': 'littafi',
    'love': 'so',
    'friend': 'aboki',
    'family': 'iyali',
    'money': 'kudi',
    'car': 'mota',
    'road': 'hanya',
    'city': 'birni',
    'work': 'aiki',
    'time': 'lokaci',
    'day': 'rana',
    'night': 'dare',
    'sun': 'rana',
    'moon': 'wata',
    'child': 'yaro'
}

idoma = {
    'hello': 'aloo',
    'food': 'onyi',
    'water': 'omi',
    'thank you': 'oche',
    'school': 'sukulu',
    'book': 'buku',
    'love': 'ohuma',
    'friend': 'omako',
    'family': 'ogijo',
    'money': 'owo',
    'car': 'moto',
    'road': 'ogba',
    'city': 'otu',
    'work': 'ogba',
    'time': 'ojo',
    'day': 'ojo',
    'night': 'odu',
    'sun': 'ene',
    'moon': 'ole',
    'child': 'oma'
}

# Dictionary to map language names to their dictionaries
languages = {
    'Isoko': isoko,
    'Igbo': igbo,
    'Igala': igala,
    'Hausa': hausa,
    'Idoma': idoma
}

# Streamlit page configuration
st.set_page_config(page_title="Language Translator", layout="centered")

# Title and description
st.title("🌍 Language Translator")
st.write("Translate English words to African languages")

# Select language
selected_language = st.selectbox(
    "Choose a language:",
    options=list(languages.keys()),
    key="language_selector"
)

# Get available words for the selected language
current_dictionary = languages[selected_language]
available_words = list(current_dictionary.keys())

# Display available words
st.subheader(f"Available words in {selected_language}:")
st.write(", ".join(available_words))

# Select word with buttons
st.subheader("Select a word to translate:")

# Create columns for word buttons
cols = st.columns(4)
col_index = 0

translation_result = None

for word in available_words:
    with cols[col_index % 4]:
        if st.button(word, key=word, use_container_width=True):
            translation_result = current_dictionary[word]

    col_index += 1

# Display translation result
if translation_result:
    st.success(f"**Translation:** {translation_result}")

# Alternative: Text input option
st.subheader("Or type a word:")
user_word = st.text_input(
    "Enter an English word:",
    placeholder="e.g., hello, food, water thank you"
)

if user_word:
    user_word_lower = user_word.lower()
    if user_word_lower in current_dictionary:
        st.info(f"**{user_word}** in {selected_language} is: **{current_dictionary[user_word_lower]}**")
    else:
        st.warning(f"'{user_word}' is not in the {selected_language} dictionary. Try another word.")

