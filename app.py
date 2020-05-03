#imports
import settings
from flask import Flask, jsonify, request,Response
from flask_cors import CORS
from flask_restful import Resource, Api
from Services import GetCOVIDdata
from Services.GetLatestAggCovidData import RetriveLatestAggData
from Services.GetAllAggData import RetriveAggData
from Services.GetAllIndiaData import RetriveIndiaData
from Services.GetIndiaAggData import RetriveAggIndiaData
from Services.GetLatesNews import  RetriveLatestNews
from Services.GetMythBusters import  RetriveMythBusters

import json
#provides a wrapper function around json.dumps to remove typeerror
#see https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
from bson.json_util import dumps
from db import mongo

from pathlib import Path
# creating the flask app 
app = Flask(__name__) 
CORS(app)
# creating an API object 
api = Api(app) 
#loading .env file for production



class GetLatestAggData(Resource):
    # corresponds to the GET request. 
    # this function is called whenever there 
    # is a GET request for this resource 
    def get(self): 
        try:
            getCovidData=RetriveLatestAggData().get_latest_agg_data()
            res=[]
            for data in getCovidData:
                res.append(data)
            return Response(dumps(res) ,status=200,mimetype='application/json')
        except Exception as err:
            return Response(jsonify({"error":str(err)}),status=500,mimetype='application/json')

class GetAggData(Resource):
    def get(self): 
        try:
            getCovidData=RetriveAggData().get_agg_data()
            res=[]
            for data in getCovidData:
                res.append(data)
            return Response(dumps(res) ,status=200,mimetype='application/json')
        except Exception as err:
            return Response(jsonify({"error":str(err)}),status=500,mimetype='application/json')

class GetAllLatestData(Resource):
    def get(self):
        try:
            get_Covid_data=GetCOVIDdata.RetriveCOVIdDATA()
            res=get_Covid_data.get_data_allcountries()
            list_=[]
            for data in res:
                list_.append(data)
            
            return Response(dumps(list_) ,status=200,mimetype='application/json')
        except Exception as err:
            return Response(jsonify({"error":str(err)}),status=500,mimetype='application/json')

class GetAllIndiaData(Resource):
    def get(self):
        try:
            get_allindia_data=RetriveIndiaData().get_data()
            list_=[]
            for data in get_allindia_data:
                list_.append(data)
            
            return Response(dumps(list_),status=200,mimetype='application/json')
        except Exception as err:
            return Response(jsonify({"error":str(err)}),status=500,mimetype='application/json')
        
class GetAllAggIndiaData(Resource):
    
        def get(self):
            try:
                getAggData=RetriveAggIndiaData().get_data()
                list_=[]
                for data in getAggData:
                    list_.append(data)
                return Response(dumps(list_),status=200,mimetype='application/json')
            except Exception as err:
                return Response(dumps(list_),status=200,mimetype='application/json')
          
        
    
class GetLatestIndiaNews(Resource):
    def get(self):
            try:
                res=RetriveLatestNews().get_india_news()
                list_=[]
                for data in res:
                    list_.append(data)
                return Response(dumps(list_),status=200,mimetype='application/json')
            except Exception as err:
                return Response(jsonify({"error":str(err)}),status=500,mimetype='application/json')

class GetLatestWorldNews(Resource):
    def get(self):
        try:
            res=RetriveLatestNews().get_global_news()
            list_=[]
            for data in res:
                list_.append(data)
            return Response(dumps(list_),status=200,mimetype='application/json')
        except Exception as err:
            return Response(jsonify({"error":str(err)}),status=500,mimetype='application/json')


class  GetMythBusters(Resource):
    def get(self):
        try:
            res=RetriveMythBusters().get_mythbusters()
            list_=[]
            for data in res:
                list_.append(data)
            return Response(dumps(list_),status=200,mimetype='application/json')
        except Exception as err:
            return Response(jsonify({"error":str(err)}),status=500,mimetype='application/json')

api.add_resource(GetLatestAggData,'/Jijivisha/v1.0/GetLatestAggData')
api.add_resource(GetAggData,'/Jijivisha/v1.0/GetAllAggData')
api.add_resource(GetAllLatestData,'/Jijivisha/v1.0/GetAllLatestData')
api.add_resource(GetAllIndiaData,'/Jijivisha/v1.0/GetAllIndiaData')
api.add_resource(GetAllAggIndiaData,'/Jijivisha/v1.0/GetAllAggIndiaData')
api.add_resource(GetLatestIndiaNews,'/Jijivisha/v1.0/GetAllLatestIndiaNews')
api.add_resource(GetLatestWorldNews,'/Jijivisha/v1.0/GetAllLatestWorldNews')
api.add_resource(GetMythBusters,'/Jijivisha/v1.0/GetMythBusters')
# driver function 
if __name__ == '__main__':  
   
   
    app.run(debug = True,host='0.0.0.0',port=5001) 
   