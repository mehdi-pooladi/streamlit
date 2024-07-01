
import streamlit as st
import requests
import pandas as pd

# تنظیمات اولیه
st.title('نمودار نرخ ارز')

# ورودی کاربر برای انتخاب نماد ارزها
base_currency = st.text_input('ارز پایه را وارد کنید:', 'USD')
target_currency = st.text_input('ارز مقصد را وارد کنید:', 'EUR')

# API key خود را وارد کنید
api_key = 'LYMFOP8X935BUHE4'

# URL درخواست به API
api_url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={base_currency}&to_symbol={target_currency}&apikey={api_key}&datatype=json'

# درخواست به API برای دریافت داده‌ها
response = requests.get(api_url)

# بررسی وضعیت درخواست
if response.status_code == 200:
    data = response.json()


    if "Time Series FX (Daily)" in data:
        time_series = data["Time Series FX (Daily)"]

        # تبدیل داده‌ها به DataFrame
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df = df.apply(pd.to_numeric)

        # اطمینان از اینکه DataFrame به درستی ساخته شده است
        st.write("داده‌های تبدیل شده به DataFrame:", df.head())

        # نمایش نمودار
        st.line_chart(df['4. close'])
        st.write(f"نمودار نرخ {base_currency} به {target_currency}")

    else:
        st.write("خطا در دریافت داده‌ها. لطفاً نمادهای ارز را درست وارد کنید یا دوباره تلاش کنید.")
else:
    st.write("خطا در دریافت داده‌ها.")
