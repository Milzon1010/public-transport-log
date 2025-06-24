from app import app
from flask import render_template, request
from app.transport import get_schedule

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == "POST":
        start = request.form.get("start")
        end = request.form.get("end")
        # panggil get_schedule() atau fungsi lain untuk mendapatkan rute terbaik
        result = get_schedule(start, end)       
        # render hasil ke template
    return render_template('form.html', result=result)
  
      
