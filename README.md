# Basic-Django-to-Learn
01. basic build -in template (e..g includes, extends)
02. custom template tag
03. custom context processor
04. middle-ware
05. custom decorator
06. mixin
07. Model manager
08. django query(read officaial docs for (Making queries, QuerySet API)
09. make custom 404 and 500 page
10. django file upload (make clean method not more than 10mb file, and if file is image will be crop with a ratio, make sure joto tuku neoar jay nibo)
11. phonenumber_field
12. django-geoposition
13. simple_history
14. python-decouple
15. requests  (Python package)
16. Import/export outside admin site,( should be done manually, not using app )
17. learn package 'django ckeditor'
18. django pdf response (file download and preview in browser both option)
19. custom management command
20. json response/ json data type / rest api(concept), / json response vs http response 
21. django with postgres (overwrite the user model with using Django json field and the email should be unique) 
22. cron job (Python + OS)
23. cache, session, cookie (just read)
24. django test






# JsonResponse
JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response. Its default Content-Type header is set to application/json. The first parameter, data, should be a dict instance. If the safe parameter is set to False, any object can be passed for serialization; otherwise only dict instances are allowed.

Example for json data:
{
  "name" : "kazal",
  "result" : true,
  "grade" : null,
  "rollno" : 210
}


# JSON Data Types
In JSON, values must be one of the following data types:
a string
a number
an object (JSON object)
an array
a boolean
null

JSON values cannot be one of the following data types:
a function
a date
undefined


# JsonResponse vs HttpResponse 
HTTPResponse
    HTTPResponse (content=response body, content_type=response body data type, status=status code)
    Suitable for string, templates
    class HttpResponse(HttpResponseBase):

JsonReponse
    It is a subclass of HTTPResponse,
    Suitable for processing data in json format, but can not return templates.
    class JsonResponse(HttpResponse):


# REST API (RESTful API)
A RESTful API is an architectural style for an application program interface (API) that uses HTTP requests to access and use data. That data can be used to GET, PUT, POST and DELETE data types, which refers to the reading, updating, creating and deleting of operations concerning resources.

An API for a website is code that allows two software programs to communicate with each other. The API spells out the proper way for a developer to write a program requesting services from an operating system or other application.

A RESTful API -- also referred to as a RESTful web service or REST API -- is based on representational state transfer (REST), which is an architectural style and approach to communications often used in web services development.

REST technology is generally preferred over other similar technologies. This tends to be the case because REST uses less bandwidth, making it more suitable for efficient internet usage. RESTful APIs can also be built with programming languages such as JavaScript or Python.


