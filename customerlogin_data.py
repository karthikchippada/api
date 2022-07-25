import os
from urllib import response

import pymongo
from pymongo import MongoClient
from rest_framework import status
from rest_framework.response import Response

from utils.check_data import ecomerce_presence

from utils.mongo_func import connect




class child_details:
    def __init__(self, user_name,password):
        self.user_name = user_name
        self.password=password
    
    def insert_data(self,db): #insertion function
        mylist=[
            {'user_name' : self.user_name,'password':self.password},
        ]
        db.teble5.insert_many(mylist)
    
    

 
def post_customerlogin_data(request):
    """
    Updating the major information of a particular child and update the stage to student_full_details/guardian_information depending on the guardian details presence

    Request.body need to have :
    parent_id
    student_id
    class_no
    section
    date_of_birth
    blood_group
    emergency_contact_no
    student_aadhar
    student_school_id
    student_profile

    Return
    status        : True/False depending on the successful execution of the request
    message       : Informative message, describing the response
    student_id    : ID against which the data has been updated
    upload_status : List containing the upload status of all the media files
    """




    res, message = ecomerce_presence(request, ["user_name","password"])

    if not res:
        return Response({'status' : False, 'message' : message}, status = 400)
    user_name = request.data.get('user_name')
    password=request.data.get('password')
    #
    print(res)
  
    try:
        client = connect()
       
    except:
       
        return Response({'status' : False, 'message' : 'Error in connecting with database'}, 502)

    db = client.ecomerce   # database name  

    new_child = child_details(user_name,password)
    new_child.insert_data(db)
    return Response("login success !",status=200)