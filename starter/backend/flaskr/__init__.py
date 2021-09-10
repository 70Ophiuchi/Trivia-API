#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, json, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from sqlalchemy.sql.functions import AnsiFunction

from sqlalchemy.sql.operators import json_getitem_op

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    paginated_questions = questions[start:end]
    return paginated_questions


def create_app(test_config=None):

  # create and configure the app

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,true')
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PUT,DELETE,PATCH,OPTIONS')

    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.order_by(Category.id).all()
        return jsonify({'categories': categories.categories})

  # GET request handler for questions
  # Included GET method in decorator because
  # its better to be explicit and not implicit

    @app.route('/questions', methods=['GET'])
    def get_questions():
        body = request.get_json()
        selection = Question.query.order_by(Question.id).all()
        questions = paginate(request, selection)

        if len(questions) < 1:
            abort(404)

        return jsonify({
            'questions': questions.questions,
            'total_questions': len(questions),
            'current_category': Question.category.filter_by(category=body.category),
            'categories': Question.category.all()
            })

    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        question = Question.query.filter(id=id).one_or_none()

        if not question is None:
            try:
              question.delete()
              return jsonify({
                "status_code": 200
              })
            except:
              abort(404)
        else:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()

        question = body.get('question', None)
        answer = body.get('answer', None)
        category = body.get('category', None)
        difficulty = body.get('difficulty', None)
        search = body.get('search', None)

        if not search is None:
            search_results = \
                Question.question.ilike('%{}%'.fomrat(search))
            return jsonify({'questions': search_results,
                           'total_questions': len(Question.query.all()),
                           'current_category': Question.category.filter_by(id=body.id).all()})
        else:
            new_question = Question(question=question, answer=answer,
                                    category=category,
                                    difficulty=difficulty)
            try:
              new_question.insert()
              return jsonify({"status_code": 200})
            except:
              abort(422)

    @app.route('/category/<int:id>/questions', methods=['GET'])
    def get_questions_by_category(id):
        filter = Question.query.filter_by(id=id)
        questions = \
            Question.query.filter_by(category=filter.category).all()
        return jsonify({'questions': questions.questions,
                       'total_questions': len(Question.query.all()),
                       'current_category': questions.category})

    @app.route('/quizzes', methods=['POST'])
    def play():
        randomID = random.randint(1, 10)
        body = request.get_json()
        filter = Question.query.filter_by(category=body.category)
        question = filter.filter_by(id=randomID).one_or_none()
        if question == None:
            abort(404)
        return jsonify({'question': question,
                       'current_category': filter.one_or_none()})

    @app.errorhandler(404)
    def not_found():
        return jsonify({'success': False,
                       'message': 'Resource was not found on the server'
                       , 'error_code': 404})

    @app.errorhandler(422)
    def unprocessable():
        return jsonify({'success': False,
                       'message': 'Request could not be processed',
                       'error_code': 422})

    @app.errorhandler(400)
    def bad_request():
        return jsonify({'success': False, 'message': 'Bad request',
                       'error_code': 400})

    @app.errorhandler(405)
    def method_not_allowed():
        return jsonify({'success': False,
                       'message': 'Method is not allowed on requested resource'
                       , 'error_code': 405})

    @app.errorhandler(408)
    def request_timeout():
        return jsonify({'success': False, 'message': 'Request timed out'
                       , 'error_code': 408})

    @app.errorhandler(500)
    def server_error():
        return jsonify({'success': False,
                       'message': 'Internal Server Error',
                       'error_code': 500})

    return app
