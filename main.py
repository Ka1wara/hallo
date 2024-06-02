from datetime import date
from pathlib import Path

import streamlit as st

from Person import Person


def person_list_changed():
    st.write(st.session_state["person_list_changes"])
    selected_idx = list()
    for pos in st.session_state["person_list_changes"]["edited_rows"].
st.title("Termin 2 - Aufgabe")
if "PersonList" not in st.session_state:
    file = Path(Person.CSV_FILE_NAME)
    if file.exists():
        df = Person.df_from_file(Person.CSV_FILE_NAME)
        st.session_state["PersonList"] = Person.df_to_list(df)
    else:
        st.session_state["PersonList"] = list()

input_area = st.container(border=True)
out_area = st.container(border=True)
firstname = input_area.text_input(label="Vorname")
lastname = input_area.text_input(label="Nachname")
col1, col2 = input_area.columns(2)
birthdate = col1.date_input(label="Geburtsdatum", min_value=date(1900,1,1), max_value=date.today(), format="DD.MM.YYYY")
col2.text_input(label="Alter", value=Person.age_from_date(birthdate), disabled=True)
if firstname and lastname:
    btn_click = input_area.button(label="Create Person")
    if btn_click:
        person = Person(firstname=firstname, lastname=lastname, birthdate=birthdate)
        st.session_state["PersonList"].append(person)
        Person.as_df(st.session_state["PersonList"]).to_csv(Person.CSV_FILE_NAME)
if len(st.session_state["PersonList"]) > 0:
    column_config = {
        "firstname": st.column_config.TextColumn(label="Vorname"),
        "lastname": st.column_config.TextColumn(label="Nachname"),
        "birthdate": st.column_config.DateColumn(label="Geburtstag", format="DD.MM.YYYY"),
    }
    out_area.dataframe(data=Person.as_df(st.session_state["PersonList"]), use_container_width=True, hide_index=True, column_order=["lastname", "firstname", "birthdate"], column_config=column_config)