# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Setting Layout
st.set_page_config(layout="wide")

# Add Title and Tabs
st.title("Proyek Analisis Data: Bike Sharing Dataset")
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

# Import Dataframe
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Change the Data Type of the "dteday" Column 
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Add Content to Tab
with tab1:
    st.header("Sepanjang tahun, pada bulan apa saja permintaan penyewaan sepeda biasanya mencapai puncaknya?")
    monthly_df = day_df.resample('M', on='dteday').sum()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_df.index, monthly_df['cnt'], color='#6499E9')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Penyewaan Sepeda Sepanjang Waktu (Berdasarkan Bulan dan tahun)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    st.pyplot(plt)

    st.caption("Kesimpulan: Berdasarkan grafik untuk pertanyaan no.1 disimpulkan bahwa Bulan dengan penyewaan sepeda tertinggi adalah bulan Oktober (10) Tahun 2012.")

# Add Content to Tab
with tab2:
    st.header("Berapa rata-rata penyewaan sepeda berdasarkan bulan?")
    monthly_agg = day_df.groupby("mnth").agg({
    "instant": "nunique",
    "cnt": ["mean"]
    })
    monthly_agg = monthly_agg.reset_index()

    monthly_agg["mnth"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.figure(figsize=(16, 8))
    plt.bar(monthly_agg["mnth"],
            monthly_agg[("cnt", "mean")])

    for i in range(len(monthly_agg["mnth"])):
        plt.text(i, monthly_agg[("cnt", "mean")][i],
                str(int(monthly_agg[("cnt", "mean")][i])),
                ha="center", va="bottom")

    plt.title("Rata-rata Penyewaan sepeda berdasarkan bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah")

    plt.legend(loc="upper left")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}")
    )
    plt.show()
    st.pyplot(plt)

    st.caption("Kesimpulan: Berdasarkan grafik untuk pertanyaan no.2 disimpulkan bahwa rata-rata bulan dengan penyewaan sepeda tertinggi adalah bulan Juni.")