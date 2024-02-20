from win10toast import ToastNotifier
import requests
import schedule
import time 
import pytz
from datetime import datetime
import threading

def notify_fact():
    
	url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"

	headers = {
		"X-RapidAPI-Key": '<apikey>',
		"X-RapidAPI-Host": "trivia-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)

	question = response.json()[0]['question']
	answer = response.json()[0]['answer']
	toaster = ToastNotifier()
	toaster.show_toast("Question", question, duration=2)
	time.sleep(30)
	toaster.show_toast("Answer", answer, duration=2)
	

def run_continuously(interval=1):
    
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


schedule.every().day.at("10:30", "Europe/London").do(notify_fact)
stop_run_continuously = run_continuously()
	