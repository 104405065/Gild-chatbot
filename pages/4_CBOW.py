import streamlit as st
from utils import train_word2vec, sentence_vector, preprocess_sentence


st.title("CBOW Model - Test Your Own Sentence")

# 訓練資料
sentences = [
    "What are focus groups?",
    "How are they distinct from ordinary group discussions and what use are they anyway?",
    "This article introduces focus group methodology, explores ways of conducting such groups and examines what this technique of data collection can offer researchers in general and medical sociologists in particular.",
    "It concentrates on the one feature which inevitably distinguishes focus groups from one-to-one interviews or questionnaires",
    "namely the interaction between research participants - and argues for the overt exploration and exploitation of such interaction in the research process.",
    "Group discussions in their widest sense have continued to be popular as a method of data collection throughout the 1970s and 80s within particular niches.",
    "This article attempts to redress the balance through a detailed examination of the interactions between the research participants on the AIDS Media Research Project.",
    "The AIDS Media Research Project: Why focus groups were used and how they were selected",
    "The AIDS Media Research Project was a three-pronged study of the production, content and effect of media messages about AIDS",
    "Focus groups were used to examine the 'effect' element in this equation - to explore how media messages are processed by audiences and how understandings of AIDS are constructed."
]

# ✅ 訓練 CBOW (sg=0)
model = train_word2vec(sentences, sg=0)

# 使用者輸入測試句子
user_input = st.text_input("請輸入您想測試的句子：", "What are focus groups?")
if user_input:
    processed_sentence = preprocess_sentence(user_input)
    st.write("Tokenized Sentence:", processed_sentence)

    # 計算句子向量
    new_sentence_vec = sentence_vector(processed_sentence, model)
    st.subheader("New Sentence Vector (mean of word vectors):")
    st.write(new_sentence_vec)
    st.write(f"向量 shape: {new_sentence_vec.shape}")

    # 顯示 focus 的相似詞
    if 'focus' in model.wv:
        st.subheader("Most Similar Words to 'focus':")
        similar_words = model.wv.most_similar('focus')
        for word, score in similar_words:
            st.write(f"{word}: {score:.4f}")
    else:
        st.error("'focus' is not in vocabulary!")