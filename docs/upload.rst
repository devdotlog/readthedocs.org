업로드 API
=========

업로드 API는 3rd Party의 앱 혹은 장비에서 VR 콘텐츠를 업로드 할 수 있는 기능을 제공합니다.

Ticket
------

전력설비 콘텐츠
~~~~~~~~~~

.. http:post::  /storages/ticket/standard

  form-data
  
  :title: **Required**. 콘텐츠 제목.
  :status: **Required**. 0은 draft.
  :version: **Required**. 콘텐츠의 버전.
  :version_changes: **Required**. 콘텐츠 변경 상태 정보.
  :contents_type: **Required**. 전력 설비는 전력표준 메뉴 API를 참조.
  

표준 콘텐츠를 업로드하기 위한 Ticket의 발급을 요청하는 API. 
표준 콘텐츠는 표준 설비와 카테고리에 속하는 콘텐츠.

Response:

.. sourcecode:: js

  {
    "error": {
      "code": 0,
      "message": "success"
      },
      "ticket": "adfe123sdf3423.23423.234234sds"
  }

카테고리 콘텐츠
~~~~~~~~~~~~

.. http:post::  /storages/ticket/standard

  form-data
  
  :title: **Required**. 콘텐츠 제목.
  :status: **Required**. 0은 draft.
  :version: **Required**. 콘텐츠의 버전.
  :version_changes: **Required**. 콘텐츠 변경 상태 정보.
  :contents_type: **Required**. 콘텐츠 코드표를 참조.
  :info: **Required**. 콘텐츠 정보.
  :description: **Required**. 콘텐츠의 설명.
  
카테고리 콘텐츠를 업로드하기 위한 Ticket의 발급을 요청하는 API. 
카테고리 콘텐츠는 13개의 하위 contypes_types을 갖고 있다.

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      },
    "ticket": "adfe123sdf3423.23423.234234sds"
  }

AR 콘텐츠
~~~~~~~~

.. http:post:: /storages/ticket/ar

.. sourcecode:: js

  Header:
  Content-Type: application/json

  Body:
  {
          "common": {
                  "title": "Python is Hot",
                  "status": 0, (0: draft)
                  “version”: “1.0.0”,
                  "version_changes": "frist release"
                  “contents_type”: id (AR Code표 참조)
          },
          "training": {
                  "trackable": "Visual pattern",
                  "width": 640,
                  "height": 480,
                  "training_id": 10,
                  "name": "data01",
                  "electronic_name": "분전반_10" ,
                  "gps_latitude": "123123.123123",
                  "gps_longitude": "123123.123123",
                  "tracker_name": "Optical Flow",
                  "number_features": 300,
                  "detector_method": "FLANN",
                  "descriptor": 0, (0: SURF, 1: SIFT, 2: ORB, 3: 기타)
                  "filename": "asdfasf.zip"
          },
          "ar_contents": [
                  {
                          "id": 10,
                          "name": "765kV 개폐기_10",
                          "provider": "keti",
                          "service_name": "Test1",
                          "ar_stand": 0, (0: ARML, 1: ARAF, 3: 기타)
                          "standard_filename": "xxxx.xml",
                          "creation_time: "12313123213",
                          "model": 0, (0: 2D, 1, 3D)
                          "standard_raw": "xxxx.zip"
                  }
          ]
  }

AR 콘텐츠를 업로드하기 위한 Ticket의 발급을 요청하는 API. 
AR 콘텐츠는 2개의 하위 contypes_types을 갖고 있다.

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      },
    "ticket": "adfe123sdf3423.23423.234234sds"
  }

AR/VR 응용 콘텐츠
~~~~~~~~~~~~~~~

.. http:post:: /storages/ticket/application

  form-data
  
  :title: **Required**. 콘텐츠 제목.
  :status: **Required**. 0은 draft.
  :version: **Required**. 콘텐츠의 버전.
  :version_changes: **Required**. 콘텐츠 변경 상태 정보.
  :contents_type: **Required**. 콘텐츠 코드표를 참조.

AR/VR 응용 콘텐츠를 업로드하기 위한 Ticket의 발급을 요청하는 API. 
AR/VR 응용 콘텐츠는 2개의 하위 contypes_types을 갖고 있다.

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      },
    "ticket": "adfe123sdf3423.23423.234234sds"
  }

이미지
------

.. http:post:: /storages/images/{ticket}

  :ticket: **Required**. 콘텐츠를 업로드위해 발급 받은 ticket.
  
  form-data
  
  :key: **Required**. key / value: filename
  :key: **Required**. file / value: file
    
콘텐츠에 해당하는 이미지를 업로드하기 위한 API. 

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      }
  }
  
콘텐츠
------

전력설비, 카테고리 콘텐츠
~~~~~~~~~~~~~~~~~~~~

.. http:post:: /storages/packages/{ticket}
  
  :ticket: **Required**. ticket.
  
  form-data
  
  :key: **Required**. file / file.zip
  
전력표준, 카테고리 콘텐츠를 업로드하기 API. 

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      },
  }
  
AR 콘텐츠
~~~~~~~~

.. http:post:: /storages/arcontents/{ticket}
  
  :ticket: **Required**. ticket.
  
  form-data
  
  :key: **Required**. file / file.zip
  
AR 콘텐츠를 업로드하기 API. 

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      },
  }

AR 콘텐츠의 training
~~~~~~~~~~~~~~~~~~

.. http:post:: /storages/training/{ticket}
  
  :ticket: **Required**. ticket.
  
  form-data
  
  :key: **Required**. file / descriptor.zip
  
AR 콘텐츠의 Trainning 파일를 업로드하기 API. 

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      },
  }

AR/VR 응용 콘텐츠
~~~~~~~~~~~~~~~

.. http:post::  /storages/application/{ticket}
  
  :ticket: **Required**. ticket.
  
  form-data
  
  :key: **Required**. file / projects.zip
  
AR/VR 응용 콘텐츠를 업로드하기 API. 

Response:

.. sourcecode:: js
    
  {
    "error": {
      "code": 0,
      "message": "success"
      },
  }
  
