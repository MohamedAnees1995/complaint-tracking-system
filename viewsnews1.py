# Data display issue in views with existing Database test_voice_analytics 
from concurrent.futures import ThreadPoolExecutor
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AgentDataForm
import pandas as pd
import pymysql.cursors
import time
import matplotlib.pyplot as plt
#from sqlalchemy import create_engine
from django.db import connection
import json
import datetime as dt
from datetime import datetime, timedelta
import random
import re
import base64
# from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
#import squarify
#import matplotlib.pyplot as plt
import seaborn as sns
import io
import  base64
#from unidecode import unidecode
import os
from os import path 
from wordcloud import WordCloud 

# class create for new word summary by junaid 30 Apr 2024
class Word:
    def __init__(self, word, start, end, confidence, punctuated_word, speaker, speaker_confidence, sentiment, sentiment_score):
        self.word = word
        self.start = float(start) if start != "None" else None
        self.end = float(end) if end != "None" else None
        self.confidence = float(confidence) if confidence != "None" else None
        self.punctuated_word = punctuated_word
        self.speaker = int(speaker) if speaker != "None" else None
        self.speaker_confidence = float(speaker_confidence) if speaker_confidence != "None" else None
        self.sentiment = sentiment if sentiment != "None" else None
        self.sentiment_score = float(sentiment_score) if sentiment_score != "None" else None
# class create for new word summary by junaid 30 Apr 2024

def connection():
	conn = pymysql.connect(
		host = "192.168.0.180",
		user = "root",
		password = "Opo@1234",
		database = "voiceanalytics",
		charset='utf8mb4')
	return conn

def vm_connection():
	conn = pymysql.connect(
		host = "192.168.0.180",
		user = "root",
		password = "Opo@1234",
		database = "VAmodel_db",
		charset='utf8mb4')
	return conn

def master(request):
	return render(request,'master.html')
  
###########################################Login code #################################################################    
    
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        query = """
        SELECT name, role FROM users WHERE opoid = %s AND password = %s LIMIT 1;
        """
        with connection().cursor() as cursor:
            cursor.execute(query, [username, password])
            userinfo = cursor.fetchone()  # Fetch the first row
        
        if userinfo:
            name, role = userinfo
            print(f"Name: {name}, Role: {role}")
            request.session['name'] = name
            request.session['opoid'] = username
            request.session['role'] = role
            print(request.session.get('opoid'))
            data = "1"
            return HttpResponse(json.dumps({'data': data}), content_type="application/json")
        else:
            data = "3"
            return HttpResponse(json.dumps({'data': data}), content_type="application/json")
    else:
        return render(request, 'login.html')

###########################################Login code #################################################################
    
#############################Modified dashboard code with optimized SQL queries##########################################

def fetch_data(query):
    cache_key = hash(query)
    data = cache.get(cache_key)
    if data is None:
        conn = connection()
        data = pd.read_sql(query, conn)
        conn.close()
        cache.set(cache_key, data, timeout=60*15)  # Cache for 15 minutes
    return data

def dashboard(request):
    user = request.session.get('opoid')

    if not request.session.session_key:
        request.session.save()

    session_id = request.session.session_key

    if user is None:
        return redirect('/')

    # Define SQL queries
    queries = {
        "datastatus_query": """
            SELECT COUNT(id) AS call_evaluted,
                   FORMAT(AVG(positivescore), 2) AS positive,
                   FORMAT(AVG(negativescore), 2) AS negative,
                   FORMAT(AVG(neutralscore), 2) AS neutral,
                   FORMAT(AVG(qualityscore), 2) AS quality_score
            FROM calltrans
            WHERE calldate >= DATE_SUB(CURDATE(), INTERVAL 6 DAY);
        """,
        "df_highlight_query": """
            SELECT COUNT(*) AS call_evaluted,
                   FORMAT(AVG(positivescore), 2) AS positive,
                   FORMAT(AVG(negativescore), 2) AS negative,
                   FORMAT(AVG(neutralscore), 2) AS neutral
            FROM calltrans
            WHERE calldate >= DATE_SUB(NOW(), INTERVAL 8 DAY);
        """,
        "calls_by_date_query": """
            SELECT DATE_FORMAT(calldate, '%Y-%m-%d') AS lastdate,
                   COUNT(calldate) AS total_call
            FROM calltrans
            WHERE calldate >= DATE_SUB(NOW(), INTERVAL 7 DAY)
            GROUP BY calldate;
        """,
        "pnn_data_query": """
            SELECT DATE_FORMAT(calldate, '%Y-%m-%d') AS lastdate,
                   FORMAT(AVG(positivescore), 2) AS positive,
                   FORMAT(AVG(negativescore), 2) AS negative,
                   FORMAT(AVG(neutralscore), 2) AS neutral
            FROM calltrans
            WHERE calldate >= DATE_SUB(NOW(), INTERVAL 7 DAY)
            GROUP BY calldate;
        """,
        "disposition_query": """
            SELECT CONCAT(disposition, '-', subdisposition) AS title,
                   COUNT(*) AS disposition_count
            FROM voiceanalytics.calltrans
            JOIN VAmodel_db.test_ai ON VAmodel_db.test_ai.connid = calltrans.connid
            WHERE calldate >= DATE_SUB(NOW(), INTERVAL 7 DAY)
            GROUP BY disposition
            HAVING disposition REGEXP '^[^0-9]+$'
            ORDER BY COUNT(*) DESC;
        """,
        "quality_attr_query": """
            SELECT CAST((SUM(CASE WHEN t1.Opening = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS Opening,
                   CAST((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Self Company Introduction`,
                   CAST((SUM(CASE WHEN t1.Verification = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS Verification,
                   CAST((SUM(CASE WHEN t1.RPC = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS RPC,
                   CAST((SUM(CASE WHEN t1.Proactive_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `DIY Adherence`,
                   CAST((SUM(CASE WHEN t1.Disposition1 = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Disposition`,
                   CAST((SUM(CASE WHEN t1.Personalization = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Personalization`,
                   CAST((SUM(CASE WHEN t1.Dead_Air = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Dead Air`,
                   CAST((SUM(CASE WHEN t1.Hold_Protocol = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Hold Protocol`,
                   CAST((SUM(CASE WHEN t1.Due_Date_communication = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Due Date communication`,
                   CAST((SUM(CASE WHEN t1.Appropriate_closing = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Appropriate closing`,
                   CAST((SUM(CASE WHEN t1.PTP_Detail_FPTP = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `PTP Detail FPTP`,
                   CAST((SUM(CASE WHEN t1.Script_Adherence = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Script Adherence`,
                   CAST((SUM(CASE WHEN t1.Disclaimer = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS Disclaimer
            FROM VAmodel_db.test_ai AS t1
            JOIN calltrans c ON t1.connid = c.connid
            WHERE DATE(c.calldate) <= CURDATE()
            AND DATE(c.calldate) > DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 7 DAY), '%Y-%m-%d');
        """,
        "quality_score_query": """
            SELECT ROUND(AVG(t.score), 2) AS qualityscore
            FROM VAmodel_db.test_ai t
            JOIN voiceanalytics.calltrans c ON t.connid = c.connid
            WHERE DATE(c.calldate) <= CURDATE()
            AND DATE(c.calldate) > DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 7 DAY), '%Y-%m-%d');
        """,
        "word_freq_query": """
            SELECT Word_Occurrence AS word, COUNT(*) AS word_count
            FROM voiceanalytics.WordFinder
            WHERE DATE(calldate) >= DATE_FORMAT(DATE_SUB(NOW(), INTERVAL 7 DAY), '%Y-%m-%d')
            AND Word_Occurrence != ''
            GROUP BY Word_Occurrence
            ORDER BY word_count DESC
            LIMIT 10;
        """
    }

    # Use ThreadPoolExecutor to fetch data concurrently
    with ThreadPoolExecutor() as executor:
        results = {name: executor.submit(fetch_data, query) for name, query in queries.items()}
        
        # Collect results
        datastatus = results['datastatus_query'].result()
        df_highlight_data = results['df_highlight_query'].result()
        df_tc_date = results['calls_by_date_query'].result()
        pnn_data = results['pnn_data_query'].result()
        disposition_average_count = results['disposition_query'].result().to_dict('records')
        quality_attr = results['quality_attr_query'].result().to_dict('records')
        qualityScore = results['quality_score_query'].result().to_dict('records')
        word_freq = results['word_freq_query'].result().to_dict('records')

    # Extract values from datastatus
    evaluated_call = datastatus['call_evaluted'][0] if datastatus['call_evaluted'][0] is not None else 0
    positive_call = datastatus['positive'][0] if datastatus['positive'][0] is not None else 0
    negative_call = datastatus['negative'][0] if datastatus['negative'][0] is not None else 0
    neutral_call = datastatus['neutral'][0] if datastatus['neutral'][0] is not None else 0
    quality_score = datastatus['quality_score'][0] if datastatus['quality_score'][0] is not None else 0

    # Prepare date list and call counts
    date_list = [(dt.datetime.today() - dt.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(7)]
    call_counts = {row['lastdate']: row['total_call'] for row in df_tc_date.to_dict('records')}
    
    final_gp1 = {f'lastdate_{index}': call_counts.get(date, 0) for index, date in enumerate(date_list)}

    # Prepare PNN data
    pnn_data = pnn_data.to_dict('records')

    # Generate Word Cloud
    word_freq_dict = {row['word']: row['word_count'] for row in word_freq}
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq_dict)
    buffer = io.BytesIO()
    img = wordcloud.to_image()
    img.save(buffer, 'png')
    b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Prepare quality attributes
    sorted_list = [{'key': k, 'value': v if v is not None else 0} for k, v in quality_attr[0].items()]
    finallist = sorted_list
    
    # Prepare disposition average count
    disposition_average_count = []
    for item in results['disposition_query'].result().to_dict('split')['data']:
        disposition_average_count.append({"title": item[0], "count": item[1]})

    context = {
        'calldata': df_tc_date.to_dict('records'),
        'evaluated_call': evaluated_call,
        'positive': positive_call,
        'negative': negative_call,
        'neutral': neutral_call,
        'sentiment': pnn_data,
        'wordcloud': b64,
        'qa_score': qualityScore,
        'attribut_val': finallist,
        'disp_qry': disposition_average_count,
        'final_gp1': final_gp1,
        'word_freq':word_freq
    }

    return render(request, 'dashboard.html', context)
#############################Modified dashboard code with optimized SQL queries##########################################

#####################Working fast parameterized code for dashboard date filter #########################################

def dashboard_date_filter(request):
	user = request.session.get('opoid')
	if user is None:
		return redirect('/')
	else:
		if request.method =='POST':
			fromdate = request.POST.get('startdata')
			todate = request.POST.get('enddata')
			request.session['fromdate_dash'] = fromdate
			request.session['todate_dash'] = todate

			print()
			print("====================================================================")
			print("fromdate :", fromdate)
			print("todate :", todate)
			print("====================================================================")
			print()
		
			conn = connection()

			# Aggregated Data
			datastatus_query = f"""
				SELECT 
					COUNT(*) AS call_evaluted, 
					FORMAT(AVG(positivescore), 2) AS positive, 
					FORMAT(AVG(negativescore), 2) AS negative, 
					FORMAT(AVG(neutralscore), 2) AS neutral,
					FORMAT(AVG(score), 2) AS quality_score 
				FROM calltrans join VAmodel_db.test_ai on calltrans.connid = VAmodel_db.test_ai.connid
				WHERE calldate BETWEEN '{fromdate}' and '{todate}';
			"""
			datastatus = pd.read_sql(datastatus_query, conn)

			df_highlight_query = f"""
				SELECT 
					COUNT(*) AS call_evaluted, 
					FORMAT(AVG(positivescore), 2) AS positive, 
					FORMAT(AVG(negativescore), 2) AS negative, 
					FORMAT(AVG(neutralscore), 2) AS neutral 
				FROM calltrans 
				WHERE calldate BETWEEN '{fromdate}' and '{todate}';
			"""
			df_highlight_data = pd.read_sql(df_highlight_query, conn)
			
			evaluated_call = datastatus['call_evaluted'][0]
			positive_call = datastatus['positive'][0]
			negative_call = datastatus['negative'][0]
			neutral_call = datastatus['neutral'][0]
			quality_score = datastatus['quality_score'][0]
			
			# Date List Preparation
			date_list = [(dt.datetime.today() - dt.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(7)]
			
			# Calls by Date
			calls_by_date_query = f"""
				SELECT 
					DATE_FORMAT(calldate, '%Y-%m-%d') AS lastdate, 
					COUNT(calldate) AS total_call 
				FROM calltrans 
				WHERE calldate BETWEEN '{fromdate}' and '{todate}' 
				GROUP BY calldate;
			"""
			df_tc_date = pd.read_sql(calls_by_date_query, conn)
			data = df_tc_date.to_dict('records')
			
			# Processing Data
			final_gp1 = {f'lastdate_{index}': 0 for index in range(7)}
			for index, date in enumerate(date_list):
				for record in data:
					if record['lastdate'] == date:
						final_gp1[f'lastdate_{index}'] = record['total_call']
						break

			# Chart 2 Data
			pnn_data_query = f"""
				SELECT 
					DATE_FORMAT(calldate, '%Y-%m-%d') AS lastdate,
					FORMAT(AVG(positivescore), 2) AS positive, 
					FORMAT(AVG(negativescore), 2) AS negative, 
					FORMAT(AVG(neutralscore), 2) AS neutral 
				FROM calltrans 
				WHERE calldate BETWEEN '{fromdate}' and '{todate}' 
				GROUP BY calldate;
			"""
			df_pnn_data = pd.read_sql(pnn_data_query, conn)
			pnn_data = df_pnn_data.to_dict('records')
			
			sizes, label, unique, wordcldtxt = wordtree('NO')
			try:
				img = generate_wordcloud(wordcldtxt)
			except Exception as e:
				img = 'hello'
				print(e)
			
			disp_qry = pd.read_sql(f"select concat(disposition,'-',subdisposition) as disposition, COUNT(*) AS disposition_count from voiceanalytics.calltrans join VAmodel_db.test_ai on VAmodel_db.test_ai.connid= calltrans.connid where calldate BETWEEN '{fromdate}' and '{todate}'  GROUP BY disposition HAVING disposition REGEXP '^[^0-9]+$' order by count(*) desc;",conn)
			
			disposition_average_count = []

			disp_qry = disp_qry.to_dict('split')
			print(disp_qry)
			for i in disp_qry['data']:
				disposition_average_count.append({"title":""+i[0]+"","count":i[1]},)
			
			# Quality Attributes Data
			quality_attr_query = f"""
				SELECT 
					CAST((SUM(CASE WHEN t1.Opening = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS Opening,
					CAST((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Self Company Introduction`,
					CAST((SUM(CASE WHEN t1.Verification = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS Verification,
					CAST((SUM(CASE WHEN t1.RPC = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS RPC,
					CAST((SUM(CASE WHEN t1.Proactive_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `DIY Adherence`,
					CAST((SUM(CASE WHEN t1.Disposition1 = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Disposition`,
					CAST((SUM(CASE WHEN t1.Personalization = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Personalization`,
					CAST((SUM(CASE WHEN t1.Dead_Air = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Dead Air`,
					CAST((SUM(CASE WHEN t1.Hold_Protocol = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Hold Protocol`,
					CAST((SUM(CASE WHEN t1.Due_Date_communication = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Due Date communication`,
					CAST((SUM(CASE WHEN t1.Appropriate_closing = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Appropriate closing`,
					CAST((SUM(CASE WHEN t1.PTP_Detail_FPTP = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `PTP Detail FPTP`,
					CAST((SUM(CASE WHEN t1.Script_Adherence = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS `Script Adherence`,
					CAST((SUM(CASE WHEN t1.Disclaimer = 'MET' THEN 1 ELSE 0 END) / COUNT(*) * 100) AS DECIMAL(18, 2)) AS Disclaimer 
				FROM VAmodel_db.test_ai AS t1 
				JOIN calltrans c ON t1.connid = c.connid 
				WHERE c.calldate BETWEEN '{fromdate}' and '{todate}';
			"""
			quality_attr = pd.read_sql(quality_attr_query, conn)
			sorted_list = [{'key': k, 'value': v} for k, v in quality_attr.iloc[0].items()]
			finallist = sorted_list
			
			# Quality Score Data
			quality_score_query = f"""
				SELECT ROUND(AVG(t.score), 2) AS qualityscore 
				FROM VAmodel_db.test_ai t 
				JOIN voiceanalytics.calltrans c ON t.connid = c.connid 
				WHERE c.calldate BETWEEN '{fromdate}' and '{todate}';
			"""
			qualityScore = pd.read_sql(quality_score_query, conn)
			
			# Word Frequency Data
			word_freq = pd.read_sql(f"SELECT COALESCE(t.Word_Occurrence, 'N/A') AS word,COALESCE(t.word_count, 0) AS word_count FROM ( SELECT Word_Occurrence, count(*) AS word_count FROM voiceanalytics.WordFinder WHERE date(calldate) BETWEEN '{fromdate}' AND '{todate}' AND Word_Occurrence != '' GROUP BY Word_Occurrence ORDER BY word_count DESC LIMIT 10) AS t RIGHT JOIN (SELECT 1) AS dummy ON 1 = 1;", conn)
			
			word_freq = word_freq.to_dict('records')

			word_freq_dict = {row['word']: row['word_count'] for row in word_freq}
			
			if word_freq[0]['word_count'] == 0:
				word_freq_dict = "No Data found:1,Missing:2,Not present:3,Nonexistent:4,Lacking:5"
				
				word_freq_dict = {word.strip(): int(count) for word, count in (item.split(':') for item in word_freq_dict.split(','))}
			
			wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq_dict)
			img = wordcloud.to_image()
			buffer = io.BytesIO()
			img.save(buffer, 'png')
			b64 = base64.b64encode(buffer.getvalue())
					
			conn.close()

			context = {'calldata':data,'evaluated_call':evaluated_call,'positive':positive_call,'negative':negative_call,'neutral':neutral_call,'sentiment':pnn_data,'sizes':str(sizes)[1:-1].replace("'",'"'),'label':str(label)[1:-1].replace("'",'"'),"wordcloud":str(b64)[2:-3],'qa_score':qualityScore.to_dict('records'),'attribut_val':finallist,'disp_qry':disposition_average_count,'fromdate':fromdate,'todate':todate,'word_freq':word_freq}
			return render(request,'dashboard.html',context)
		else:
			return redirect('dashboard')

#####################Working fast parameterized code for dashboard date filter #########################################

def wordtree(connid):
	if connid == "NO":
		sql="select id,fulltranscript from calltrans where calldate >= DATE_SUB(NOW(), INTERVAL 7 DAY) LIMIT 10"
	else:
		sql=f"select id,fulltranscript from calltrans where connid='{connid}'"
	con=connection()
	df=pd.read_sql(sql, con)
	wordcldtxt = ' '.join(df['fulltranscript']).lower().split()
	wordcount=pd.Series(' '.join(df['fulltranscript']).lower().split()).value_counts()[:100]
	wordcount=wordcount.reset_index()
	colors=['#fae588','#f79d65','#f9dc5c','#e8ac65','#e76f51','#ef233c','#b7094c'] #color palette
	sns.set_style(style="whitegrid") # set seaborn plot style
	sizes= wordcount[wordcount.columns[1]]# proportions of the categories
	label= list(wordcount["index"])
	unique = set(label).intersection(set(label))
	sizes = list(sizes)
	con.close()
	return sizes,label,unique,wordcldtxt

def wordtree_filter(connid, fromdate, todate):
	wordsList = ["Lawyer", "Repetitive calls", "Unauthorised Visit", "police", "Sr Management", "Threaten", "Social Media", "Reversal", "RBI", "Suicide", "Wrong Identity", "Abusive", "Prime Minister", "Crime", "Court of Law", "MD - CEO", "Legal", "Relatives", "Colleagues - HR", "Harassment"]
	
	if connid == "NO":
		sql=f"select id,fulltranscript from calltrans where calldate BETWEEN '{fromdate}' and '{todate}'"
	else:
		sql=f"select id,fulltranscript from calltrans where connid='{connid}'"
	con=connection()
	df=pd.read_sql(sql, con)
	filtered_words = ' '.join(df['fulltranscript']).lower().split()
	filtered_words = [word for word in filtered_words if word in wordsList]
	wordcount = pd.Series(filtered_words).value_counts()[:100]

	#wordcount=pd.Series(' '.join(df['fulltranscript']).lower().split()).value_counts()[:100]
	
	wordcount=wordcount.reset_index()
	colors=['#fae588','#f79d65','#f9dc5c','#e8ac65','#e76f51','#ef233c','#b7094c'] #color palette
	sns.set_style(style="whitegrid") # set seaborn plot style
	sizes= wordcount[wordcount.columns[1]]# proportions of the categories
	label= list(wordcount["index"])
	unique = set(label).intersection(set(label))
	sizes = list(sizes)
	con.close()
	return sizes,label,unique,filtered_words

def generate_wordcloud(wordcldtxt):
	wordcloud = WordCloud(background_color='white',font_path = '/var/www/html/VA_ICICI/voiceanalytics_main/static/img/TiroDevanagariHindi-Regular.ttf',max_font_size=50).generate(str(wordcldtxt)[1:-1])
	print("==============")
	print("==============")
	img = wordcloud.to_image()
	buffer = io.BytesIO()
	img.save(buffer, 'png')
	b64 = base64.b64encode(buffer.getvalue())

	return b64

def getdates(start_date_str,end_date_str,typex):
    start_date = dt.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end_date_str, '%Y-%m-%d').date()

    # Calculate the number of days in the date range
    num_days = (end_date - start_date).days + 1

    # Create an empty list to store the substrings
    date_substrings = []

    # Generate the substrings for each date within the specified range
    for day in range(num_days):
        current_date = start_date + timedelta(days=day)
        formatted_date = current_date.strftime('%Y-%m-%d')
        substring = f"Format(avg(CASE WHEN calldate = '{formatted_date}' THEN {typex} ELSE NULL END), 2) AS '{formatted_date}',"
        date_substrings.append(substring)

    # Join the substrings into a single string
    result_string = " ".join(date_substrings)
    return result_string[0:-1]

def disp_getdates(start_date_str,end_date_str,typex):
    start_date = dt.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end_date_str, '%Y-%m-%d').date()

    # Calculate the number of days in the date range
    num_days = (end_date - start_date).days + 1

    # Create an empty list to store the substrings
    date_substrings = []

    # Generate the substrings for each date within the specified range
    for day in range(num_days):
        current_date = start_date + timedelta(days=day)
        formatted_date = current_date.strftime('%Y-%m-%d')
        #substring = f"CAST((SUM(CASE WHEN ta.{typex} = 'MET' THEN 1 ELSE 0 END) / COUNT(*)  * 100 )as decimal(18,2)) AS '{formatted_date}',"
        substring = f"CAST((SUM(CASE WHEN ta.{typex} = 'MET' AND c.calldate = '{formatted_date}' THEN 1 ELSE 0 END) / COUNT(CASE WHEN c.calldate = '{formatted_date}' THEN 1 ELSE NULL END) * 100) AS DECIMAL(18, 2)) AS '{formatted_date}',"
        date_substrings.append(substring)

    # Join the substrings into a single string
    result_string = " ".join(date_substrings)
    return result_string[0:-1]

##################################Modified Reports View##################################################################

def execute_query(query, params):
    conn = connection()
    return pd.read_sql(query, conn, params=params)

def reports(request):
    user = request.session.get('opoid')
    if user is None:
        return redirect('/')

    getdata = request.POST.get('searchdata')
    firstdate = request.POST.get('first_date')
    lastdate = request.POST.get('last_date')
    print(getdata, firstdate, lastdate)
    df_get_data = None
    dy_column_name = None
    downloadpath = None

    # Define a mapping for report names
    report_name_map = {
        '1': 'Dump Report',
        '8': 'Wordcloud Report',
        '9': 'Top 50 Calls by Positive Score',
        '10': 'Top 50 Calls by Negative Score'
    }

    # Queries for options 1, 8, 9, 10 (downloadable reports)
    if getdata in ['1', '8', '9', '10']:
        query_map = {
            '1': f"""SELECT c.connid, c.calldate, c.opoid, c.processname, c.disposition, c.subdisposition, 
                      c.total_duration, c.silence_sec, ta.score, c.positivescore, c.negativescore, 
                      c.fulltranscript, c.neutralscore, ta.Opening, ta.Self_Company_Introduction, 
                      ta.Verification, ta.RPC, ta.Disclaimer, ta.Personalization, ta.Dead_Air, 
                      ta.Hold_Protocol, ta.Due_Date_communication, ta.Appropriate_closing, 
                      ta.PTP_Detail_FPTP, ta.Script_Adherence, ta.Proactive_Information, 
                      ta.Disposition1 AS Corr_disposition 
                      FROM (SELECT * FROM calltrans WHERE calldate BETWEEN %s AND %s) AS c 
                      JOIN (SELECT * FROM VAmodel_db.test_ai) AS ta ON c.connid = ta.connid LIMIT 100;""",
            '8': f"""SELECT wf.opoid, wf.connid, wf.Word_Occurrence, ct.fulltranscript, wf.calldate 
                      FROM WordFinder wf JOIN calltrans ct ON wf.connid = ct.connid 
                      WHERE wf.Word_Occurrence != '' AND wf.calldate BETWEEN %s AND %s;""",
            '9': f"""SELECT c.connid, processname, opoid, tlopoid, disposition, subdisposition, calltype, 
                      t.score, fulltranscript, positivescore, negativescore, neutralscore, 
                      calldate, calltime, silence_sec, total_duration, quality_data 
                      FROM voiceanalytics.calltrans c 
                      JOIN VAmodel_db.test_ai t ON c.connid = t.connid 
                      WHERE c.calldate BETWEEN %s AND %s 
                      ORDER BY positivescore DESC LIMIT 50;""",
            '10': f"""SELECT c.connid, processname, opoid, tlopoid, disposition, subdisposition, calltype, 
                       t.score, fulltranscript, positivescore, negativescore, neutralscore, 
                       calldate, calltime, silence_sec, total_duration, quality_data 
                       FROM voiceanalytics.calltrans c 
                       JOIN VAmodel_db.test_ai t ON c.connid = t.connid 
                       WHERE c.calldate BETWEEN %s AND %s 
                       ORDER BY negativescore DESC LIMIT 50;"""
        }

        with ThreadPoolExecutor() as executor:
            future = executor.submit(execute_query, query_map[getdata], [firstdate, lastdate])
            df_get_data = future.result()

        # Create Excel file and set download path for options 1, 8, 9, 10
        if df_get_data is not None:
            filename = random.randint(10000, 99999)
            reportname = report_name_map.get(getdata, 'Default_Report_Name')  # Use the updated mapping to get the report name
            file_path = f'media/dumps/{reportname}_{filename}.xlsx'
            df_get_data.to_excel(file_path, index=False)
            downloadpath = f"/media/dumps/{reportname}_{filename}.xlsx"
            df_get_data = [{'total_count': filename}]

    # Queries for options 2, 3, 4, 5, 6, 7 (display directly on the page)
    elif getdata in ['2', '3', '4','5','6','7']:
        with ThreadPoolExecutor() as executor:
            if getdata == '2':
                query = f"""SELECT c.opoid AS EmployeeID, COUNT(*) AS call_count, 
                             SUM(c.total_duration) AS Call_duration, AVG(c.silence_sec) AS Silence_duration, 
                             FORMAT(AVG(ta.score), 2) AS CQ_scores, 
                             FORMAT(AVG(c.positivescore), 2) AS Positive, 
                             FORMAT(AVG(c.negativescore), 2) AS Negative, 
                             FORMAT(AVG(c.neutralscore), 2) AS Neutral 
                             FROM calltrans c 
                             JOIN VAmodel_db.test_ai ta ON c.connid = ta.connid 
                             WHERE calldate BETWEEN %s AND %s 
                             GROUP BY opoid;"""
                future = executor.submit(execute_query, query, [firstdate, lastdate])
                df_get_data = future.result().to_dict('records')

            elif getdata == '3':
                query = f"""SELECT c.disposition AS Disposition, COUNT(*) AS Total_count, 
                             SUM(c.total_duration) AS Call_duration, AVG(c.silence_sec) AS Silence_duration, 
                             FORMAT(AVG(ta.score), 2) AS CQ_scores, 
                             FORMAT(AVG(c.positivescore), 2) AS Positive, 
                             FORMAT(AVG(c.negativescore), 2) AS Negative, 
                             FORMAT(AVG(c.neutralscore), 2) AS Neutral 
                             FROM calltrans c 
                             JOIN VAmodel_db.test_ai ta ON c.connid = ta.connid 
                             WHERE c.calldate BETWEEN %s AND %s 
                             GROUP BY c.disposition;"""
                future = executor.submit(execute_query, query, [firstdate, lastdate])
                df_get_data = future.result().to_dict('records')

            elif getdata == '4':
                start_date_str = firstdate
                end_date_str = lastdate
                posdatestr = getdates(start_date_str, end_date_str, 'positivescore')
                negativestr = getdates(start_date_str, end_date_str, 'negativescore')
                neutralstr = getdates(start_date_str, end_date_str, 'neutralscore')
                querypos = f"""SELECT opoid AS EmployeeID, 'Positive' AS Sentiment_scores, {posdatestr} 
                               FROM calltrans WHERE calldate BETWEEN '{start_date_str}' AND '{end_date_str}' 
                               GROUP BY EmployeeID UNION ALL """
                queryneg = f"""SELECT opoid AS EmployeeID, 'Negative' AS Sentiment_scores, {negativestr} 
                               FROM calltrans WHERE calldate BETWEEN '{start_date_str}' AND '{end_date_str}' 
                               GROUP BY EmployeeID UNION ALL """
                queryneutr = f"""SELECT opoid AS EmployeeID, 'Neutral' AS Sentiment_scores, {neutralstr} 
                                 FROM calltrans WHERE calldate BETWEEN '{start_date_str}' AND '{end_date_str}' 
                                 GROUP BY EmployeeID ORDER BY EmployeeID;"""
                qry = querypos + queryneg + queryneutr
                future = executor.submit(execute_query, qry, [])
                df = future.result()
                dy_column_name = df.columns
                df_get_data = df.to_html(classes="table table-stripe table-hover mytable", index=False)

            elif getdata == '5':
                print("----in----")
                start_date_str = firstdate
                end_date_str = lastdate
                attrlist = ['Opening', 'Self_Company_Introduction', 'Verification', 'RPC', 'Disclaimer', 'Assertiveness_Confident', 'Enthu_Energy', 'Professionalism_Casual', 'Speech_Clarity_ClearExplanation', 'Pace_Customer_Language', 'Personalization', 'Active_Listening_No_Repetition', 'Dead_Air', 'Hold_Protocol', 'Negotiation_Skils', 'Urgency_Creation', 'Objection_Handling_Rebuttals', 'Due_Date_communication', 'Summarization', 'Appropriate_closing', 'Complete_Information', 'Correct_Information', 'PTP_Detail_FPTP', 'Script_Adherence', 'Proactive_Information', 'Data_Capturing_Remarks']

                qrylist = []

                for i in range(len(attrlist)):
                    qry = disp_getdates(start_date_str, end_date_str, f'{attrlist[i]}')
                    #print(qry)
                    if i == 25:
                        querypos = f"""select c.opoid,'{attrlist[i]}' as 'Attribute_name', {qry} from calltrans 
                            c join VAmodel_db.test_ai ta on c.connid = ta.connid 
                            where c.calldate between '{start_date_str}' and '{end_date_str}'
                            group by c.opoid """
                        qrylist.append(querypos)
                        
                    else:
                        querypos = f"""select c.opoid,'{attrlist[i]}' as 'Attribute_name', {qry} from calltrans 
                        c join VAmodel_db.test_ai ta on c.connid = ta.connid 
                        where c.calldate between '{start_date_str}' and '{end_date_str}'
                        group by c.opoid UNION ALL"""
                        qrylist.append(querypos)


                #print(qrylist[0])
                totalqry = ''
                for i in range(26):
                    totalqry += qrylist[i] + " "
                #print(totalqry)
                future = executor.submit(execute_query, totalqry, [])
                df = future.result()
                
                #df_get_data = df.to_dict('records')
                df_get_data = df.to_html(classes="table table-stripe table-hover mytable", index=False)

            elif getdata == '6':
                print("---in-----")
                start_date_str = firstdate
                end_date_str = lastdate
                attrlist = ['Opening', 'Self_Company_Introduction', 'Verification', 'RPC', 'Disclaimer', 'Assertiveness_Confident', 'Enthu_Energy', 'Professionalism_Casual', 'Speech_Clarity_ClearExplanation', 'Pace_Customer_Language', 'Personalization', 'Active_Listening_No_Repetition', 'Dead_Air', 'Hold_Protocol', 'Negotiation_Skils', 'Urgency_Creation', 'Objection_Handling_Rebuttals', 'Due_Date_communication', 'Summarization', 'Appropriate_closing', 'Complete_Information', 'Correct_Information', 'PTP_Detail_FPTP', 'Script_Adherence', 'Proactive_Information', 'Data_Capturing_Remarks']

                qrylist = []

                for i in range(len(attrlist)):
                    qry = disp_getdates(start_date_str, end_date_str, f'{attrlist[i]}')
                    #print(qry)
                    if i == 25:
                        querypos = f"""select c.disposition,'{attrlist[i]}' as 'Attribute_name', {qry} from calltrans 
                            c join VAmodel_db.test_ai ta on c.connid = ta.connid 
                            where c.calldate between '{start_date_str}' and '{end_date_str}'
                            group by c.disposition """
                        qrylist.append(querypos)
                        
                    else:
                        querypos = f"""select c.disposition,'{attrlist[i]}' as 'Attribute_name', {qry} from calltrans 
                        c join VAmodel_db.test_ai ta on c.connid = ta.connid 
                        where c.calldate between '{start_date_str}' and '{end_date_str}'
                        group by c.disposition UNION ALL"""
                        qrylist.append(querypos)


                #print(qrylist[0])
                totalqry = ''
                for i in range(26):
                    totalqry += qrylist[i] + " "
                #print(totalqry)
                future = executor.submit(execute_query, totalqry, [])
                df = future.result()
                #df_get_data = df.to_dict('records')
                df_get_data = df.to_html(classes="table table-stripe table-hover mytable", index=False)
                #print(df_get_data)

            elif getdata == '7':
                print("---in-----")
                start_date_str = firstdate
                end_date_str = lastdate
                attrlist = ['Opening', 'Self_Company_Introduction', 'Verification', 'RPC', 'Disclaimer', 'Assertiveness_Confident', 'Enthu_Energy', 'Professionalism_Casual', 'Speech_Clarity_ClearExplanation', 'Pace_Customer_Language', 'Personalization', 'Active_Listening_No_Repetition', 'Dead_Air', 'Hold_Protocol', 'Negotiation_Skils', 'Urgency_Creation', 'Objection_Handling_Rebuttals', 'Due_Date_communication', 'Summarization', 'Appropriate_closing', 'Complete_Information', 'Correct_Information', 'PTP_Detail_FPTP', 'Script_Adherence', 'Proactive_Information', 'Data_Capturing_Remarks']

                qrylist = []

                for i in range(len(attrlist)):
                    qry = disp_getdates(start_date_str, end_date_str, f'{attrlist[i]}')
                    #print(qry)
                    if i == 25:
                        querypos = f"""select c.opoid,'{attrlist[i]}' as 'Attribute_name', {qry} from calltrans 
                            c join VAmodel_db.test_ai ta on c.connid = ta.connid 
                            where c.calldate between '{start_date_str}' and '{end_date_str}'
                            group by c.opoid """
                        qrylist.append(querypos)
                        
                    else:
                        querypos = f"""select c.opoid,'{attrlist[i]}' as 'Attribute_name', {qry} from calltrans 
                        c join VAmodel_db.test_ai ta on c.connid = ta.connid 
                        where c.calldate between '{start_date_str}' and '{end_date_str}'
                        group by c.opoid UNION ALL"""
                        qrylist.append(querypos)


                #print(qrylist[0])
                totalqry = ''
                for i in range(26):
                    totalqry += qrylist[i] + " "
                #print(totalqry)
                future = executor.submit(execute_query, totalqry, [])
                df = future.result()
                #df_get_data = df.to_dict('records')
                df_get_data = df.to_html(classes="table table-stripe table-hover mytable", index=False)
                #print(df_get_data)



    # Queries for disposition and subdisposition
    with ThreadPoolExecutor() as executor:
        dispo_future = executor.submit(execute_query, 
            "SELECT disposition FROM calltrans WHERE YEAR(calldate) >= '2024' GROUP BY disposition;", [])
        subdispo_future = executor.submit(execute_query, 
            "SELECT subdisposition FROM calltrans WHERE YEAR(calldate) >= '2024' GROUP BY subdisposition;", [])
        
        dispo_query = dispo_future.result().to_dict('records')
        subdispo_query = subdispo_future.result().to_dict('records')

    context = {
        'dispo_query': dispo_query,
        'subdispo': subdispo_query,
        'data': df_get_data,
        'searchdata': getdata,
        'fdate': firstdate,
        'ldate': lastdate,
        'dy_column_name': dy_column_name,
        'downloadlink': downloadpath
    }

    return render(request, 'reports.html', context)

##################################Modified Reports View##################################################################

########################Search view with modifications in Raw SQL#######################################################

def search(request):
    user = request.session.get('opoid')
    
    if user is None:
        return redirect('/')
    
    get_opoid_data = request.POST.get('searchdata')
    startdate = request.POST.get('startdata')
    enddate = request.POST.get('enddata')
    
    # Convert date strings to date objects if needed
    if startdate:
        startdate = datetime.strptime(startdate, '%Y-%m-%d').date()
    if enddate:
        enddate = datetime.strptime(enddate, '%Y-%m-%d').date()

    # Initialize context
    context = {'data': [], 'filter_count': 0, 'startdate': startdate, 'enddate': enddate}

    if get_opoid_data:
        try:
            with connection().cursor() as cursor:
                # Prepare SQL query based on the condition
                if 'OPO' in get_opoid_data:
                    sql = """
                        SELECT * FROM calltrans
                        WHERE opoid = %s
                        AND calldate BETWEEN %s AND %s
                    """
                    params = [get_opoid_data, startdate, enddate]
                else:
                    sql = """
                        SELECT * FROM calltrans
                        WHERE connid = %s
                        AND calldate BETWEEN %s AND %s
                    """
                    params = [get_opoid_data, startdate, enddate]

                # Execute the SQL query
                cursor.execute(sql, params)
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()

                # Convert the result to a list of dictionaries
                data = [dict(zip(columns, row)) for row in rows]
                context['data'] = data
                context['filter_count'] = len(data)
                
        except Exception as e:
            print(f"Error: {e}")
    
    return render(request, 'search.html', context)
########################Search view with modifications in Raw SQL#######################################################

#new function added by junaid 30 Apr 2024
def join_chat_view(chat_array):
	chat_view = []
	for i, chat in enumerate(chat_array):
		if i == 0:
			chat_view.append({"speaker": chat["speaker"], "words": [chat["word"]]})
 
		elif chat_view[-1]["speaker"] == chat["speaker"]:
			chat_view[-1]["words"].append(chat["word"])
		else:
			chat_view.append({"speaker": chat["speaker"], "words": [chat["word"]]}) 
	return chat_view
#new function added by junaid 30 Apr 2024

def join_chat_view_orig(chat_array):
	chat_view = []
	for i, chat in enumerate(chat_array):
		
		if i == 0:
			chat_view.append({"speaker": chat["speaker"], "words": [chat["word"]]})

		elif chat_view[-1]["speaker"] == chat["speaker"]:
			chat_view[-1]["words"].append(chat["word"])
		else:
			chat_view.append({"speaker": chat["speaker"], "words": [chat["word"]]}) 
	return chat_view

def replace_apostrophe(text):
    pattern = r'\b(\w+)"\b'
    replaced_text = re.sub(pattern, r"\1", text)
    return replaced_text

# code added by junaid 30 Apr 2024
def data_formatter(data):
     # Using regular expressions to extract individual words and their attributes
     pattern = r'Word\(word="([^"]+)", start=([^,]+), end=([^,]+), confidence=([^,]+), punctuated_word="([^"]+)", speaker=([^,]+), speaker_confidence=([^,]+), sentiment=([^,]+), sentiment_score=([^,]+)\)'

     word_list = re.findall(pattern, data)

     data = [Word(*word_attrs) for word_attrs in word_list]

     converted = []
     for word in data:

          if word.__dict__['speaker'] is None :
               del word.__dict__['speaker']
          
          if word.__dict__['speaker_confidence'] is None :
               del word.__dict__['speaker_confidence']
          
          if word.__dict__['sentiment'] is None :
               del word.__dict__['sentiment']
          
          if word.__dict__['sentiment_score'] is None :
               del word.__dict__['sentiment_score']

          converted.append(word.__dict__)

     return converted
# code added by junaid 30 Apr 2024

#######################################result_data function with optimized MySQL queries############################### 
def result_data(request):
    conn = connection()
    connid = request.POST.get('search_tearm')
    #print(connid)
    data = pd.read_sql(f"select *, cast(positivescore as decimal(4,2)) as positive_score, cast(negativescore  as decimal(4,2)) as negative_score, cast(positivescore as decimal(4,2)) as neutral_score from calltrans WHERE connid = '{connid}';",conn)
    fulltrans = data['fulltranscript'][0]
    # print(fulltrans)
    calldate = data['calldate'][0]
    # print(calldate)
    #print(data)
    fulltranslist = fulltrans.split(" ")
    dt = data['wordssummary'][0]
    dt1 = replace_apostrophe(dt)
    converted_data = data_formatter(dt1)
    #mydata=np.array(converted_data)
    chatdata = join_chat_view(converted_data)
    filepath_str = data['filepath'][0]
    #print(filepath_str[filepath_str.rfind('call_'):])
    date_folder_str = str(calldate)
    filename_str = str(data['filepath'][0])
    
    
    # to play audio if old path or new path after july new path before old path  Added By Junaid 16 july 2024
    if calldate >= datetime(2024, 7, 1).date():
        new_audio_file = "/icici/"+str(calldate)+"/"+str(filepath_str[filepath_str.rfind('call_'):])
    
    else:
        new_audio_file = "/icici_old/ICICI_CARD/ICICI_CARD/"+str(calldate)+"/"+str(filepath_str[filepath_str.rfind('call_'):])

    try:
        with open(os.path.join(new_audio_file), "rb") as audio_file:
            encoded_audio = base64.b64encode(audio_file.read())
            #print(encoded_audio)
    except Exception as e:

        print("audio not found :", e)
        encoded_audio = None

    negative_words = ["good", "evening", "dominos", "place", "problem", "receive", "but","complaint","worry","ok","order","बहुत","कैसे","address","no","नहीं","but"];
    common_word = set(negative_words).intersection(fulltranslist)
    wd = str(common_word).replace("'",'')
    
    transcriptdata = data['fulltranscript'][0]
    print("+++++++")
    print("+++++++")
    sizes,label,unique,wordcldtxt = wordtree(connid)
    

    wdsql = pd.read_sql(f"SELECT IF(Word_Occurrence IS NULL or Word_Occurrence = '', 'N/A', Word_Occurrence) as Word_Occurrence  FROM voiceanalytics.WordFinder where connid='{connid}'",conn)
    #word_occurrence = wdsql.to_dict('records')
    word_occurrence_list = wdsql['Word_Occurrence'].to_list()
    word_occurrence = word_occurrence_list[0]
    print(word_occurrence)
    main_words = ["Word", "Amount", "Bounce", "Branch", "Call Back", "Cash", "CIBIL", "Date", "Extra", "Fund Issue", "Impact", "Late", "Link", "Meeting", "Mode", "NET Banking", "On Call", "Purpose", "Record", "Recording", "Time", "Waiver", "Alternative Number", "Charges", "Expired", "Interest", "Minimum", "Settle", "Settlement", "Wrong Number"]

    # Parse word occurrences
    if  word_occurrence=='N/A':
        word_occurrence="No Data found:1,Missing:2,Not present:3,Nonexistent:4,Lacking:5"
        occurrences = {word.strip(): int(count) for word, count in (item.split(':') for item in word_occurrence.split(','))}

    else:
        occurrences = {word.strip(): int(count) for word, count in (item.split(':') for item in word_occurrence.split(','))}

    # Generate word cloud
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(occurrences)

    # Save the word cloud as an image and encode in base64
    imgs = wordcloud.to_image()
    buffer = io.BytesIO()
    imgs.save(buffer, 'png')
    img = base64.b64encode(buffer.getvalue())

    # quality attribute
    qty_dt = """SELECT (SUM(CASE WHEN t1.Opening = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question1,
            (SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question2,
            (SUM(CASE WHEN t1.Verification = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question3,
            (SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question4,
            (SUM(CASE WHEN t1.RPC = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question5,
            (SUM(CASE WHEN t1.Assertiveness_Confident = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question6,
            (SUM(CASE WHEN t1.Enthu_Energy = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question7,
            (SUM(CASE WHEN t1.Professionalism_Casual = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question8,
            (SUM(CASE WHEN t1.Speech_Clarity_ClearExplanation = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question9,
            (SUM(CASE WHEN t1.Pace_Customer_Language = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question10,
            (SUM(CASE WHEN t1.Personalization = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question11,
            (SUM(CASE WHEN t1.Active_Listening_No_Repetition = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question12,
            (SUM(CASE WHEN t1.Dead_Air = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question13,
            (SUM(CASE WHEN t1.Hold_Protocol = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question14,
            (SUM(CASE WHEN t1.Negotiation_Skils = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question15,
            (SUM(CASE WHEN t1.Urgency_Creation = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question16,
            (SUM(CASE WHEN t1.Objection_Handling_Rebuttals = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question17,
            (SUM(CASE WHEN t1.Due_Date_communication = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question18,
            (SUM(CASE WHEN t1.Summarization = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question19,
            (SUM(CASE WHEN t1.Appropriate_closing = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question20,
            (SUM(CASE WHEN t1.Complete_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question21,
            (SUM(CASE WHEN t1.Correct_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question22,
            (SUM(CASE WHEN t1.PTP_Detail_FPTP = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question23,
            (SUM(CASE WHEN t1.Script_Adherence = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question24,
            (SUM(CASE WHEN t1.Proactive_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question25,
            (SUM(CASE WHEN t1.Data_Capturing_Remarks = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question26,
            (SUM(CASE WHEN t1.Disclaimer = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS question27, score
            FROM VAmodel_db.test_ai AS t1 join calltrans c on t1.connid = c.connid where"""
    quality_attr = pd.read_sql(f"select * from VAmodel_db.test_ai where connid='{connid}' limit 1",conn)
    quality_attr = quality_attr.to_dict('records')
    #print(quality_attr)
    conn.close()
    
    context = {'data':data,'msg':chatdata,'negativeword':wd[1:-1],'transcript':transcriptdata,'audiodt':str(encoded_audio)[2:-1],"wordcloud":str(img)[2:-3],'attribut_val':quality_attr}
    return render(request,'resultofdata.html', context)
#######################################result_data function with optimized MySQL queries###############################

def user_logout(request):
	logout(request)
	return redirect('/')

def formdata(request):
	if request.method == "POST":
		form = AgentDataForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
	else:
		context = {'data':AgentDataForm()}
		return render(request,'form.html', context)

@csrf_exempt
def cal_score(request):
	score = 89
	return HttpResponse(score)

## ==============================Working positive_call function =========================================================

def positive_call(request):
    conn = connection()
    
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')
    
    if fromdate:
        query = """
            SELECT calldate,opoid,connid,processname,calltime, cast(positivescore as DECIMAL(18,2)) AS positiveval
            FROM calltrans
            WHERE calldate BETWEEN %s AND %s
            ORDER BY calldate DESC, positivescore DESC
            LIMIT 50
        """
        pos_call = pd.read_sql(query, conn, params=[fromdate, todate])
    else:
        query = """
            SELECT calldate,opoid,connid,processname,calltime, cast(positivescore as DECIMAL(18,2)) AS positiveval
            FROM calltrans
            WHERE calldate >= DATE_SUB(NOW(), INTERVAL 7 DAY)
            ORDER BY calldate DESC, positivescore DESC
            LIMIT 50
        """
        pos_call = pd.read_sql(query, conn)

    # Extract the time part from 'calltime'
    pos_call['calltime'] = pos_call['calltime'].astype(str).str.split().str[-1]
    
    conn.close()
    
    context = {
        'data': pos_call.to_dict('records'),
        'fromdate': fromdate,
        'todate': todate
    }
    
    return render(request, 'positivecall.html', context)

## ==============================Working positive_call function =========================================================


## ==============================Working onclick_graph function =========================================================

def onclick_graph(request):
    conn = connection()
    label = request.GET.get('label', '').replace(" ", "")
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')

    # Print debug information
    print('Label:', label)
    print('From Date:', fromdate)
    print('Type(From Date):', type(fromdate))
    print('To Date:', todate)
    print('Type(To Date):', type(todate))

    # Construct the SQL query with parameters
    query = """
    SELECT c.*, w.Word_Occurrence
    FROM voiceanalytics.WordFinder w
    JOIN calltrans c ON w.connid = c.connid
    WHERE REPLACE(w.Word_Occurrence, ' ', '') = %s
    """
    params = [label]

    if fromdate and todate:  # New condition added by Junaid 17 May 2024
        query += " AND DATE(w.calldate) BETWEEN %s AND %s"
        params.extend([fromdate, todate])
    else:
        query += " AND DATE(w.calldate) >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)"

    # Execute the query
    pos_call = pd.read_sql(query, conn, params=params)
    pos_call['calltime'] = pos_call['calltime'].astype('str').str.split().str[-1]

    conn.close()

    context = {
        'data': pos_call.to_dict('records'),
        'label': label,
        'fromdate': fromdate,
        'todate': todate
    }
    return render(request, 'onclick_graph.html', context)
## ==============================Working onclick_graph function =========================================================

## ==============================Working attribute_view function =========================================================

def attribute_view(request):
    conn = connection()
    label = request.GET.get('label', '').replace(" ", "_")
    
    # Mapping labels to column names
    label_mapping = {
        'Disposition': 'Disposition1',
        'DIY_Adherence': 'Proactive_Information',
        'PTP_Detail_FPTP': 'PTP_Detail_FPTP',
        'Script_Adherence': 'Script_Adherence'
    }
    label = label_mapping.get(label, label)  # Default to label if not found

    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')

    # SQL query with placeholder
    if fromdate and todate:
        query = f"""
            SELECT c.connid, c.calldate, c.calltime, c.processname, c.opoid, t.{label}
            FROM voiceanalytics.calltrans c
            JOIN VAmodel_db.test_ai t ON t.connid = c.connid
            WHERE DATE(c.calldate) BETWEEN %s AND %s AND t.{label} = 'Not Met'
        """
        params = (fromdate, todate)
    else:
        query = f"""
            SELECT c.connid, c.calldate, c.calltime, c.processname, c.opoid, t.{label}
            FROM voiceanalytics.calltrans c
            JOIN VAmodel_db.test_ai t ON t.connid = c.connid
            WHERE DATE(c.calldate) BETWEEN DATE_SUB(CURDATE(), INTERVAL %s DAY) AND CURDATE()
            AND t.{label} = 'Not Met'
        """
        params = (7,)  # Default to last 7 days

    # Execute query
    try:
        pos_call = pd.read_sql(query, conn, params=params)
    except Exception as e:
        print(f"SQL execution error: {e}")
        conn.close()
        return render(request, 'error.html', {'message': 'Error executing the SQL query.'})
    
    pos_call['calltime'] = pos_call['calltime'].astype(str).str.split().str[-1]
    conn.close()

    # Pagination
    page = request.GET.get('page', 1)
    items_per_page = 50
    paginator = Paginator(pos_call.to_dict('records'), items_per_page)

    try:
        pos_call_page = paginator.page(page)
    except PageNotAnInteger:
        pos_call_page = paginator.page(1)
    except EmptyPage:
        pos_call_page = paginator.page(paginator.num_pages)

    # Debugging output
    print(f"Requested page: {page}")
    print(f"Total pages: {paginator.num_pages}")
    
    context = {'data': pos_call_page, 'label': label, 'fromdate': fromdate, 'todate': todate}
    
    return render(request, 'attribute_view.html', context)

## ==============================Working attribute_view function =========================================================

## ==============================Working negative_call function =========================================================

def negative_call(request):
    conn = connection()
    
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')
    
    if fromdate:
        query = """
            SELECT calldate,opoid,processname,connid,calltime, cast(negativescore as DECIMAL(18,2)) AS negativeval
            FROM calltrans
            WHERE calldate BETWEEN %s AND %s
            ORDER BY calldate DESC, negativescore DESC
            LIMIT 50
        """
        neg_call = pd.read_sql(query, conn, params=[fromdate, todate])
    else:
        query = """
            SELECT calldate,opoid,processname,connid,calltime, cast(negativescore as DECIMAL(18,2)) AS negativeval
            FROM calltrans
            WHERE calldate >= DATE_SUB(NOW(), INTERVAL 7 DAY)
            ORDER BY calldate DESC, negativescore DESC
            LIMIT 50
        """
        neg_call = pd.read_sql(query, conn)
    
    # Extract the time part from 'calltime'
    neg_call['calltime'] = neg_call['calltime'].astype(str).str.split().str[-1]
    
    conn.close()
    
    context = {
        'data': neg_call.to_dict('records'),
        'fromdate': fromdate,
        'todate': todate
    }
    
    return render(request, 'negativecall.html', context)

## ==============================Working negative_call function =========================================================

## ==============================Working neutral_call function =========================================================

def neutral_call(request):
    conn = connection()
    
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')
    
    if fromdate:
        query = """
            SELECT calldate,opoid,processname,connid,calltime, cast(neutralscore as DECIMAL(18,2)) AS neutralval
            FROM calltrans
            WHERE calldate BETWEEN %s AND %s
            ORDER BY calldate DESC, neutralscore DESC
            LIMIT 50
        """
        neu_call = pd.read_sql(query, conn, params=[fromdate, todate])
    else:
        query = """
            SELECT calldate,opoid,processname,connid,calltime, cast(neutralscore as DECIMAL(18,2)) AS neutralval
            FROM calltrans
            WHERE calldate >= DATE_SUB(NOW(), INTERVAL 7 DAY)
            ORDER BY calldate DESC, neutralscore DESC
            LIMIT 50
        """
        neu_call = pd.read_sql(query, conn)
    
    # Extract the time part from 'calltime'
    neu_call['calltime'] = neu_call['calltime'].astype(str).str.split().str[-1]
    
    conn.close()
    
    context = {
        'data': neu_call.to_dict('records'),
        'fromdate': fromdate,
        'todate': todate
    }
    
    return render(request, 'neutralcall.html', context)

## ==============================Working neutral_call function =========================================================

##=================================Working  getsubdisp function===========================================================

def getsubdisp(request):
	selectedDisp = request.GET.get('d')
	conn = connection()
	df_get_data = pd.read_sql(f"""select distinct subdisposition from calltrans where year(calldate)='2024' and disposition='{selectedDisp}';""",conn)
	df_get_data = df_get_data.to_dict('records')
	return HttpResponse(json.dumps({'data':df_get_data}), content_type="application/json")

##=================================Working  getsubdisp function===========================================================

def select_keyword(request):
	conn = connection()
	df_get_data = pd.read_sql(f"""select KeywordID,Keyword from Keywords;""",conn)
	df_get_data = df_get_data.to_dict('records')
	context = {'data':df_get_data}
	return render(request,'keywords.html',context)

def select_keyword_edit(request):
	conn = connection()
	df_get_data = pd.read_sql(f"""select KeywordID,Keyword from Keywords;""",conn)
	df_get_data = df_get_data.to_dict('records')
	context = {'data':df_get_data,'ed':'1'}
	return render(request,'keywords.html',context)

def select_keyword_save(request):
	conn = connection()
	KeywordID = request.POST.get('KeywordID')
	Keyword = request.POST.get('Keyword')
	cursor = conn.cursor()
	cursor.execute(f"""update Keywords set Keyword='{Keyword}' where  KeywordID='{KeywordID}';""")
	conn.commit()
	cursor.close()   # Close the cursor and connection when done
	conn.close()
	return redirect ('/select_keyword')

def select_keyword_add(request):
	conn = connection()
	 
	Keyword = request.POST.get('Keyword')
	cursor = conn.cursor()
	cursor.execute(f"""insert into Keywords (Keyword) values ('{Keyword}');""")
	conn.commit()
	cursor.close()   # Close the cursor and connection when done
	conn.close()
	return redirect ('/select_keyword')

def select_keyword_delete(request):
	conn = connection()
	KeywordID = request.POST.get('KeywordID')
	cursor = conn.cursor()
	print("delete from Keywords where  KeywordID='{KeywordID}';")
	cursor.execute(f"""delete from Keywords where KeywordID='{KeywordID}';""")
	conn.commit()
	cursor.close()    # Close the cursor and connection when done
	conn.close() 
	return redirect ('/select_keyword_delete')

##############################Working agent_search function  ###########################################################

def fetch_query(query):
    # Function to execute a query and return the results
    with connection().cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def agent_search(request):
    # SQL queries to get unique dispositions and subdispositions
    query_dispositions = """
        SELECT DISTINCT disposition
        FROM calltrans
        WHERE YEAR(calldate) >= 2024
    """   
    
    query_subdispositions = """
        SELECT DISTINCT subdisposition
        FROM calltrans
        WHERE YEAR(calldate) >= 2024
    """
    
    # Use ThreadPoolExecutor to run queries in parallel
    with ThreadPoolExecutor() as executor:
        # Submit both queries to be executed concurrently
        future_dispo = executor.submit(fetch_query, query_dispositions)
        future_subdispo = executor.submit(fetch_query, query_subdispositions)
        
        # Wait for the results
        dispo_query = future_dispo.result()
        subdispo_query = future_subdispo.result()

    # Process the results into dictionaries
    dispo_query = [{'disposition': row[0]} for row in dispo_query]
    subdispo_query = [{'subdisposition': row[0]} for row in subdispo_query]
    
    # Prepare context for rendering
    context = {
        'data': dispo_query,
        'subdispo': subdispo_query
    }
    
    return render(request, 'agent_search.html', context)

##############################Working agent_search function  ###########################################################

################################Working agent_view function#############################################################

def agent_view(request):
    opoid = request.POST.get("opoid")
    disposition_type = request.POST.get("disposition")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")
    print(opoid, disposition_type, fromdate, todate)
    
    def fetch_data(query):
        with connection().cursor() as cursor:
            cursor.execute(query)
            return pd.DataFrame(cursor.fetchall(), columns=[col[0] for col in cursor.description])
    
    # Queries with date range
    queries_with_dates = {
        "agent_senti_data": f"SELECT COUNT(id) AS call_evaluted, FORMAT(AVG(positivescore),2) AS positive, FORMAT(AVG(negativescore),2) AS negative, FORMAT(AVG(neutralscore),2) as neutral, FORMAT(AVG(qualityscore),2) as quality_score FROM calltrans WHERE opoid = '{opoid}' AND disposition = '{disposition_type}' AND calldate BETWEEN '{fromdate}' AND '{todate}'",
        "agent_call_7_days": f"SELECT DATE_FORMAT(calldate, '%Y-%m-%d') AS lastdate, COUNT(calldate) AS total_call FROM calltrans WHERE opoid ='{opoid}' AND disposition ='{disposition_type}' AND calldate BETWEEN '{fromdate}' AND '{todate}' GROUP BY calldate",
        "quality_attr": f"""
            SELECT CAST(((SUM(CASE WHEN t1.Opening = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question1,
            CAST(((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question2,
            CAST(((SUM(CASE WHEN t1.Verification = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question3,
            CAST(((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question4,
            CAST(((SUM(CASE WHEN t1.RPC = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question5,
            CAST(((SUM(CASE WHEN t1.Dead_Air = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question13,
            CAST(((SUM(CASE WHEN t1.Hold_Protocol = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question14,
            CAST(((SUM(CASE WHEN t1.Due_Date_communication = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question18,
            CAST(((SUM(CASE WHEN t1.Appropriate_closing = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question20,
            CAST(((SUM(CASE WHEN t1.PTP_Detail_FPTP = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question23,
            CAST(((SUM(CASE WHEN t1.Script_Adherence = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question24,
            CAST(((SUM(CASE WHEN t1.Proactive_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question25,
            CAST(((SUM(CASE WHEN t1.Disclaimer = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question27
            FROM VAmodel_db.test_ai AS t1
            JOIN calltrans c ON t1.connid = c.connid
            WHERE c.opoid = '{opoid}' AND c.disposition = '{disposition_type}' AND DATE(c.calldate) BETWEEN '{fromdate}' AND '{todate}'
        """,
        "quality_score": f"SELECT ROUND(AVG(score),2) AS qualityscore FROM VAmodel_db.test_ai WHERE connid IN (SELECT connid FROM calltrans WHERE disposition = '{disposition_type}' AND DATE(calldate) BETWEEN '{fromdate}' AND '{todate}')",
        "dispo_query": f"SELECT disposition FROM calltrans WHERE YEAR(calldate) >= '2024' GROUP BY disposition",
        "subdispo_query": f"SELECT subdisposition FROM calltrans WHERE YEAR(calldate) >= '2024' GROUP BY subdisposition",
    }

    # Queries without date range
    queries_without_dates = {
        "agent_senti_data": f"SELECT COUNT(id) AS call_evaluted, FORMAT(AVG(positivescore),2) AS positive, FORMAT(AVG(negativescore),2) AS negative, FORMAT(AVG(neutralscore),2) as neutral, FORMAT(AVG(qualityscore),2) as quality_score FROM calltrans where opoid = '{opoid}' and calldate >= DATE_SUB(NOW(), INTERVAL 8 DAY)",
        "agent_call_7_days": f"SELECT DATE_FORMAT(calldate, '%Y-%m-%d') AS lastdate, COUNT(calldate) AS total_call FROM calltrans WHERE opoid ='{opoid}' and calldate >= DATE_SUB(NOW(), INTERVAL 8 DAY) GROUP BY calldate",
        "quality_attr": f"""
        SELECT FORMAT(((SUM(CASE WHEN t1.Opening = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question1,
 		FORMAT(((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question2,
		FORMAT(((SUM(CASE WHEN t1.Verification = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question3,
		FORMAT(((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question4,
 		FORMAT(((SUM(CASE WHEN t1.RPC = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question5,
 		FORMAT(((SUM(CASE WHEN t1.Assertiveness_Confident = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question6,
 		FORMAT(((SUM(CASE WHEN t1.Enthu_Energy = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question7,
		FORMAT(((SUM(CASE WHEN t1.Professionalism_Casual = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question8,
 		FORMAT(((SUM(CASE WHEN t1.Speech_Clarity_ClearExplanation = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question9,
 		FORMAT(((SUM(CASE WHEN t1.Pace_Customer_Language = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question10,
 		FORMAT(((SUM(CASE WHEN t1.Personalization = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question11, 		FORMAT(((SUM(CASE WHEN t1.Active_Listening_No_Repetition = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question12,
 		FORMAT(((SUM(CASE WHEN t1.Dead_Air = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question13,
 		FORMAT(((SUM(CASE WHEN t1.Hold_Protocol = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question14,
		FORMAT(((SUM(CASE WHEN t1.Negotiation_Skils = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question15,
		FORMAT(((SUM(CASE WHEN t1.Urgency_Creation = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question16,
 		FORMAT(((SUM(CASE WHEN t1.Objection_Handling_Rebuttals = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question17,
 		FORMAT(((SUM(CASE WHEN t1.Due_Date_communication = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question18,
 		FORMAT(((SUM(CASE WHEN t1.Summarization = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question19,
 		FORMAT(((SUM(CASE WHEN t1.Appropriate_closing = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question20,
 		FORMAT(((SUM(CASE WHEN t1.Complete_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question21,
 		FORMAT(((SUM(CASE WHEN t1.Correct_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question22,
 		FORMAT(((SUM(CASE WHEN t1.PTP_Detail_FPTP = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question23,
 		FORMAT(((SUM(CASE WHEN t1.Script_Adherence = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question24,
 		FORMAT(((SUM(CASE WHEN t1.Proactive_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question25,
		FORMAT(((SUM(CASE WHEN t1.Data_Capturing_Remarks = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question26,
 		FORMAT(((SUM(CASE WHEN t1.Disclaimer = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100),2) AS question27
            FROM VAmodel_db.test_ai AS t1
            JOIN calltrans c ON t1.connid = c.connid
            WHERE c.opoid = '{opoid}' AND c.disposition = '{disposition_type}'
        """,
        "quality_score": f"SELECT ROUND(AVG(score),2) as qualityscore from VAmodel_db.test_ai WHERE connid in(select connid from calltrans where opoid='{opoid}' and disposition='{disposition_type}' and  Date(calldate) BETWEEN '{fromdate}' and '{todate}');",
        "dispo_query": f"SELECT disposition FROM calltrans WHERE YEAR(calldate) >= '2024' GROUP BY disposition",
        "subdispo_query": f"SELECT subdisposition FROM calltrans WHERE YEAR(calldate) >= '2024' GROUP BY subdisposition",
    }

    # Select queries based on the presence of fromdate and todate
    queries = queries_with_dates if fromdate and todate else queries_without_dates

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_data, query): key for key, query in queries.items()}
        results = {}
        for future in futures:
            key = futures[future]
            results[key] = future.result()

    agent_senti_data = results['agent_senti_data'].to_dict('records')[0]
    agent_call_7_days = results['agent_call_7_days'].to_dict('records')
    quality_attr = results['quality_attr'].to_dict('records')
    qualityScore = results['quality_score'].to_dict('records')[0]['qualityscore']
    dispo_query = results['dispo_query'].to_dict('records')
    subdispo_query = results['subdispo_query'].to_dict('records')

    context = {
        'data': dispo_query,
        'subdispo_query': subdispo_query,
        'sentiment_data': agent_senti_data,
        'opoid': opoid,
        'agent_call_7_days': agent_call_7_days,
        'attribut_val': quality_attr,
        'fromdate': fromdate,
        'todate': todate,
        'qualityScore': qualityScore
    }

    return render(request, 'agent_search.html', context)

################################Working agent_view function#############################################################

#####################Disposition_analysis using Multithreading#########################################################
def fetch_disposition_query():
    with connection().cursor() as cursor:
        cursor.execute(
            "SELECT disposition FROM calltrans WHERE YEAR(calldate) >= 2024 GROUP BY disposition"
        )
        return cursor.fetchall()

def fetch_subdisposition_query():
    with connection().cursor() as cursor:
        cursor.execute(
            "SELECT subdisposition FROM calltrans WHERE YEAR(calldate) >= 2024 GROUP BY subdisposition"
        )
        return cursor.fetchall()

def disposition_analysis(request):
    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        dispo_future = executor.submit(fetch_disposition_query)
        subdispo_future = executor.submit(fetch_subdisposition_query)

        # Wait for results
        dispo_query = dispo_future.result()
        subdispo_query = subdispo_future.result()

    # Convert results to dict
    dispo_query = [dict(disposition=row[0]) for row in dispo_query]
    subdispo_query = [dict(subdisposition=row[0]) for row in subdispo_query]

    context = {'data': dispo_query, 'subdispo': subdispo_query}
    
    return render(request, 'disposition_analysis.html', context)

#####################Disposition_analysis using Multithreading#########################################################

#####################Working code for get_disposition_data##############################################################

def fetch_data(query, params=None):
    conn = connection()
    if params:
        data = pd.read_sql(query, conn, params=params)
    else:
        data = pd.read_sql(query, conn)
    conn.close()
    return data

def get_disposition_data(request):
    start_time = time.time()
    disposition_type = request.POST.get("disposition")
    disposition_name = request.POST.get("disposition_name")
    start_date = request.POST.get("fromdate")
    end_date = request.POST.get("todate")
    
    print(disposition_type, start_date, end_date)

    with ThreadPoolExecutor() as executor:
        sentiment_query = """
            SELECT COUNT(id) AS call_evaluted, 
                   FORMAT(AVG(positivescore), 2) AS positive,
                   FORMAT(AVG(negativescore), 2) AS negative,
                   FORMAT(AVG(neutralscore), 2) AS neutral,
                   FORMAT(AVG(qualityscore), 2) AS quality_score
            FROM calltrans
            WHERE disposition = %s AND calldate BETWEEN %s AND %s
        """
        chart_query = """
        SELECT DATE(calldate) AS lastdate,
        COUNT(calldate) AS total_call
        FROM calltrans
        WHERE disposition = %s AND calldate BETWEEN %s AND %s
        GROUP BY lastdate
        """
        qty_dt = """
        SELECT CAST(((SUM(CASE WHEN t1.Opening = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question1,
        CAST(((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question2,
		CAST(((SUM(CASE WHEN t1.Verification = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question3,
		CAST(((SUM(CASE WHEN t1.Self_Company_Introduction = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question4,
		CAST(((SUM(CASE WHEN t1.RPC = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question5,
		CAST(((SUM(CASE WHEN t1.Assertiveness_Confident = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question6,
		CAST(((SUM(CASE WHEN t1.Enthu_Energy = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question7,
		CAST(((SUM(CASE WHEN t1.Professionalism_Casual = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question8,
		CAST(((SUM(CASE WHEN t1.Speech_Clarity_ClearExplanation = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question9,
		CAST(((SUM(CASE WHEN t1.Pace_Customer_Language = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question10,
		CAST(((SUM(CASE WHEN t1.Personalization = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question11,
		CAST(((SUM(CASE WHEN t1.Active_Listening_No_Repetition = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question12,
		CAST(((SUM(CASE WHEN t1.Dead_Air = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question13,
		CAST(((SUM(CASE WHEN t1.Hold_Protocol = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question14,
		CAST(((SUM(CASE WHEN t1.Negotiation_Skils = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question15,
		CAST(((SUM(CASE WHEN t1.Urgency_Creation = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question16,
		CAST(((SUM(CASE WHEN t1.Objection_Handling_Rebuttals = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question17,
		CAST(((SUM(CASE WHEN t1.Due_Date_communication = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question18,
		CAST(((SUM(CASE WHEN t1.Summarization = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question19,
		CAST(((SUM(CASE WHEN t1.Appropriate_closing = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question20,
		CAST(((SUM(CASE WHEN t1.Complete_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question21,
		CAST(((SUM(CASE WHEN t1.Correct_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question22,
		CAST(((SUM(CASE WHEN t1.PTP_Detail_FPTP = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question23,
		CAST(((SUM(CASE WHEN t1.Script_Adherence = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question24,
		CAST(((SUM(CASE WHEN t1.Proactive_Information = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question25,
		CAST(((SUM(CASE WHEN t1.Data_Capturing_Remarks = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question26,
		CAST(((SUM(CASE WHEN t1.Disclaimer = 'MET' THEN 1 ELSE 0 END) / COUNT(*)) * 100) as decimal(18,2)) AS question27
                   
            FROM VAmodel_db.test_ai AS t1
            JOIN calltrans c ON t1.connid = c.connid
            WHERE c.disposition = %s AND DATE(c.calldate) BETWEEN %s AND %s
        """
        quality_score_query = """
            SELECT ROUND(AVG(score), 2) AS qualityscore
            FROM VAmodel_db.test_ai
            WHERE connid IN (SELECT connid FROM calltrans WHERE disposition = %s AND DATE(calldate) BETWEEN %s AND %s)
        """
        dispo_query = "SELECT DISTINCT disposition FROM calltrans WHERE YEAR(calldate) >= 2024"
        subdispo_query = "SELECT DISTINCT subdisposition FROM calltrans WHERE YEAR(calldate) >= 2024"

        results = {
            'disposition_senti_data': executor.submit(fetch_data, sentiment_query, (disposition_type, start_date, end_date)),
            'disp_7_day_chart': executor.submit(fetch_data, chart_query, (disposition_type, start_date, end_date)),
            'quality_attr': executor.submit(fetch_data, qty_dt, (disposition_type, start_date, end_date)),
            'qualityScore': executor.submit(fetch_data, quality_score_query, (disposition_type, start_date, end_date)),
            'dispo_data': executor.submit(fetch_data, dispo_query),
            'subdispo_data': executor.submit(fetch_data, subdispo_query)
        }

    disposition_senti_data = results['disposition_senti_data'].result().to_dict('records')[0]
    disp_7_day_chart = results['disp_7_day_chart'].result().to_dict('records')
    quality_attr = results['quality_attr'].result().to_dict('records')
    qualityScore = results['qualityScore'].result().to_dict('records')
    dispo_data = results['dispo_data'].result().to_dict('records')
    subdispo_data = results['subdispo_data'].result().to_dict('records')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to execute get_disposition_data: {elapsed_time:.4f} seconds")

    context = {
        'data': dispo_data,
        'subdispo': subdispo_data,
        'disposition_senti_data': disposition_senti_data,
        'disp_7_day_chart': disp_7_day_chart,
        'disposition_name': disposition_name,
        'attribut_val': quality_attr,
        'qualityScore': qualityScore,
        'start_date': start_date,
        'end_date': end_date
    }

    return render(request, 'disposition_analysis.html', context)

#####################Working code for get_disposition_data##############################################################

##########################New view users added to view the number of users using the app ##########################

def users(request):
    if request.method == "GET":
        query = "SELECT id, name, opoid, role, created_at FROM users;"
        with connection().cursor() as cursor:
            cursor.execute(query)
            user_list = cursor.fetchall()  # Fetch all rows

        # Prepare user data for the template
        users_data = []
        for user in user_list:
            users_data.append({
                'id': user[0],
                'name': user[1],
                'opoid': user[2],
                'role': user[3],
                'created_at': user[4],
            })

        return render(request, 'users.html', {'users': users_data})

##########################New view users added to view the number of users using the app ##########################
