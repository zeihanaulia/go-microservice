import os
import json
import itertools

from flask import Blueprint, jsonify, request
from nameko.standalone.rpc import ClusterRpcProxy

news = Blueprint('news', __name__)
CONFIG_RPC = {'AMQP_URI': os.environ.get('QUEUE_HOST')}

@news.route('/<string:news_type>/<int:news_id>', methods=['GET'])
def get_single_news(news_type, news_id):
    """ Get single user details """
    try:
        response_object = rpc_get_news(news_type, news_id)
        return jsonify(response_object), 200
    except Exception as e:
        error_response(e, 500)

@news.route('/all/<int:num_page>/<int:limit>',methods=['GET'])
def get_all_news(num_page, limit):
    try:
        response_famous =  rpc_get_all_news('famous', num_page, limit)
        response_politics = rpc_get_all_news('politics', num_page, limit)
        response_sports = rpc_get_all_news('sports', num_page, limit)

        # summarizing the microservices response in just one
        all_news = itertools.chain(
            response_famous.get('news', [])
            response_politics.get('politics', [])
            response_sports.get('sports', [])
        )

        response_object = {
            'status': 'success',
            'news': list(all_news)
        }

        return jsonify(response_object)
    except Exception as e:
        return error_response(e, 500)