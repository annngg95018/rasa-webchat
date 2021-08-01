# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import datetime as dt
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []

class ActionParkingSpace(Action):

    def name(self) -> Text:
        return "action_show_parking_space"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        covid_resources = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "PARKING SPACE",
                    "subtitle": "FIND SPACE, SAVE TIEM.",
                    "image_url": "static/parking-space-template-vector-18862836.jpg",
                    "buttons": [
                        {
                            "title": "B1",
                            "url": "static/B1.png",
                            "type": "web_url"
                        },

                        {
                            "title": "B2",
                            "url": "static/B2.png",
                            "type": "web_url"
                        },
                        
                        {
                            "title": "B3",
                            "url": "static/B1.png",
                            "type": "web_url"
                        }
                    ]
                }
                ]
            }
        }

        dispatcher.utter_message(attachment=covid_resources)
        return []
