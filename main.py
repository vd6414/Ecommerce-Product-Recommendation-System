import streamlit as st
import pandas as pd
import base64
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="E-Commerce Recommendation System",
    page_icon="🛒",
    layout="wide",
    
)

st.title("🛒 E-Commerce Product Recommendation System")
st.write("Search for a product and get the top 5 similar recommendations.")

df = pd.read_csv("new_data.csv")

tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(df["Features"])

st.sidebar.title("🔍 Filters")

# Category Filter
categories = ["All"] + sorted(df["Category"].unique().tolist())

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

# Price Filter
min_price = int(df["Price"].min())
max_price = int(df["Price"].max())

selected_price = st.sidebar.slider(
    "Maximum Price (₹)",
    min_value=min_price,
    max_value=max_price,
    value=max_price
)

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

filtered_df = filtered_df[
    filtered_df["Price"] <= selected_price
]

def recommend(product_name):

    if product_name not in df["Product_Name"].values:
        return None

    index = df[df["Product_Name"] == product_name].index[0]

    # Compute similarity only for the selected product
    sim_scores = cosine_similarity(
        tfidf_matrix[index:index+1],
        tfidf_matrix
    ).flatten()

    top_indices = sim_scores.argsort()[::-1][1:6]

    return df.iloc[top_indices]

if len(filtered_df) == 0:
    st.warning("No products match the selected filters.")
    st.stop()

product = st.selectbox(
    "🔍 Search Product",
    sorted(filtered_df["Product_Name"].unique())
)

# -------------------------------------------------
# Recommend Button
# -------------------------------------------------
if st.button("Recommend"):

    selected = df[df["Product_Name"] == product].iloc[0]

    st.subheader("📦 Selected Product")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Product Name:** {selected['Product_Name']}")
        st.write(f"**Category:** {selected['Category']}")
        st.write(f"**Brand:** {selected['Brand']}")
        st.write(f"**Price:** ₹{selected['Price']}")
        st.write(f"**Rating:** ⭐ {selected['Rating']}")

    with col2:
        st.write("### Features")
        st.write(selected["Features"])

    st.divider()

    st.subheader("⭐ Top 5 Recommended Products")

    recommendations = recommend(product)

    if recommendations is not None and len(recommendations) > 0:

        for i, row in recommendations.iterrows():

            with st.container():

                st.markdown(f"### {row['Product_Name']}")

                col1, col2 = st.columns([2,1])

                with col1:
                    st.write(f"**Category:** {row['Category']}")
                    st.write(f"**Brand:** {row['Brand']}")
                    st.write(f"**Price:** ₹{row['Price']}")
                    st.write(f"**Rating:** ⭐ {row['Rating']}")
                    st.write(f"**Features:** {row['Features']}")

                st.divider()

    else:
        st.error("No recommendations found.")