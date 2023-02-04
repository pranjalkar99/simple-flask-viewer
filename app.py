from flask import Flask,render_template,redirect, url_for,request
app = Flask(__name__)
import json
status="default"

f=open("new_batch_letera_3-2.json","r")
data=json.loads(f.read())

f.close()


#Just checking
##  ***************************Testing ****************************8
# pages = [
#     "<html><body><h1>Page 1</h1></body></html>",
#     "<html><body><h1>Page 2</h1></body></html>",
#     "<html><body><h1>Page 3</h1></body></html>"
# ]
@app.route('/')
def index_test():
    return "Go to /serve to get started..."

@app.route('/next_test')
def next_page(pages):
    current_page = int(request.args.get('current_page', 0))
    next_page = current_page + 1
    if next_page >= len(pages):
        next_page = 0
    return render_template('index_test.html', pages=pages, current_page=next_page)

#   
##########################end of testing ####################3333

@app.route("/serve")
def serve_html():
    ids = [obj["iden"] for obj in data]
    identifier={}
    for each in ids:
        identifier[each]={}
        identifier[each]['link']=url_for('page',id=each)
        identifier[each]['status']=status
    
    return render_template("index.html",ids=identifier)
    #return data[0]





# @app.route('/next_test')
# def next_page(pages):
#     current_page = int(request.args.get('current_page', 0))
#     next_page = current_page + 1
#     if next_page >= len(pages):
#         next_page = 0
#     return render_template('index_test.html', pages=pages, current_page=next_page)


current_page = 0

@app.route('/serve/<id>', methods=['GET', 'POST'])
def page(id):
    obj = next((obj for obj in data if obj["iden"] == id), None)
    if obj:
        pages=obj['html']
    else:
        return "Error: Object not found"
    if request.method=='POST':
        global current_page
        current_page = (current_page + 1) % len(pages)
        return render_template('index_test.html', pages=pages, current_page=current_page)

    else:
        return render_template("index_test.html",obj=obj,   pages=pages, current_page=0)
    

## @Rajdeep write js code to update the status after button is clicked on page.html so that next time when index is loaded, status of that is updated...
# def update_status(id):
#     console.log(id)
#     print(id)
#     status="success"