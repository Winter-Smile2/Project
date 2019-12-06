import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from message.models import Message
from tools.logging_check import logging_check
from topic.models import Topic


@logging_check('POST')
def message(request, topic_id):
    if request.method == 'POST':
        # 发表留言/回复
        json_str = request.body
        json_obj = json.loads(json_str)
        content = json_obj.get('content')
        parent_id = json_obj.get('parent_id', 0)
        # TODO 参数检查
        # 检查topic是否存在
        try:
            topic = Topic.objects.get(id=topic_id)
        except Exception as e:
            result = {'code': 40101, 'error': 'No Topic'}
            return JsonResponse(result)
        Message.objects.create(content=content,parent_message=parent_id, publisher=request.user, topic_id=topic_id)
        return JsonResponse({'code':200, 'data':{}})
    if request.method == 'GET':
        all_m = Message.objects.all()
        all_list = []
        for m in all_m:
            d = {}
            d['id'] = m.id
            d['content'] = m.content
            d['parent_message'] = m.parent_message
            d['publisher'] = m.publisher.username
            d['topic'] = m.topic.id
            all_list.append(d)
        return JsonResponse({'code':200,'data':all_list})