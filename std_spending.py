import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# @st.cache
def load_data():
    return pd.read_csv('student_spending.csv')

data = load_data()

# Page configurations
st.set_page_config(
    page_title="Student Spending Analysis",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main {
}
.sidebar{
    background-color: #fff;
}
.desc{
border: 2px solid white;
// width = 50px;
padding: 0 20px;
margin: 0px 20px 20px 10px;
border-radius: 20px;
}
.footer {
        position: fixed;
        bottom: 0;
        width: 100vw;
        color: white;
        background: black;
        text-align: center;
        z-index: 10000;
        left: -1px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_option('deprecation.showPyplotGlobalUse', False)
# Create navigation bar
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "EDA", 'Visualization'])
    page = page.split(" ")[0]
    data = pd.read_csv('student_spending.csv')
    df = data.copy()
    if page == "Home":
        st.title("Welcome to Student Spending Analysis App")
        st.write("This app helps you analyze student spending data.")
        st.markdown("""
#### Information about columns
* **Age:** Age of the student (in years)\n
* **Gender:**  Gender of the student (Male, Female, Non-binary)\n
* **Year in School:** Year of study (Freshman, Sophomore, Junior, Senior)\n
* **Major:** Field of study or major\n
* **Monthly Expenses (in dollars)**\n
* **Monthly Income: Monthly income of the student**\n
* **Financial Aid:** Financial aid received by the student\n
* **Tuition:** Expenses for tuition\n
* **Housing:** Expenses for housing\n
* **Food:** Expenses for food\n
* **Transportation:** Expenses for transportation\n
* **Books & Supplies:** Expenses for books and supplies\n
* **Entertainment:** Expenses for entertainment\n
* **Personal Care:** Expenses for personal care items\n
* **Technology:** Expenses for technology\n
* **Health & Wellness:** Expenses for health and wellness\n
* **Miscellaneous:** Miscellaneous expenses\n
* **Preferred Payment Method**\n
* **Preferred Payment Method:** Cash, Credit/Debit Card, Mobile Payment App\n
* **Additionaly columns created by me**\n
* **Total Monthly Income:** Addition of all the income sources\n
* **Total Monthly Expenses:** Addition of all the expense sources\n
                    
#### Preferred Payment Method
* **Preferred Payment Method:** Cash, Credit/Debit Card, Mobile Payment App\n
""")

    elif page == "EDA":
        st.title("Exploratory Data Analysis")
        st.markdown("""
<p class="desc">This section provides an overview of the dataset through various analytical components. It includes descriptive statistics, data types, and the shape of the dataset. Use the sections below to explore different aspects of the dataset.</p>
""",unsafe_allow_html=True)
        # Add your data analysis components here
        st.header("Data Set")
        st.dataframe(df.head())
        st.markdown("#### Shape of Data")
        st.markdown("""
<p class="desc">Here, you can see the dimensions of the dataset represented as rows and columns. This information gives you an understanding of the dataset's size and structure.</p>
""",unsafe_allow_html=True)
        st.write(df.shape)
        st.markdown("### Data Types")
        st.markdown("""
<p class="desc">
                    Explore the data types of each column in the dataset. Understanding the data types is crucial for data preprocessing and analysis.
                    </p>
""",unsafe_allow_html=True)
        st.write(df.dtypes)

        st.markdown("## Descriptive Statistic of Data")
        st.markdown("""
<p class="desc">
                    Get insights into the central tendencies and spread of numerical features in the dataset. These descriptive statistics help in understanding the distribution and variability of the data.
                    </p>
""",unsafe_allow_html=True)
        st.write(df.describe())

        st.markdown("")

    elif page == "Visualization":
        # Pie Chart
        catigories = ['major','gender','year_in_school','age','preferred_payment_method']
        st.title("Pie Chart")
        cat = st.selectbox("Select Categories,",catigories)
        # Add your visualization components
        st.markdown(f"""
        <h3>Distribution of {cat.capitalize().replace('_'," ")} in the Data Set </h3>
        """,unsafe_allow_html=True)
        st.markdown(f"""
        <p class="desc">The Pie Chart Vizualize the Distribution of {cat.capitalize().replace('_'," ")} among  the total Student in the Data Set. It provides insigts into the portions of different {cat.capitalize().replace('_'," ")} values, allowing for the quick understanding of the dataset's composition. Use the dropdown menu to select different categories to explore </p>
        """,unsafe_allow_html=True)
        fig, ax_pie = plt.subplots()
        major_counts = data[cat].value_counts()
        plt.figure(figsize=(3, 8))  # Adjust the size of the figure
        ax_pie.pie(major_counts, labels=major_counts.index, autopct='%1.1f%%', startangle=140)
        ax_pie.axis('equal')
        ax_pie.legend(title="Legend", loc="upper right", fontsize="small", fancybox=True,bbox_to_anchor=(2, 1))
        ax_pie.set_title(f"{cat.capitalize().replace('_',' ')} Percentage in Data set.")
    
        st.pyplot(fig)
        del fig,ax_pie
        # Bar Chart
        fig, ax_pie = plt.subplots()

        st.title("Bar Chart")
        expenses_columns = ['monthly_income','financial_aid','tuition','housing','food','transportation','books_supplies', 'entertainment', 'personal_care', 'technology','health_wellness','miscellaneous']
        cate = st.selectbox("Select ",expenses_columns)
        num_bin = 10
        num_bin = int(st.selectbox("No of Students",range(10,1000,5)))
        fig, ax = plt.subplots()
        ax.bar(df.head(num_bin).index, df[cate].head(num_bin))
        ax.legend([cate], title="Legend", loc="upper right", fontsize="small", fancybox=True, bbox_to_anchor=(1.9, 1))
        st.markdown(f"""
        <h3>Top  {num_bin} Students {cate.capitalize().replace("_"," ")} Spendings</h3>

        <p class="desc"> This bar plot displays the spending distribution of the top {num_bin} students in the dataset across different categories. It offers insights into how the spending varies across categories for the selected group of students. Use the dropdown menus to select the spending category and the number of students to analyze.</p>

        """,unsafe_allow_html=True)
        ax.set_xlabel('Category')
        ax.set_ylabel('Spending ($)')
        ax.set_title(f'{cate.capitalize().replace("_"," ")} for top {num_bin} students')
        st.pyplot(fig)
        del fig, ax
        # Histogram
        fig, ax = plt.subplots()
        st.title("Histogram Chart")
        expenses_columns = ['monthly_income','financial_aid','tuition','housing','food','transportation','books_supplies', 'entertainment', 'personal_care', 'technology','health_wellness','miscellaneous']
        cate_hist = st.selectbox("Select Hist ",expenses_columns)
        hist_bin = int(st.selectbox("No of Bins",range(10,1000,5)))

        st.markdown(f"""
        <h3>Distribution {cate_hist.capitalize().replace("_"," ")} Data</h3>

        <p class="desc"> This histogram displays the distribution of {cate_hist.capitalize().replace("_"," ")} data among the students in the dataset. It offers insights into the spread and density of values within the selected category. Use the dropdown menus to select the category and adjust the number of bins for the histogram.</p>

        """,unsafe_allow_html=True)
        plt.title(f'Distrubution of {cate_hist.capitalize().replace("_"," ")} data')
        sns.histplot(df[cate_hist],bins=hist_bin,kde=True)
        plt.legend([cate_hist], title="Legend", loc="upper right", fontsize="small", fancybox=True, bbox_to_anchor=(1.9, 1))
        st.pyplot()

        #Box Plot
        fig, ax = plt.subplots()
        st.title("Box Chart")
        expenses_columns = ['monthly_income','financial_aid','tuition','housing','food','transportation','books_supplies', 'entertainment', 'personal_care', 'technology','health_wellness','miscellaneous']
        catigories = ['major','gender','year_in_school','age','preferred_payment_method']

        x_inp = st.selectbox("Select Cat ",catigories)
        st.write("V/s")
        y_inp = st.selectbox("Select Expence ",expenses_columns)

        st.markdown(f"""
        <h3>Comparision of {y_inp.capitalize().replace("_"," ")} across {x_inp.capitalize().replace("_"," ")}</h3>

        <p class="desc"> This box plot compares the distribution of {y_inp.capitalize().replace("_"," ")} across different categories of {x_inp.capitalize().replace("_"," ")}. It provides insights into the spread and variation of {y_inp.capitalize().replace("_"," ")} within each category, allowing for easy comparison between groups. Use the dropdown menus to select the category for the x-axis and the expense for the y-axis.</p>

        """,unsafe_allow_html=True)
        sns.boxplot(x=x_inp,y=y_inp, data=df)
        plt.xlabel('Categories')
        plt.title('Box Plot of Student Spending')
        plt.legend([x_inp.capitalize().replace("_"," ")],title="Legend", loc="upper right", fontsize="small", fancybox=True, bbox_to_anchor=(1.9, 1))
        plt.xticks(rotation=45) 
        st.pyplot()
        del x_inp,fig, ax
        
        # Violene Plot
        fig_v, ax = plt.subplots()
        st.title("Violine Chart")
        expenses_columns = ['monthly_income','financial_aid','tuition','housing','food','transportation','books_supplies', 'entertainment', 'personal_care', 'technology','health_wellness','miscellaneous']
        catigories = ['major','gender','year_in_school','age','preferred_payment_method']

        x_inp = st.selectbox("Select Cat",catigories)
        st.write("V/s")
        y_inp = st.selectbox("Select Expence",expenses_columns)

        st.markdown(f"""
        <h3>Distribution of {y_inp.capitalize().replace("_"," ")} by {x_inp.capitalize().replace("_"," ")}</h3>

        <p class="desc"> This violin plot displays the distribution of {y_inp.capitalize().replace("_"," ")} across different categories of {x_inp.capitalize().replace("_"," ")}. It provides insights into the spread and density of {y_inp.capitalize().replace("_"," ")} within each category, allowing for comparison between groups. Use the dropdown menus to select the category for the x-axis and the expense for the y-axis.</p>

        """,unsafe_allow_html=True)

        sns.violinplot(x=x_inp,y=y_inp, data=df)
        plt.xlabel('Category')
        plt.xticks(rotation=45) 
        plt.title('Violine Plot of Student Spending')
        plt.legend([x_inp.capitalize().replace("_"," ")],title="Legend", loc="upper right", fontsize="small", fancybox=True, bbox_to_anchor=(1.9, 1))
        st.pyplot(fig_v)
      
    st.markdown("---")

    st.markdown("<footer class='footer'>© 2024 @yawarKhaplu </footer>",unsafe_allow_html=True)




if __name__ == "__main__":
    
    main()
