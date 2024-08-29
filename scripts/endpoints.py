from scripts.dbConn import *
from jinja2 import Template
from flask import render_template, url_for

def friendsPageBuilder(id):
    friends = pullFriends(id)
    print(friends)

    # with open('templates/friends.html.jinja') as f:
    #     tmpl = Template(f.read())
    return render_template('friends.html.jinja',
        variable = 'Friends',
        mainUserId = id,
        item_list = friends
    )

def messagePageBuilder(user1Id, user2Id):
    messages = pullAllMsgHistory(user1Id, user2Id)
    friend = pullUser(user2Id)
    print(messages)

    with open('templates/messages.html.jinja') as f:
        tmpl = Template(f.read())
    return tmpl.render(
        variable = 'Messages',
        senderId = user1Id,
        friend = [friend[0][0], friend[0][1]],
        postUrl = url_for('sendMessage', user1Id=user1Id, user2Id=user2Id),
        item_list = messages
    )