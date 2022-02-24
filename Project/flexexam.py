
def flex_timeexam(data_flex):
    
    # print(data_flex)
    
    tempday = ""
    flex_box = ""
    text = """
              ]
            }"""

    for i in range(len(data_flex)):

        # print("loop " ,i ," = ",data_flex[i][8])
        # print(" ")
      day = data_flex[i][11]

      # print(tempday)

      if tempday != day :
        
        if i > 0 :
          # print(data_flex[i])
          flex_box = """%s %s %s %s """%(flex_box,flex_day,flex_course,text)
          # print(flex_box)
          
        flex_day =  """,{
            "type": "box",
            "layout": "vertical",
            "margin": "sm",
            "contents": [
              {
                "type": "text",
                "text": "%s",
                "weight": "bold",
                "color": "#8603D0"
              }"""%(str(data_flex[i][11]))
        
        tempday = day 
        # print(tempday ," / ", day)
        flex_course = ""
      
      flex_course = flex_course + """,{
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "%s %s",
                "size": "sm",
                "weight": "bold",
                "flex": 0 ,
                "wrap": true
              }, 
              {
                "type": "text",
                "text": " - %s",
                "flex": 8,
                "weight": "regular",
                "style": "italic"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "time : %s - %s",
                "wrap": true,
                "size": "sm",
                "color": "#737373"
              },
              {
                "type": "text",
                "text": "room : %s",
                "color": "#737373",
                "size": "sm",
                "wrap": true
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "sec : %s  ",
                "size": "sm",
                "color": "#737373",
                "wrap": true
              },
              {
                "type": "text",
                "text": "seat number : %s",
                "color": "#737373",
                "size": "sm"
              }
            ]
          }"""%(str(data_flex[i][7]),str(data_flex[i][8]),str(data_flex[i][15]),str(data_flex[i][9]),str(data_flex[i][10]),str(data_flex[i][13]),str(data_flex[i][12]),str(data_flex[i][14]))

      # print(flex_course)
      

    if flex_box != "" and flex_course != "" :
      # print("end loop")
      # print(flex_box)    
      
      name = """{
                          "type": "text",
                          "text": "%s",
                          "weight": "bold",
                          "size": "xl",
                          "color": "#F9934b"
                      },
                      {
                          "type": "text",
                          "text": "%s%s %s",
                          "color": "#00182E",
                          "weight": "bold"
                      },
                      {
                          "type": "text",
                          "text": "Exam schedule %s/%s",
                          "color": "#aaaaaa",
                          "size": "sm"
                      },
                      {
                          "type": "separator",
                          "margin": "lg"
                      }"""%(str(data_flex[i][0]),str(data_flex[i][3]),str(data_flex[i][1]),str(data_flex[i][2]),str(data_flex[i][5]),str(data_flex[i][6]))

      result =  """{
              "type": "bubble",
              "direction": "ltr",
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
                  "contents": [%s %s %s %s %s]
                  }
              }
              """%(name,flex_box,flex_day,flex_course,text)
      
      # result = """%s %s %s %s %s %s"""%(flex_name,flex_box,flex_day,flex_course,text,textend)

      
    # print(result)
      # print("V\nV\nV\nV\nV\nV\nV\nV")
    return result
      



# flex_course =  flex_course + ''',{
#         "type": "box",
#         "layout": "vertical",
#         "margin": "sm",
#         "contents": [
#           {
#             "type": "text",
#             "text": "%s",
#             "weight": "bold",
#             "color": "#884dff"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "%s %s",
#                 "size": "sm",
#                 "weight": "bold",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "time : %s - %s",
#                 "wrap": true,
#                 "size": "sm",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "room : %s",
#                 "flex": 10,
#                 "size": "sm"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "sec : %s  ",
#                 "size": "sm",
#                 "flex": 4,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "seat number : %s",
#                 "flex": 10,
#                 "size": "sm"
#               },
#               {
#                 "type": "text",
#                 "text": "%s",
#                 "flex": 8,
#                 "weight": "regular",
#                 "style": "italic"
#               }
#             ]
#           }'''%(str(data_flex[i][11]),str(data_flex[i][7]),str(data_flex[i][8]),str(data_flex[i][9]),str(data_flex[i][10]),str(data_flex[i][13]),str(data_flex[i][12]),str(data_flex[i][14]),str(data_flex[i][15]))









































# {
#   "type": "bubble",
#   "direction": "ltr",
#   "hero": {
#     "type": "image",
#     "url": "https://sv1.picz.in.th/images/2022/02/11/rYV0LP.png",
#     "size": "full",
#     "aspectRatio": "12:5",
#     "aspectMode": "cover"
#   },
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "contents": [
#       {
#         "type": "text",
#         "text": "61314601",
#         "weight": "bold",
#         "size": "xl",
#         "color": "#FF9933"
#       },
#       {
#         "type": "text",
#         "text": "Mr.Saendee janangkaan",
#         "weight": "bold"
#       },
#       {
#         "type": "text",
#         "text": "Exam schedule 2/2564",
#         "color": "#aaaaaa",
#         "size": "sm"
#       },
#       {
#         "type": "separator",
#         "margin": "lg"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "sm",
#         "contents": [
#           {
#             "type": "text",
#             "text": "12 jan 2022",
#             "weight": "bold",
#             "color": "#884dff"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001201 Population",
#                 "size": "sm",
#                 "weight": "bold",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "time : 09:00 - 12:00",
#                 "wrap": true,
#                 "size": "sm",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "room : QS2201",
#                 "flex": 10,
#                 "size": "sm"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "sec : 2  ",
#                 "size": "sm",
#                 "flex": 4,
#                 "wrap": true
#               },
#               {
#                 "type": "text",
#                 "text": "seat number : 60",
#                 "flex": 10,
#                 "size": "sm"
#               },
#               {
#                 "type": "text",
#                 "text": "midterm",
#                 "flex": 8,
#                 "weight": "regular",
#                 "style": "italic"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "margin": "none",
#             "spacing": "none",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "spacing": "sm",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "001202 Internet Programming",
#                     "size": "sm",
#                     "weight": "bold",
#                     "flex": 0
#                   }
#                 ]
#               },
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "spacing": "sm",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "time : 15:00 - 17:00",
#                     "wrap": true,
#                     "size": "sm",
#                     "flex": 10
#                   },
#                   {
#                     "type": "text",
#                     "text": "room : QS2201",
#                     "flex": 10,
#                     "size": "sm"
#                   }
#                 ]
#               },
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "sec : 1",
#                     "size": "sm",
#                     "flex": 4
#                   },
#                   {
#                     "type": "text",
#                     "text": "seat number : 60",
#                     "flex": 10,
#                     "size": "sm"
#                   },
#                   {
#                     "type": "text",
#                     "text": "midterm",
#                     "flex": 8,
#                     "weight": "regular",
#                     "style": "italic"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "lg",
#         "contents": [
#           {
#             "type": "text",
#             "text": "13 jan 2022",
#             "weight": "bold",
#             "color": "#884dff"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001203 Internet of Things",
#                 "size": "sm",
#                 "weight": "bold",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "time : 10:00 - 12:00",
#                 "wrap": true,
#                 "size": "sm",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "room : SC1-311",
#                 "flex": 10,
#                 "size": "sm"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "sec : 1",
#                 "size": "sm",
#                 "flex": 4
#               },
#               {
#                 "type": "text",
#                 "text": "seat number : 60",
#                 "flex": 10,
#                 "size": "sm"
#               },
#               {
#                 "type": "text",
#                 "text": "midterm",
#                 "flex": 8,
#                 "weight": "regular",
#                 "style": "italic"
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "lg",
#         "contents": [
#           {
#             "type": "text",
#             "text": "15 jan 2022",
#             "weight": "bold",
#             "color": "#884dff"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001204 Communicative English for Academic Analysis in Computer Technology",
#                 "size": "sm",
#                 "weight": "bold",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "time : 09:00 - 12:00",
#                 "wrap": true,
#                 "size": "sm",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "room : QS2201",
#                 "flex": 10,
#                 "size": "sm"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "sec : 3",
#                 "size": "sm",
#                 "flex": 4
#               },
#               {
#                 "type": "text",
#                 "text": "seat number : 60",
#                 "flex": 10,
#                 "size": "sm"
#               },
#               {
#                 "type": "text",
#                 "text": "midterm",
#                 "flex": 8,
#                 "weight": "regular",
#                 "style": "italic"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "margin": "none",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "spacing": "sm",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "001205 Robotic",
#                     "size": "sm",
#                     "weight": "bold",
#                     "flex": 0
#                   }
#                 ]
#               },
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "spacing": "sm",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "time : 15:00 - 17:00",
#                     "wrap": true,
#                     "size": "sm",
#                     "flex": 10
#                   },
#                   {
#                     "type": "text",
#                     "text": "room : QS2201",
#                     "flex": 10,
#                     "size": "sm"
#                   }
#                 ]
#               },
#               {
#                 "type": "box",
#                 "layout": "baseline",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "sec : 1",
#                     "size": "sm",
#                     "flex": 4
#                   },
#                   {
#                     "type": "text",
#                     "text": "seat number : 60",
#                     "flex": 10,
#                     "size": "sm"
#                   },
#                   {
#                     "type": "text",
#                     "text": "midterm",
#                     "flex": 8,
#                     "weight": "regular",
#                     "style": "italic"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "lg",
#         "contents": [
#           {
#             "type": "text",
#             "text": "18 jan 2022",
#             "weight": "bold",
#             "color": "#884dff"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001206 Software Engineer",
#                 "size": "sm",
#                 "weight": "bold",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "time : 12:00 - 14:00",
#                 "wrap": true,
#                 "size": "sm",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "room : QS2201",
#                 "flex": 10,
#                 "size": "sm"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "sec : 2",
#                 "size": "sm",
#                 "flex": 4
#               },
#               {
#                 "type": "text",
#                 "text": "seat number : 60",
#                 "flex": 10,
#                 "size": "sm"
#               },
#               {
#                 "type": "text",
#                 "text": "midterm",
#                 "flex": 8,
#                 "weight": "regular",
#                 "style": "italic"
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "lg",
#         "contents": [
#           {
#             "type": "text",
#             "text": "20 jan 2022",
#             "weight": "bold",
#             "color": "#884dff"
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001207 Artificial Intelligence",
#                 "size": "sm",
#                 "weight": "bold",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "time : 10:00 - 12:00",
#                 "wrap": true,
#                 "size": "sm",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "room : QS2201",
#                 "flex": 10,
#                 "size": "sm"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "sec : 2",
#                 "size": "sm",
#                 "flex": 4
#               },
#               {
#                 "type": "text",
#                 "text": "seat number : 60",
#                 "flex": 10,
#                 "size": "sm"
#               },
#               {
#                 "type": "text",
#                 "text": "midterm",
#                 "flex": 8,
#                 "weight": "regular",
#                 "style": "italic"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "001208 Samena",
#                 "size": "sm",
#                 "weight": "bold",
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "spacing": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "time : 15:00- 17:00",
#                 "wrap": true,
#                 "size": "sm",
#                 "flex": 10
#               },
#               {
#                 "type": "text",
#                 "text": "room : SC2-208",
#                 "flex": 10,
#                 "size": "sm"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "baseline",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "sec : 2",
#                 "size": "sm",
#                 "flex": 4
#               },
#               {
#                 "type": "text",
#                 "text": "seat number : 60",
#                 "flex": 10,
#                 "size": "sm"
#               },
#               {
#                 "type": "text",
#                 "text": "midterm",
#                 "flex": 8,
#                 "weight": "regular",
#                 "style": "italic"
#               }
#             ]
#           }
#         ]
#       }
#     ]
#   }
# }