다운로드 API
==========
    
.. http:get:: /storages/download/{content_id}/?type

    :content_id: **Required**. 다운받으려는 패키지의 콘텐츠 Id
    :type: **Required**. 다운 받으려는 종류(package, arcontents, training, application)

콘텐츠의 패키지, ar, train, 응용을 다운 받기 위한 URL을 요청하는 API

example:

::

    http://{domain}/storages/download/12345678?type=package
    http://{domain}/storages/download/12345678?type=arcontents
    http://{domain}/storages/download/12345678?type=training
    http://{domain}/storages/download/12345678?type=application

Results:

.. sourcecode:: js

  {
    "error": {
      "code": 200,
      "message": "success"
    },
    "url": "http://storages.kepcovr.co.kr/contents/context.zip"
  }
