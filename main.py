import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
st.set_page_config(layout='wide')

def main():
    st.markdown('<div style="text-align: center;"><h1><em>--- Case Study: Datengetriebene Entscheidung ---</em></h1></div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.subheader("Teamarbeit:")
    st.write('''1. Sie sind ein Team von Datenanalysten in einem Unternehmen. 
    Ihr Unternehmen verfügt über seinen eigenen Datensatz, die die Leistung des Unternehmens aufzeichnen. 
    Öffnen Sie eine der verfügbaren Datensätze: jeder Datensatz steht für ein Unternehmen und jedes Unternehmen
    hat sein eigenes Problem.''')
    st.write('''2. Ihre Aufgabe als Team ist es, mithilfe dieses Datensatzes wichtige Informationen herauszufinden 
    und mithilfe dieser Informationen sinnvolle/hilfreiche Entscheidungen zur Verbesserung des Unternehmens zu treffen.''')
    st.write('''3. Die Aufgabe wird dann zu 3 Schritten unterteilt. Lesen Sie die Details zu jeder Aufgabe durch.''')
    st.write('''4. Nicht vergessen: Sie sind eine Gruppe. Nutzen Sie die Möglichkeit, Ihre Meinungen zu äußern und 
    anderen Mitarbeitern Fragen zu stellen, um gute Kommunikation und Zusammenarbeit leisten zu können.''')
    st.write("Viel Erfolg!")
    st.write("_____")
    datasets = ["crime_data.csv","employee_data.csv","food_wastage_data.csv","food_delivery_data.csv"]
    dataset = st.selectbox("Select dataset:", datasets)
    df = pd.DataFrame()
    if dataset == datasets[0]:
        df = pd.read_csv(datasets[0])
        k1,k2,k3 = st.columns(3)
        with k2:
            st.write('''Sie Arbeiten als Datenanalyst bei der LAPD (Los Angeles Police Department). Sie haben den Datensatz,
            deren Einträge den einzelnen Kriminalfall berichtet. Sie wollen irgendeine Lösungsidee finden, 
            um mindestens die Anzahl eines Kriminalfalls zu verringern. Nutzen Sie dazu die Variablen im Datensatz,
            identifizieren Sie jede Variable, was sie bedeutet. Schauen Sie im Internet, falls es schwierig zu verstehen ist.
            ''')
            st.write(" ")
            st.write(" ")
    elif dataset == datasets[1]:
        df = pd.read_csv(datasets[1])
        l1,l2,l3 = st.columns(3)
        with l2:
            st.write('''Sie Arbeiten als Datenanalyst zusammen mit dem HR-Team im Unternehmen. Sie haben den Datensatz,
            der die Mitarbeiterinformationen beschreibt. Sie wollen irgendeine Lösungsidee finden, 
            um die Kündigungsrate der mitarbeiter zu verringern. Nutzen Sie dazu die Variablen im Datensatz,
            identifizieren Sie jede Variable, was sie bedeutet. Schauen Sie im Internet, falls es schwierig zu verstehen ist.
            ''')
            st.write(" ")
            st.write(" ")
    elif dataset == datasets[2]:
        df = pd.read_csv(datasets[2])
        p1,p2,p3 = st.columns(3)
        with p2:
            st.write('''Sie Arbeiten als Datenanalyst in einem Restaurant, der ein Catering-Service anbietet. Sie haben den Datensatz,
            deren Einträge die Business-Historie beschreibt. Sie wollen irgendeine Lösungsidee finden, 
            um die Lebensmittelverschwendung zu verringern. Nutzen Sie dazu die Variablen im Datensatz,
            identifizieren Sie jede Variable, was sie bedeutet. Schauen Sie im Internet, falls es schwierig zu verstehen ist.
            ''')
            st.write(" ")
            st.write(" ")
    elif dataset == datasets[3]:
        df = pd.read_csv(datasets[3])
        q1,q2,q3 = st.columns(3)
        with q2:
            st.write('''Sie Arbeiten als Datenanalyst bei einem Food-Delivery-Unternehmen. Sie haben den Datensatz,
            deren Einträge die Business-Historie berichtet. Sie wollen irgendeine Lösungsidee finden, 
            um mindestens die Business zu verbessern. Nutzen Sie dazu die Variablen im Datensatz,
            identifizieren Sie jede Variable, was sie bedeutet. Schauen Sie im Internet, falls es schwierig zu verstehen ist.
            ''')
            st.write(" ")
            st.write(" ")
    st.write(" ")
    if st.checkbox("Show Full Data"):
        st.write(df)
    else:
        st.write(df.head())
    
    if 'dis' not in st.session_state:
        st.session_state.dis = pd.DataFrame(columns=["Selected","discrete"])
    if 'con' not in st.session_state:
        st.session_state.con = pd.DataFrame(columns=["Selected","continuous"])
    st.write("_____")
    r1,r2,r3 = st.columns(3)
    with r2:
        st.write("Identifizieren Sie zunächst die Variablen.")
        st.write("Gruppieren Sie diese zu den richtigen Klassen (Diskret/Kontinuierlich)")
        st.write("Sie müssen nicht alle Variablen verwenden. Nehmen Sie nur was wichtig sein könnten.")
        st.write(" ")
        st.write(" ")
    a1,a2,a3,a4,a5 = st.columns([2,.5,3,.5,3])
    with a1:
        col = st.radio("Select Column:", df.columns.tolist())
    with a3:
        a31,a32 = st.columns(2)
        with a31:
            if st.button("Put Variable To Discrete"):
                st.session_state.dis = st.session_state.dis.append({"Selected":False, "discrete":col}, ignore_index = True)
                st.toast("Liste aktualisiert!")
        with a32:
            if st.button("Delete Selected", key = "del_1"):
                st.session_state.dis = st.session_state.dis[st.session_state.dis["Selected"] == False]
        st.session_state.dis = st.data_editor(st.session_state.dis, column_config = {
            "Selected": st.column_config.CheckboxColumn("Selected", default = False)
        }, hide_index = True, use_container_width=True)
        
    with a5:
        a51,a52 = st.columns(2)
        with a51:
            if st.button("Put Variable To Continuous"):
                st.session_state.con = st.session_state.con.append({"Selected":False, "continuous":col}, ignore_index = True)
                st.toast("Liste aktualisiert!")  
        with a52:
            if st.button("Delete Selected", key = "del_2"):
                st.session_state.con = st.session_state.con[st.session_state.con["Selected"] == False]
        st.session_state.con = st.data_editor(st.session_state.con, column_config = {
            "Selected": st.column_config.CheckboxColumn("Selected", default = False)
        }, hide_index = True, use_container_width=True)
        
    st.write("_____")
    if st.checkbox("Open Visualization"):
        data = []
        cols_x = st.session_state.dis.values[:,1].tolist()
        aggfunc = ["sum","count","mean","min","max","do not group"]
        b1,b2,b3 = st.columns([2,1,2])
        with b2:
            colx = st.selectbox("Pick a Value for x-Axis:", cols_x)
            if len(cols_x) != 0:
                x = df[colx].values.tolist()
                
                # pivot = st.selectbox("choose aggregate function (graph A)",aggfunc)
                # if pivot == "sum":
                #     grouped = df.groupby(colx).sum()
                #     st.success("aggfunc: SUM")
                #     grouped = grouped.sort_index()
                #     x = grouped.index.tolist()
                # elif pivot == "count":
                #     grouped = df.groupby(colx).count()
                #     st.success("aggfunc: COUNT")
                #     grouped = grouped.sort_index()
                #     x = grouped.index.tolist()
                # elif pivot == "mean":
                #     grouped = df.groupby(colx).mean()
                #     st.success("aggfunc: MEAN")
                #     grouped = grouped.sort_index()
                #     x = grouped.index.tolist()
                # elif pivot == "min":
                #     grouped = df.groupby(colx).min()
                #     st.success("aggfunc: MIN")
                #     grouped = grouped.sort_index()
                #     x = grouped.index.tolist()
                # elif pivot == "max":
                #     grouped = df.groupby(colx).max()
                #     st.success("aggfunc: MAX")
                #     grouped = grouped.sort_index()
                #     x = grouped.index.tolist()
                # else:
                #     x = df[colx].values.tolist()
            
        
        style = ["Bar","Scatter","Line"]
        c1,c2,c3 = st.columns([2,1,2])
        with c1:
            cols_ya = st.session_state.con.values[:,1].tolist()
            colya = st.selectbox("Pick a Value for y-Axis (graph A):", cols_ya)
            
            if len(cols_x) != 0:
                pivota = st.selectbox("choose aggregate function (graph A)",aggfunc)
                if pivota == "sum":
                    grouped_a = df.groupby(colx).sum()
                    st.success("aggfunc: SUM")
                    grouped_a = grouped_a.sort_index()
                    x = grouped_a.index.tolist()
                elif pivota == "count":
                    grouped_a = df.groupby(colx).count()
                    st.success("aggfunc: COUNT")
                    grouped_a = grouped_a.sort_index()
                    x = grouped_a.index.tolist()
                elif pivota == "mean":
                    grouped_a = df.groupby(colx).mean()
                    st.success("aggfunc: MEAN")
                    grouped_a = grouped_a.sort_index()
                    x = grouped_a.index.tolist()
                elif pivota == "min":
                    grouped_a = df.groupby(colx).min()
                    st.success("aggfunc: MIN")
                    grouped_a = grouped_a.sort_index()
                    x = grouped_a.index.tolist()
                elif pivota == "max":
                    grouped_a = df.groupby(colx).max()
                    st.success("aggfunc: MAX")
                    grouped_a = grouped_a.sort_index()
                    x = grouped_a.index.tolist()
                else:
                    x = df[colx].values.tolist()

            typea = st.selectbox("Select Plot Style (graph A)", style)
            if len(cols_ya) != 0:
                ya = df[colya].values.tolist()
                if pivota != aggfunc[-1]:
                    try:
                        ya = grouped_a[colya].values.tolist()
                    except:
                        pass
                else:
                    ya = df[colya].values.tolist()
                if typea == "Bar":
                    trace1 = go.Bar(
                    x = x,
                    y = ya,
                    width = .5,
                    textposition='outside',name = colya
                    )
                elif typea == "Scatter":
                    trace1 = go.Scatter(
                    x = x,
                    y = ya,
                    mode = "markers",name = colya
                    )
                elif typea == "Line":
                    trace1 = go.Scatter(
                    x = x,
                    y = ya,
                    mode = "lines",name = colya
                    )
                texta = "Show Graph "+colya +" - "+colx
                if st.checkbox(texta, key = "texta"):
                    try:
                        data.append(trace1)
                    except:
                        pass
        with c3:
            cols_yb = st.session_state.con.values[:,1].tolist()
            colyb = st.selectbox("Pick a Value for y-Axis (graph B):", cols_yb)
            if len(cols_x) != 0:
                pivotb = st.selectbox("choose aggregate function (graph B)",aggfunc)
                if pivotb == "sum":
                    grouped_b = df.groupby(colx).sum()
                    st.success("aggfunc: SUM")
                    grouped_b = grouped_b.sort_index()
                    x = grouped_b.index.tolist()
                elif pivotb == "count":
                    grouped_b = df.groupby(colx).count()
                    st.success("aggfunc: COUNT")
                    grouped_b = grouped_b.sort_index()
                    x = grouped_b.index.tolist()
                elif pivotb == "mean":
                    grouped_b = df.groupby(colx).mean()
                    st.success("aggfunc: MEAN")
                    grouped_b = grouped_b.sort_index()
                    x = grouped_b.index.tolist()
                elif pivotb == "min":
                    grouped_b = df.groupby(colx).min()
                    st.success("aggfunc: MIN")
                    grouped_b = grouped_b.sort_index()
                    x = grouped_b.index.tolist()
                elif pivotb == "max":
                    grouped_b = df.groupby(colx).max()
                    st.success("aggfunc: MAX")
                    grouped_b = grouped_b.sort_index()
                    x = grouped_b.index.tolist()
                else:
                    x = df[colx].values.tolist()

            typeb = st.selectbox("Select Plot Style (graph B)", style)
            if len(cols_yb) != 0:
                yb = df[colyb].values.tolist()
                if pivotb != aggfunc[-1]:
                    try:
                        yb = grouped_b[colyb].values.tolist()
                    except:
                        pass
                else:
                    yb = df[colyb].values.tolist()
                if typeb == "Bar":
                    trace2 = go.Bar(
                    x = x,
                    y = yb,
                    width = .5,
                    textposition='outside',name = colyb
                    )
                elif typeb == "Scatter":
                    trace2 = go.Scatter(
                    x = x,
                    y = yb,
                    mode = "markers",name = colyb
                    )
                elif typeb == "Line":
                    trace2 = go.Scatter(
                    x = x,
                    y = yb,
                    mode = "lines",name = colyb
                    )
                textb = "Show Graph "+colyb +" - "+colx
                if st.checkbox(textb, key = "textb"):
                    try:
                        data.append(trace2)
                    except:
                        pass
        st.write("___")        
                
                
        d1,d2,d3 = st.columns([.5,4,.5])
        with d2:                       
            fig = go.Figure(data = data)
            fig.update_layout(template="plotly_dark",
            autosize=True, height = 600
            )
            st.plotly_chart(fig, use_container_width=True)
    st.write("_____")
    st.subheader("Discussion / Conclusion")
    st.write('''Sie haben explorative Datenanalyse durchgeführt. Diskutieren Sie jetzt mit der Gruppe, 
    welche Maßnahmen das Unternehmen zur Verbesserung der Unternehmenssituation genommen werden können. 
    Erzählen Sie über Ihre Ideen als einen kleinen Vortrag.''')
        



main()