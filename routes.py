from flask import Blueprint,jsonify,request
main=Blueprint('main',__name__)
tasks=[]
@main.route('/task',methods=['get'])
def gettasks_():
    return jsonify (tasks)

@main.route('/tasks', methods=['get'])
def addtasks():
    data=request.get_json()
    tasks={"id":len(tasks)+1,"title":data.get("title")}
    tasks.append(tasks)
    return jsonify (tasks),201
