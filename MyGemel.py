from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st

# Streamlit UI Customizations
st.title('Best Investment Suggester')
st.markdown('### 📈 Get the best investment options across categories!')
st.markdown('---')

# Fetching and Parsing Data
response = requests.get("https://www.mygemel.net/קופת-גמל-להשקעה")
soup = BeautifulSoup(response.text, 'html.parser')

    # Define categories
categories = [
        "קופת גמל להשקעה - מניות",
        "קופת גמל להשקעה - כללי",
        "קופת גמל להשקעה - מניות חו""ל",
        "קופת גמל להשקעה - ללא מניות",
        "קופת גמל להשקעה - עד 10% מניות",
        "קופת גמל להשקעה - עד 15% מניות",
        "קופת גמל להשקעה - עד 20% מניות",
        "קופת גמל להשקעה - עד 25% מניות",
        "קופת גמל להשקעה - אג""ח ממשלתי",
        "קופת גמל להשקעה- מסלול הלכתי",
        "קופת גמל להשקעה - מסלול פאסיבי",
        "קופת גמל להשקעה - אג""ח קונצרני",
        "קופת גמל להשקעה - אג""ח שקלי טווח קצר",
        "קופת גמל להשקעה - כספית",
        "קופת גמל להשקעה - מט""ח",
        "קופת גמל להשקעה - שריעה"
    ]

final_df = pd.DataFrame(columns=['Category', '1 Year ROI', '3 Years ROI', '5 Years ROI'])

for category in categories:
    header_tag = soup.find("h2", string=category)
    if header_tag:
        table_tag = header_tag.find_next("table")
        if table_tag:
            rows = table_tag.find_all("tr")
            best_5_year_roi = -float("inf")
            best_row_data = []

            for row in rows[1:]:
                cells = row.find_all("td")
                try:
                    five_year_roi = float(cells[4].text.strip('%'))
                except (ValueError, IndexError):
                    continue
                
                if five_year_roi > best_5_year_roi:
                    best_5_year_roi = five_year_roi
                    best_row_data = [cell.text.strip() for cell in cells]
            
            if best_row_data:
                final_df.loc[len(final_df)] = [category, best_row_data[1], best_row_data[2], best_row_data[4]]

# Convert ROI to float and calculate total ROI
for col in ['1 Year ROI', '3 Years ROI', '5 Years ROI']:
    final_df[col] = final_df[col].str.rstrip('%').astype('float')

# Calculate 'Total ROI'
final_df['Total ROI'] = final_df[['1 Year ROI', '3 Years ROI', '5 Years ROI']].sum(axis=1)

# Sort by 'Total ROI'
final_df_sorted = final_df.sort_values('Total ROI', ascending=False)

# Convert back to percentage strings
for col in ['1 Year ROI', '3 Years ROI', '5 Years ROI', 'Total ROI']:
    final_df_sorted[col] = final_df_sorted[col].apply(lambda x: f"{x:.2f}%")

# Initialize session state if not already done
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = ""

# Create top section with summary table
st.subheader('Summary Table')
st.table(final_df_sorted)

# Create a link to the original webpage as the source
st.markdown("Source: [MyGemel.net](https://www.mygemel.net/קופת-גמל-להשקעה)")

# Run the Streamlit app
if __name__ == "__main__":
    st.session_state.selected_category = ""