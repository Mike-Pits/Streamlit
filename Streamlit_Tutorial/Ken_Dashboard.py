# import relevant libraries (visualization, dashboard, data manipulation)
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime


# Load/engineer data


def load_data():
    df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:, :]
    df_agg.columns = ['Video', 'Video title', 'Video publish time', 'Comments added', 'Shares', 'Dislikes', 'Likes',
                      'Subscribers lost', 'Subscribers gained', 'RPM(USD)', 'CPM(USD)', 'Average % viewed',
                      'Average view duration',
                      'Views', 'Watch time (hours)', 'Subscribers', 'Your estimated revenue (USD)', 'Impressions',
                      'Impressions ctr(%)']
    df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time'])
    df_agg['Average view duration'] = df_agg['Average view duration'].apply(lambda x: datetime.strptime(x, '%H:%M:%S'))
    df_agg['Avg_duration_sec'] = df_agg['Average view duration'].apply(
        lambda x: x.second + x.minute * 60 + x.hour * 3600)
    df_agg['Engagement_ratio'] = (df_agg['Comments added'] + df_agg['Shares'] + df_agg['Dislikes'] + df_agg[
        'Likes']) / df_agg.Views
    df_agg['Views / sub gained'] = df_agg['Views'] / df_agg['Subscribers gained']
    df_agg.sort_values('Video publish time', ascending=False, inplace=True)
    df_agg_sub = pd.read_csv('Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
    df_comments = pd.read_csv('Aggregated_Metrics_By_Video.csv')
    df_time = pd.read_csv('Video_Performance_Over_Time.csv')
    df_time['Date'] = pd.to_datetime(df_time['Date'])
    return df_agg, df_agg_sub, df_comments, df_time


df_agg, df_agg_sub, df_comments, df_time = load_data()
# Engineering data

df_agg_diff = df_agg.copy()
metric_date_12mo = df_agg_diff['Video publish time'].max() - pd.DateOffset(months=12)
median_agg = df_agg_diff[df_agg_diff['Video publish time'] >= metric_date_12mo].median()

# metric_data_12mo = df_agg_diff['Video publish time' - pd.DateOffset(months=12)]
# metric_medians12mo = df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_12mo].median()

# Building dashboard


add_sidebar = st.sidebar.selectbox('Aggregate or Individual Video', ('Aggregate Metrics', 'Individual Video Analysis'))
if add_sidebar == 'Aggregate Metrics':
    st.write("Ken Jee YouTube Aggregated Data")

    df_agg_metrics = df_agg[
        ['Video publish time', 'Views', 'Likes', 'Subscribers', 'Shares', 'Comments added', 'RPM(USD)',
         'Average % viewed',
         'Avg_duration_sec', 'Engagement_ratio', 'Views / sub gained']]
    metric_date_6mo = df_agg_metrics['Video publish time'].max() - pd.DateOffset(months=6)
    metric_date_12mo = df_agg_metrics['Video publish time'].max() - pd.DateOffset(months=12)
    metric_medians6mo = df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_6mo].median()
    metric_medians12mo = df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_12mo].median()

    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

if add_sidebar == 'Individual Video Analysis':
    st.write('Ind')
