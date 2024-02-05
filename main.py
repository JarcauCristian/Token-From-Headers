import streamlit as st
from redis_cache import get_data_from_redis, is_data_stale

token = get_data_from_redis("token")

if token is not None:
    if is_data_stale(token, 900):
        st.write(token)
    else:
        st.write("Unauthorized!")