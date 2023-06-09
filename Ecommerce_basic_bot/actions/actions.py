# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
# Tracker - conversation tracker. bot ka memory jaisa hai. past events aur current state of the conversation. 
# Action - action jo bot perform karta hai
# CollectingDispatcher - used to add responses to the response returned to the Rasa server.
# dispatcher se rasa server mein jayega aur fir udhar se user ko jayega. 
# utter_message seedha user ko jayega.
# run method gets executed when the action is triggered.
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
