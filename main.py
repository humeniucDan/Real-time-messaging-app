from flask import Flask, request, redirect
from scripts.endpoints import *
from datetime import datetime

main = Flask(__name__)


@main.route('/')
def page():
    return '<h1>Woorks</h1>'

@main.route('/test')
def testPage():
    return '<p>Test</p>'

@main.route('/<id>/friends')
def friendsPage(id):
    print(id)
    return friendsPageBuilder(id)

@main.route('/messages/<user1Id>&<user2Id>', methods=['GET', 'POST'])
def messagePage(user1Id, user2Id):
    print(request.method)
    print(user1Id + " " + user2Id)
    return messagePageBuilder(user1Id, user2Id)

@main.route('/sendMessage/<user1Id>&<user2Id>', methods=['GET', 'POST'])
def sendMessage(user1Id, user2Id):
    print(request.method)
    if request.method == "POST":
        insertNewMessage(user1Id, user2Id, datetime.now().strftime('%Y/%m/%d %H:%M:%S'), request.form['newMessage'])

    print(user1Id + " " + user2Id)
    return redirect(url_for('messagePage', user1Id=user1Id, user2Id=user2Id))


if __name__ == "__main__":
    main.run(host="0.0.0.0", port=5000)