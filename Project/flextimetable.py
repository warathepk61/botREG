def flex_timetable(data_flex):
    # print("first = ",data_flex)
    # print(len(data_flex))
        
    tempday = ""
    flex_box = ""
    text = """ ]
            }
        }"""
    #   print(len(data_flex))
    
    for i in range(len(data_flex)):
        # print(" ")
        # print('time table = ',data_flex[i])
        
        day = data_flex[i][15]
        # print(len(data_flex))
        # tempday = ''
        # print(tempday)
        
        if  tempday != day :
            
            if i > 0  :
                # print('data = ',data_flex[i])
                # flex_name + flex_course
                flex_box = flex_box + """%s %s %s, """%(flex_name,flex_course,text)
            
            
            flex_name = """{
                "type": "bubble",
                "hero": {
                "type": "image",
                "url": "https://sv1.picz.in.th/images/2022/02/23/rivaxQ.png",
                "size": "full",
                "aspectRatio": "12:5",
                "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "%s",
                            "weight": "bold",
                            "color": "#F9934b",
                            "size": "xl"
                        },
                        {
                            "type": "text",
                            "text": "%s%s %s",
                            "color": "#00182E",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "Class schedule %s/%s",
                            "size": "sm",
                            "color": "#aaaaaa"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "%s",
                                    "flex": 1,
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#884dff"
                                },
                                {
                                    "type": "separator",
                                    "margin": "xs"
                                }
                            ]
                        }"""%(str(data_flex[i][0]),str(data_flex[i][3]),str(data_flex[i][1]),str(data_flex[i][2]),str(data_flex[i][6]),str(data_flex[i][5]),str(data_flex[i][15]))
            # print(flex_name)
            tempday = day 
            # print(tempday ," / ", day)
            flex_course = ""
            
        flex_course = flex_course + """,{
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "%s (%s) %s",
                                    "size": "sm",
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "size": "sm",
                                    "color": "#737373",
                                    "text": "room: %s time: %s-%s sec: %s"
                                }
                            ],
                            "margin": "sm"
                        }"""%(str(data_flex[i][8]),str(data_flex[i][9]),str(data_flex[i][7]),str(data_flex[i][13]),str(data_flex[i][10]),str(data_flex[i][11]),str(data_flex[i][12]))
        #   print(flex_course)
            
    if flex_box != "" and flex_course != "" and flex_name != "" :
            # print("end loop")
            # print("loop" ,i+1)

            textend = """ ]
                    }
                    }
                    """

            # flex_box = flex_box + flex_name + flex_course + textend
        #     print(flex_box)
    # print("V\nV\nV\nV\nV\nV\nV\nV")
    result = """
                {
                    "type": "carousel",
                    "contents": [%s %s %s %s]
                }
                """%(flex_box,flex_name,flex_course,textend)

    
    #   print(result)
    return result

 


  
# {
#     "type": "carousel",
#     "contents": [
#         {
#             "type": "bubble",
#             "body": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                     {
#                         "type": "text",
#                         "text": "61314601",
#                         "weight": "bold",
#                         "color": "#FF7500",
#                         "size": "xl"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Mr.Swaddee Taweesuk",
#                         "color": "#00182E",
#                         "weight": "bold"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Class schedule 2/2564",
#                         "size": "sm",
#                         "color": "#aaaaaa"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "Monday",
#                                 "flex": 1,
#                                 "weight": "bold",
#                                 "size": "lg",
#                                 "color": "#0C6BA1"
#                             },
#                             {
#                                 "type": "separator",
#                                 "margin": "xs"
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "001201 (C) Population",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: QS2201 time: 09:00-12:00 sec: 1"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001202 (C) Internet Programming",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC1-204 time: 13:00-15:00 sec: 1"
#                             }
#                         ],
#                         "margin": "sm"
#                     }
#                 ]
#             }
#         },
#         {
#             "type": "bubble",
#             "body": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                     {
#                         "type": "text",
#                         "text": "61314601",
#                         "weight": "bold",
#                         "color": "#FF7500",
#                         "size": "xl"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Mr.Swaddee Taweesuk",
#                         "color": "#00182E",
#                         "weight": "bold"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Class schedule 2/2564",
#                         "size": "sm",
#                         "color": "#aaaaaa"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "Tuesday",
#                                 "flex": 1,
#                                 "weight": "bold",
#                                 "size": "lg",
#                                 "color": "#0C6BA1"
#                             },
#                             {
#                                 "type": "separator",
#                                 "margin": "xs"
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "001203 (C) Internet of Things",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC2-307 time: 08:00-10:00 sec: 2"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001204 (C) Communicative English for Academic Analysis in Computer Technology",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC2-208 time: 13:00-15:00 sec: 3"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001205 (C) Robotic",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC2-307 time: 15:00-17:00 sec: 1"
#                             }
#                         ],
#                         "margin": "sm"
#                     }
#                 ]
#             }
#         },
#         {
#             "type": "bubble",
#             "body": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                     {
#                         "type": "text",
#                         "text": "61314601",
#                         "weight": "bold",
#                         "color": "#FF7500",
#                         "size": "xl"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Mr.Swaddee Taweesuk",
#                         "color": "#00182E",
#                         "weight": "bold"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Class schedule 2/2564",
#                         "size": "sm",
#                         "color": "#aaaaaa"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "Wednesday",
#                                 "flex": 1,
#                                 "weight": "bold",
#                                 "size": "lg",
#                                 "color": "#0C6BA1"
#                             },
#                             {
#                                 "type": "separator",
#                                 "margin": "xs"
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "001206 (L) Software Engineer",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC1-304 time: 10:00-12:00 sec: 1"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001203 (L) Internet of Things",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC2-308 time: 13:00-15:00 sec: 2"
#                             }
#                         ],
#                         "margin": "sm"
#                     }
#                 ]
#             }
#         },
#         {
#             "type": "bubble",
#             "body": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                     {
#                         "type": "text",
#                         "text": "61314601",
#                         "weight": "bold",
#                         "color": "#FF7500",
#                         "size": "xl"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Mr.Swaddee Taweesuk",
#                         "color": "#00182E",
#                         "weight": "bold"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Class schedule 2/2564",
#                         "size": "sm",
#                         "color": "#aaaaaa"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "Thursday",
#                                 "flex": 1,
#                                 "weight": "bold",
#                                 "size": "lg",
#                                 "color": "#0C6BA1"
#                             },
#                             {
#                                 "type": "separator",
#                                 "margin": "xs"
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "001207 (C) Artificial Intelligence",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC1-205 time: 08:00-10:00 sec: 1"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001208 (C) Samena",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC1-311 time: 12:00-15:00 sec: 1"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001202 (L) Internet Programming",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC2-209 time: 15:00-17:00 sec: 1"
#                             }
#                         ],
#                         "margin": "sm"
#                     }
#                 ]
#             }
#         },
#         {
#             "type": "bubble",
#             "body": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                     {
#                         "type": "text",
#                         "text": "61314601",
#                         "weight": "bold",
#                         "color": "#FF7500",
#                         "size": "xl"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Mr.Swaddee Taweesuk",
#                         "color": "#00182E",
#                         "weight": "bold"
#                     },
#                     {
#                         "type": "text",
#                         "text": "Class schedule 2/2564",
#                         "size": "sm",
#                         "color": "#aaaaaa"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "Friday",
#                                 "flex": 1,
#                                 "weight": "bold",
#                                 "size": "lg",
#                                 "color": "#0C6BA1"
#                             },
#                             {
#                                 "type": "separator",
#                                 "margin": "xs"
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "001205 (L) Robotic",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC2-207 time: 10:00-12:00 sec: 1"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001206 (C) Software Engineer",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC1-205 time: 13:00-15:00 sec: 1"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "001207 (L) Artificial Intelligence",
#                                 "size": "sm",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "size": "sm",
#                                 "color": "#aaaaaa",
#                                 "text": "room: SC2-308 time: 15:00-17:00 sec: 1"
#                             }
#                         ],
#                         "margin": "sm"
#                     }
#                 ]
#             }
#         }
#     ]
# }