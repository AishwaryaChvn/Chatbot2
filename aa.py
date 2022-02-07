import streamlit as st
import request
import pandas as pd

# http://127.0.01:5000/ is from the flask api
response = request.get("http://127.0.01:5000/")
print(response.json())
